from PIL import Image, ImageDraw, ImageFont

# Define the terminal interactions
interactions = [
    {"cmd": "kubectl apply -f emptydir-pod.yaml", "out": ["pod/emptydir-demo created"]},
    {"cmd": "kubectl get pods", "out": ["NAME            READY   STATUS    RESTARTS   AGE", "emptydir-demo   1/1     Running   0          10s"]},
    {"cmd": "kubectl exec -it emptydir-demo -- bash", "out": ["root@emptydir-demo:/# echo \"Hello Kubernetes\" > /data/message.txt", "root@emptydir-demo:/# cat /data/message.txt", "Hello Kubernetes", "root@emptydir-demo:/# exit", "exit"]},
    {"cmd": "kubectl delete pod emptydir-demo", "out": ["pod \"emptydir-demo\" deleted"]},
    {"cmd": "kubectl apply -f emptydir-pod.yaml", "out": ["pod/emptydir-demo created"]},
    {"cmd": "kubectl exec emptydir-demo -- cat /data/message.txt", "out": ["cat: /data/message.txt: No such file or directory", "command terminated with exit code 1"]},
    {"cmd": "", "out": []}
]

# Create a black background image (dark gray/black like #1e1e1e)
width = 1800
height = 800
bg_color = (24, 24, 24)
img = Image.new('RGB', (width, height), color=bg_color)
d = ImageDraw.Draw(img)

# Try to load a font, if not default
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 15)
except:
    font = ImageFont.load_default()

# Colors
color_user_host = (35, 209, 139) # green
color_colon = (204, 204, 204) # white/gray
color_path = (59, 142, 234) # blue
color_text = (212, 208, 200) # light grey for commands/output

prompt_user_host = "abhay@abhay-VivoBook-ASUSLaptop-X515DA-M515DA"
prompt_colon = ":"
prompt_path = "~/Documents/DevOps/devops-heros/session13/01-volumes"
prompt_dollar = "$ "

def draw_prompt(draw, x, y, cmd):
    # draw user/host
    draw.text((x, y), prompt_user_host, fill=color_user_host, font=font)
    x += draw.textlength(prompt_user_host, font=font)
    
    # draw colon
    draw.text((x, y), prompt_colon, fill=color_colon, font=font)
    x += draw.textlength(prompt_colon, font=font)
    
    # draw path
    draw.text((x, y), prompt_path, fill=color_path, font=font)
    x += draw.textlength(prompt_path, font=font)
    
    # draw dollar and cmd
    draw.text((x, y), prompt_dollar + cmd, fill=color_text, font=font)

x_start = 20
y_text = 20

for interaction in interactions:
    draw_prompt(d, x_start, y_text, interaction["cmd"])
    y_text += 25
    for line in interaction["out"]:
        d.text((x_start, y_text), line, fill=color_text, font=font)
        y_text += 25

img.save('/home/abhay/Documents/DevOps/devops-heros/session13/assignment/ss/01_ss1.png')
print("Image created successfully")
