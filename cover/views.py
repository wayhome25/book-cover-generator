from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from cover.forms import CoverForm
from cover.utils import COLOR_CODE


def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CoverForm()
    return render(request, 'cover/index.html', {'form': form})

def image_generator(request):
    title = request.GET['title']
    top_text = request.GET['top_text']
    author = request.GET['author']
    animal_code = request.GET['animal_code']
    color_index = request.GET['color_code']
    guide_text = request.GET['guide_text']
    guide_text_placement = request.GET['guide_text_placement']

    animal_path = settings.ROOT('assets', 'animal', '{}.png'.format(animal_code))
    animal_im = Image.open(animal_path)
    animal_im = animal_im.resize((400, 400))

    color = COLOR_CODE[int(color_index)]

    canvas_im = Image.new('RGB', (500, 700), (255, 255, 255, 255))
    canvas_im.paste(animal_im, (50, 40))

    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')  # get a font
    draw = ImageDraw.Draw(canvas_im)  # get a drawing context

    # rectangle_top
    draw.rectangle([20, 0, 480, 10], fill=color)

    # rectangle_middle
    draw.rectangle([20, 400, 480, 510], fill=color)

    # Title
    fnt = ImageFont.truetype(ttf_path, 70)
    draw.text((45, 430), title, font=fnt, fill=(255, 255, 255, 255))

    # Top text
    fnt = ImageFont.truetype(ttf_path, 20)
    draw.text((160, 13), top_text, font=fnt, fill=(0, 0, 0, 255))

    # Author
    fnt = ImageFont.truetype(ttf_path, 25)
    draw.text((360, 655), author, font=fnt, fill=(0, 0, 0, 255))

    # guide_text
    fnt = ImageFont.truetype(ttf_path, 25)
    draw.text((140, 510), guide_text, font=fnt, fill=(0, 0, 0, 255))

    response = HttpResponse(content_type='image/png')
    canvas_im.save(response, format='PNG')
    return response
