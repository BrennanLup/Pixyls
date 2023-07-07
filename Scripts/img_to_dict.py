from PIL import Image
import output_pixel_sheet


def dither_image(image, num_colors):
    # Convert the image to a specific mode with the desired number of colors
    image = image.convert("P", palette=Image.Palette.ADAPTIVE, colors=num_colors)
    # Apply dithering
    dithered_image = image.convert("RGB", dither=Image.Dither.FLOYDSTEINBERG)
    
    # Display the dithered image
    return dithered_image

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
image = Image.open("../purp.png")
image = dither_image(image, 30)
image.show()

# Count the number of colors
num_colors = count_colors(image)
outputDict(num_colors)
output_pixel_sheet.outputPixelSheet(num_colors)


