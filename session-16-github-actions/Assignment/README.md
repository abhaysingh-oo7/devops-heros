# GitHub Actions CI/CD Demo

A small Python calculator project that demonstrates continuous integration and
continuous delivery with GitHub Actions. CI tests and packages every pull
request and push to `main`. CD publishes a Docker image to GitHub Container
Registry (GHCR) only after CI succeeds for a push to `main`.

> CD in this demo means **continuous delivery of a versioned container image**.
> It does not deploy to a running server or cloud account; no deployment target
> was specified.

## Project layout

```text
.
├── .github/workflows/
│   ├── ci.yml             # Test, build, Docker validation, artifact upload
│   └── cd.yml             # Publish the tested image to GHCR
├── app/                   # Calculator application
├── tests/                 # Automated tests
├── screenshots/                 # Screenshots
├── Dockerfile
├── build.sh               # Creates the downloadable application bundle
└── requirements.txt
```

## CI vs CD

- **Continuous Integration (CI)** frequently integrates changes and checks
  them automatically. Here, a push or pull request runs tests, packages the
  application, verifies the Docker image builds, and saves a downloadable
  artifact.
- **Continuous Delivery (CD)** takes a change that passed CI and prepares a
  deployable release. Here, a successful push to `main` publishes the Docker
  image to GHCR. Pull requests and failed CI runs cannot publish.
- **Continuous deployment** would additionally roll that release out to a live
  environment automatically. That is intentionally outside this demo.

## GitHub Actions concepts in this project

- A **workflow** is a YAML automation in `.github/workflows/`; these are the
  separate CI and CD pipelines.
- **Events** (`push`, `pull_request`, `workflow_run`) decide when a workflow
  starts. `workflow_dispatch` also permits manually starting CI.
- **Jobs** are units of work executed on a **runner**. The CI `build` job has
  `needs: test`, so it cannot run unless tests pass. CD runs on a GitHub-hosted
  `ubuntu-latest` runner after the successful CI workflow.
- **Steps** are individual commands or reusable actions within a job, such as
  checking out code, setting up Python, running pytest, and uploading an
  artifact.
- **Secrets** are sensitive values made available to a workflow without
  hard-coding them. CD uses GitHub's automatically provided
  `secrets.GITHUB_TOKEN` to authenticate to GHCR. Its permissions are limited
  to `contents: read` and `packages: write`; no personal access token or
  manually configured secret is needed.
- **Artifacts** are files produced by a workflow. CI uploads the contents of
  `build/` under a commit-specific artifact name; find it on the successful
  CI run's **Artifacts** section. The container image is the CD deliverable.

Execution Screenshots:

![Execution Screenshot](image.png)