from PIL import Image

from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from cover.forms import CoverForm


def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('cover:index')
    else:
        form = CoverForm()
    return render(request, 'cover/index.html', {'form': form})

def image_generator(request):
    im = Image.new('RGB', (256, 256), 'yellow')
    response = HttpResponse(content_type='image/jpeg')
    im.save(response, format='JPEG')
    return response
