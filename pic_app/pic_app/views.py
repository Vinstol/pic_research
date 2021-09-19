from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from PIL import Image

from pic_app.forms import Picture_colourForm

from pic_app.models import Picture_colour


def get_new_picture(request):
    """Function, generating page with form for Picture_colour Model filling."""

    form = Picture_colourForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        picture = form.save()
        return redirect('result', picture.id)
    return render(request, 'form_page.html', {'form': form})


def result(request, picture_id):
    """Function, generating page with results of image research.
    Function provide template with:
    1. Image object;
    2. Text conclusion of majority of black or white pixels on image;
    3. HEX code for chosen colour;
    4. Pixels amount for chosen RGB colour."""

    picture = get_object_or_404(Picture_colour, pk=picture_id)
    picture_item = picture.image
    picture.b_w_trigger = count_black_white_pixels(picture_item)
    if picture.b_w_trigger is True:
        b_w_res = 'На изображении больше чёрных пикселей'
    else:
        b_w_res = 'На изображении больше белых пикселей'
    colour_rgb = hex_to_rgb(picture.colour_hex)
    picture.colour_cnt = count_pixels_in_pic(picture.image, colour_rgb)
    picture.save()
    return render(request, 'result.html', {
        'picture': picture,
        'pic': picture.image,
        'b_w_res': b_w_res,
        'colour_hex': picture.colour_hex,
        'col_amount': picture.colour_cnt,
    })


def count_pixels_in_pic(image, colour_rgb):
    """Function-counter of pixels amount for chosen RGB colour."""

    pix = Image.open(image)
    width = pix.width
    height = pix.height
    colour_cnt = 0
    for x in range(width):
        for y in range(height):
            if pix.getpixel((x, y)) == colour_rgb:
                colour_cnt += 1
    return colour_cnt


def count_black_white_pixels(image):
    """Function-counter of black and white pixels in the image.
    Function returns True for black pixels majority and
    False if white pixels get the most part of the image."""

    black = count_pixels_in_pic(image, (0, 0, 0))
    white = count_pixels_in_pic(image, (255, 255, 255))
    if black > white:
        return True
    else:
        return False


def hex_to_rgb(colour_hex):
    """Function-converter HEX colour code to RGB colour code."""

    colour_hex = colour_hex.lstrip('#')
    ln = len(colour_hex)
    return tuple(int(colour_hex[i:i+ln//3], 16) for i in range(0, ln, ln//3))


def rgb_to_hex(colour_rgb):
    """Function-converter RGB colour code to HEX colour code."""

    return '#%02x%02x%02x' % colour_rgb
