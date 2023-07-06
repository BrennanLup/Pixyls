from PIL import Image
import output_pixel_sheet


def count_colors(image):
    width, height = image.size
    colors = {}

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            if pixel in colors:
                colors[pixel] += 1
            else:
                colors[pixel] = 1

    return colors

def outputDict(colorDict):
    for pixel, count in colorDict.items():
        print(f"Color: {pixel}, Count: {count}")
# Open the image
# pixyl_images/pixyl_windows.jpeg
# frog.jpg
image = Image.open("../purp.jpeg")

# Count the number of colors
num_colors = count_colors(image)
outputDict(num_colors)
output_pixel_sheet.outputPixelSheet(num_colors)


