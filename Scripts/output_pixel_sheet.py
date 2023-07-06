from PIL import Image
import math

# INPUTS
name = 'white'
basic_input = {
    (255, 0, 0): 300,
    (0, 255, 0): 175,
    (0, 0, 255): 60,
    (0, 150, 150): 150,
    (255, 0, 255): 90
}

image_width = 22
image_height = 0
# END INPUTS

# Create size of new PNG
def newPNG(name, x, y):
    im = Image.new('RGB', (x, y), name)
    return im

def outputWhiteLine(img, width, y):
    for x in range(width):
        img.putpixel((x, y), (255, 255, 255))

def outputPixelSheet(colourDict, height=0, width=22):
    # Calculate height for the image
    rounded_counts = [math.ceil(count / width) * width for count in colourDict.values()]
    image_height = sum(rounded_counts) // width
    image_height += len(colourDict) + 1
    # Create a new image
    image = newPNG(name, width, image_height)

    # Initialize position variables
    x = 0
    y = 0

    # Iterate over the pixel counts and colors
    outputWhiteLine(image, image_width, y)
    y += 1
    for color, count in colourDict.items():
        rounded_count = math.ceil(count / image_width) * image_width
        for _ in range(rounded_count):
            image.putpixel((x, y), color)
            x += 1
            if x == image_width:
                x = 0
                y += 1
        # Add block of white pixels after each color block
        outputWhiteLine(image, image_width, y)
        y += 1

    # Save the image
    image.save('output.png')

# Call the function
outputPixelSheet(basic_input, image_height, image_width)
