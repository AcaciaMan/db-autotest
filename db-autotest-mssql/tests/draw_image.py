from PIL import Image, ImageDraw, ImageFont

# Create a blank image with the desired dimensions
width = 1280
height = 640
image = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Set the font and size
font = ImageFont.truetype("arial.ttf", 200)
large_font = ImageFont.truetype("arial.ttf", 400)

# Draw the characters on the image
text = " DB"
large_text = "T   "
# text_width = draw.textlength(text, font=font)
# text_height = draw.te
# x = (width - text_width) // 2
# y = (height - text_height) // 2
# draw.text((x, y), text, font=font, fill=(0, 0, 0))
draw.text((width//2, height-200), text, anchor='ms', fill="black", font=font)
draw.text((width//2, height-200), large_text, anchor='ms', fill="green", font=large_font)

# Save the image
image.save("C:/work/GitHub/db-autotest-vscode/src/social_preview.png")