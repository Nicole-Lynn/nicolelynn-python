import sys
import os
from PIL import Image, ImageOps


# If the user does not specify exactly two command-line arguments, sys.exit
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# If input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively, sys.exit
if os.path.splitext(sys.argv[1])[1].lower() not in [".jpg", ".png", ".jpeg"]:
    sys.exit("Invalid input")
elif os.path.splitext(sys.argv[2])[1].lower() not in [".jpg", ".png", ".jpeg"]:
    sys.exit("Invalid output")

# If input’s name does not have the same extension as the output’s name, sys.exit
input_ext = os.path.splitext(sys.argv[1])[1]
output_ext = os.path.splitext(sys.argv[2])[1]
if input_ext != output_ext:
    sys.exit("Input and output have different extensions")


shirt = Image.open("shirt.png")
size = shirt.size

try:
    # Open the input
    with Image.open(sys.argv[1]) as photo:
        # resize and crop the input using default values for method, bleed, and centering
        # overlay the shirt
        # save the result
        resizePhoto = ImageOps.fit(photo, size)
        resizePhoto.paste(shirt, mask=shirt)
        resizePhoto.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
