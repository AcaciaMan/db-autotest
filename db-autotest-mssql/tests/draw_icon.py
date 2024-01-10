from PIL import Image, ImageDraw, ImageFont

# Create a blank image with the desired dimensions
width = 24
height = 24
image = Image.new("RGB", (width, height), (67, 60, 59, 44))
draw = ImageDraw.Draw(image)

# Set the font and size
font = ImageFont.truetype("arial.ttf", 8)
large_font = ImageFont.truetype("arial.ttf", 16)

# Draw the characters on the image
text = "  DB"
large_text = "T   "
# text_width = draw.textlength(text, font=font)
# text_height = draw.te
# x = (width - text_width) // 2
# y = (height - text_height) // 2
# draw.text((x, y), text, font=font, fill=(0, 0, 0))
draw.text((width//2, height-8), text, anchor='ms', fill="gray", font=font)
draw.text((width//2, height-8), large_text, anchor='ms', fill="green", font=large_font)

# Save the image
image.save("C:/work/GitHub/db-autotest-vscode/src/activity_icon.png")