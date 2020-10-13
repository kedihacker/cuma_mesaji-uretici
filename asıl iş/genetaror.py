try:
    import sys
    import json
    import os
    import random
    import textwrap

    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
except ImportError as err:
    print(f"Import Error in {sys.argv[0]}:\n{err}")
    sys.exit()

os.system("mkdir finisheds")

messages = json.loads(open("im_messages.json", "r", encoding="utf-8").read())

print("\n".join([f"Message: {m}" for m in messages]))

time = sys.argv[1]

try:
    time = int(time)
except Exception as err:
    print(f"Exception in {sys.argv[0]}:\n{err}")
    sys.exit()

for i in range(time):
    image_path = os.path.join(os.getcwd(), "images", random.choice(os.listdir("images")))
    message = textwrap.wrap(random.choice(messages), width=15)

    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("font.ttf", 100)

    current_h, pad = image.height/4, 20
    
    for line in message:
        w, h = draw.textsize(line, font=font)
        draw.text(((image.width - w)/2, current_h), line, fill=(random.randint(0, 100), random.randint(100, 255), random.randint(100, 255)), font=font)
        current_h += h + pad

    image.save(f"finisheds/{''.join([str(random.randint(0, 9)) for i in range(9)])}.png")

    print(f"%{round(i/time*100, 2)}")


print(f"Fihished ({time}) images.")