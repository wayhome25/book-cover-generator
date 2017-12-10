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
    animal_im = animal_im.resize((300, 300))

    color = COLOR_CODE[int(color_index)]

    canvas_im = Image.new('RGB', (500, 700), color)
    canvas_im.paste(animal_im, (0, 0))

    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')  # get a font
    d = ImageDraw.Draw(canvas_im)  # get a drawing context

    fnt = ImageFont.truetype(ttf_path, 40)
    d.text((10, 10), title, font=fnt, fill=(0, 255, 0, 255))

    fnt = ImageFont.truetype(ttf_path, 20)
    d.text((10, 60), top_text, font=fnt, fill=(0, 255, 0, 255))

    fnt = ImageFont.truetype(ttf_path, 10)
    d.text((10, 110), author, font=fnt, fill=(0, 255, 0, 255))

    fnt = ImageFont.truetype(ttf_path, 10)
    d.text((10, 130), guide_text, font=fnt, fill=(0, 255, 0, 255))

    response = HttpResponse(content_type='image/png')
    canvas_im.save(response, format='PNG')
    return response
