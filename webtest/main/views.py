from django.shortcuts import render
from .models import Image, TextIndex,SubImage


def index(request):
    img = Image.objects.all()
    simg = SubImage.objects.all()
    text_indexes = TextIndex.objects.all()
    return render(request, 'main/index.html', {'img': img, 'text_indexes': text_indexes,'simg' : simg})


def product(request):
    return render(request, 'main/product.html')


def image_list(request):
    img = Image.objects.all()
    print(img)
    text_index = TextIndex.objects.first()
    context = {'big_text': text_index.big_text}
    return render(request, 'main/index.html', {'img': img, 'big_text': text_index.big_text})


