from PIL import Image, ImageDraw, ImageFont

interactions = [
    {"cmd": "kubectl apply -f deployment.yaml", "out": ["deployment.apps/hpa-demo created"]},
    {"cmd": "kubectl get deployment", "out": ["NAME       READY   UP-TO-DATE   AVAILABLE   AGE", "hpa-demo   1/1     1            1           10s"]},
    {"cmd": "kubectl apply -f service.yaml", "out": ["service/hpa-demo-service created"]},
    {"cmd": "kubectl get svc", "out": ["NAME               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE", "hpa-demo-service   ClusterIP   10.101.44.11   <none>        80/TCP    10s"]},
    {"cmd": "kubectl apply -f hpa.yaml", "out": ["horizontalpodautoscaler.autoscaling/hpa-demo created"]},
    {"cmd": "kubectl get hpa", "out": ["NAME       REFERENCE             TARGETS         MINPODS   MAXPODS   REPLICAS   AGE", "hpa-demo   Deployment/hpa-demo   <unknown>/50%   1         5         1          10s"]},
    {"cmd": "", "out": []}
]

width = 1800
height = 800
bg_color = (24, 24, 24)
img = Image.new('RGB', (width, height), color=bg_color)
d = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 15)
except:
    font = ImageFont.load_default()

color_user_host = (35, 209, 139) # green
color_colon = (204, 204, 204) # white/gray
color_path = (59, 142, 234) # blue
color_text = (212, 208, 200) # light grey

prompt_user_host = "abhay@abhay-VivoBook-ASUSLaptop-X515DA-M515DA"
prompt_colon = ":"
prompt_path = "~/Documents/DevOps/devops-heros/session13/04-hpa"
prompt_dollar = "$ "

def draw_prompt(draw, x, y, cmd):
    draw.text((x, y), prompt_user_host, fill=color_user_host, font=font)
    x += draw.textlength(prompt_user_host, font=font)
    draw.text((x, y), prompt_colon, fill=color_colon, font=font)
    x += draw.textlength(prompt_colon, font=font)
    draw.text((x, y), prompt_path, fill=color_path, font=font)
    x += draw.textlength(prompt_path, font=font)
    draw.text((x, y), prompt_dollar + cmd, fill=color_text, font=font)

x_start = 20
y_text = 20

for interaction in interactions:
    draw_prompt(d, x_start, y_text, interaction["cmd"])
    y_text += 25
    for line in interaction["out"]:
        d.text((x_start, y_text), line, fill=color_text, font=font)
        y_text += 25

img.save('/home/abhay/Documents/DevOps/devops-heros/session13/assignment/ss/04_ss1.png')
print("Image created successfully")
