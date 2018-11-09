from PIL import Image

def crop_image(image,ratio):

    img = Image.open(image.path)

    # get the original dimensions
    img_width = img.width
    img_height = img.height

    # the original image ratio
    img_ratio = img_width/img_height

    # img_ratio greater than ratio means longer img width
    # we keep the original height and crop the width
    if img_ratio > ratio:
        # adjusted width
        new_width = ratio * img_height
        # new crop center
        x = (img_width - new_width)/2
        cropped_image = img.crop((x,0,new_width+x, img_height))

        # save after cropping
        cropped_image.save(image.path)

    # else if the img_ratio is less; it means the height is longer
    elif img_ratio < ratio:
        # adjusted img_height
        new_height = img_width/ratio
        # new crop center on y axis
        y = (img_height - new_height) / 2
        cropped_image = img.crop((0, y, img_width, new_height + y))

        # save image
        cropped_image.save(image.path)
