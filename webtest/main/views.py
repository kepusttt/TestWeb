from django.shortcuts import render, redirect
from main.models import Image, TextIndex, SubImage, CustomUser, productCards
from main.forms import CustomUserCreationForm



def index(request):
    img = Image.objects.all()
    simg = SubImage.objects.all()
    text_indexes = TextIndex.objects.all()
    return render(request, 'main/index.html', {'img': img, 'text_indexes': text_indexes,'simg' : simg})


def product(request):
    products = productCards.objects.all()  # Получаем первый объект ProductCards (может быть изменено в соответствии с вашей логикой)
    context = {
        'products': products
    }
    return render(request, 'main/product.html', context)



def login(request):
    return render(request, 'main/login.html')

def account(request):
    return render(request, 'main/account.html')

def contacts(request):
    return render(request, 'main/contacts.html')


def image_list(request):
    img = Image.objects.all()
    print(img)
    text_index = TextIndex.objects.first()
    context = {'big_text': text_index.big_text}
    return render(request, 'main/index.html', {'img': img, 'big_text': text_index.big_text})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password1')
            CustomUser.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})











