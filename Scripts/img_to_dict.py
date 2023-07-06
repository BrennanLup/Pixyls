from PIL import Image

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

# Open the image
# pixyl_images/pixyl_windows.jpeg
# frog.jpg
image = Image.open("flowers.png")

# Count the number of colors
num_colors = count_colors(image)
 
for pixel, count in num_colors.items():
    print(f"Color: {pixel}, Count: {count}")

