from PIL import Image, ImageDraw, ImageFont

interactions = [
    {"cmd": "kubectl get storageclass", "out": ["NAME                 PROVISIONER                RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE", "standard (default)   k8s.io/minikube-hostpath   Delete          Immediate           false                  29d"]},
    {"cmd": "kubectl describe storageclass standard", "out": ["Name:            standard", "IsDefaultClass:  Yes", "Provisioner:     k8s.io/minikube-hostpath", "ReclaimPolicy:   Delete", "VolumeBindingMode: Immediate"]},
    {"cmd": "kubectl apply -f pvc.yaml", "out": ["persistentvolumeclaim/dynamic-pvc created"]},
    {"cmd": "kubectl get pvc", "out": ["NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS", "dynamic-pvc   Bound    pvc-abbb9e83-1c76-47a3-91d6-11fdf082c7de   500Mi      RWO            standard"]},
    {"cmd": "kubectl get pv", "out": ["NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM", "pvc-abbb9e83-1c76-47a3-91d6-11fdf082c7de   500Mi      RWO            Delete           Bound    default/dynamic-pvc"]},
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
prompt_path = "~/Documents/DevOps/devops-heros/session13/03-storageclass"
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

img.save('/home/abhay/Documents/DevOps/devops-heros/session13/assignment/ss/03_ss1.png')
print("Image created successfully")
