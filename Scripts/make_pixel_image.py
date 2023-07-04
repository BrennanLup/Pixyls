from PIL import Image
#PIL - is the Pillow module

def output_pixel_image():
    img = Image.open("images/lilac1.png")
    smallerImage = img.resize((64,64), Image.Resampling.BILINEAR)
    finalImage = smallerImage.resize(img.size, Image.Resampling.NEAREST)
    finalImage.save('pixyl_images/pixyl_lilac1.png')

def limit_img_colour():
    img = Image.open("pixyl_images/pixyl_lilac1.png")
    img = img.convert('RGB')
    lim_col_img = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=40)
    lim_col_img.save("lim_col_images/lim_col_lilac1.png")




def resize_pixels():
    img = Image.open("images/lilac1.png")
    current_width_px, current_height_px = img.size
    target_width_px = int((current_width_px * pixel_width_mm) / 3.5)
    target_height_px = int((current_height_px * pixel_height_mm) / 3.5)
     # Resize the image using the calculated size
    resized_image = image.resize((target_width_px, target_height_px))
    resized_image.save("pixyl_images/pixyl_lilac1.png")
