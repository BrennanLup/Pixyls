from PIL import Image

def count_colors(image):
    width, height = image.size
    colors = set()

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            colors.add(pixel)

    return len(colors)


def round_color(color, precision):
    if precision == 0:
        return color
    else:
        return tuple(int(round(channel / precision) * precision) for channel in color)

def count_colors_rounded(image, tolerance=0):
    width, height = image.size
    pixel_count = {}


    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            pixel = round_color(pixel, tolerance)
            if pixel in pixel_count:
                pixel_count[pixel] += 1
            else:
                pixel_count[pixel] = 1
    return pixel_count

# Open the image
image = Image.open("pixyl_images/pixyl_windows.jpeg")

tolerance = 50
# Count the number of colors
num_colors = count_colors_rounded(image, tolerance)

for pixel, count in num_colors.items():
    print(f"Color: {pixel}, Count: {count}")