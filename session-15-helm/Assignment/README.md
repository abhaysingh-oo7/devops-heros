# Session 15: Helm Assignment


## Task 1: Helm Commands

Screenshots:

### Chart Creation, Rendering, and Linting

![Create and render demo-chart](ss/02-1.png)

![Render and install simple-chart](ss/03-1.png)

![Verify simple-chart resources](ss/03-2.png)

![Lint my-app chart](ss/04-1.png)

### Install, Upgrade, and Uninstall

![List releases and uninstall my-nginx](ss/01-1.png)

![Install demo-release](ss/02-2.png)

![Verify and uninstall demo-release](ss/02-3.png)

![Install and upgrade web-app](ss/07-1.png)

![Verify pods and uninstall web-app](ss/07-2.png)

### Task 2 Rollback

## Guestbook Deployment and Rollback

![Lint and render guestbook-chart](ss/09-1.png)

![Install and verify guestbook resources](ss/09-2.png)

![View history, rollback, and uninstall my-guestbook](ss/09-3.png)

### Task 3: Mini-Project

The complete chart structure and commands are documented in [mini-project/README.md](../mini-project/README.md). The screenshots provide the following evidence:

1. **Lint and render:** `helm lint notes-chart` passed, and `helm template notes-dev notes-chart` rendered the ConfigMap, Service, and Deployment.

	![Mini-project lint and rendered chart](ss/mini-project1.png)

2. **Workload verification:** the output shows three `notes-dev-deploy` pods in `Running` state, along with the cluster's other workloads.

	![Mini-project pods, Services, and ConfigMaps](ss/mini-project2.png)

3. **Upgrade and rollback:** the screenshot shows the production-values upgrade, Helm history through revision 5, an upgrade with an invalid image tag, rollback to revision 2, and uninstall. It confirms the rollback command succeeded, but does not capture pod health after rollback.

	![Mini-project upgrade history and rollback](ss/mini-project3.png)

4. **Cleanup check:** the Service is absent, while the Notes pods are still `Terminating` in this immediate listing. Wait for deletion to finish before claiming all resources are gone.

	![Mini-project cleanup check](ss/mini-project4.png)

