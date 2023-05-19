from django.shortcuts import render, redirect
from main.models import Image, TextIndex, SubImage, CustomUser, productCards, appealFIZ, appealUR, AnimalsSI, TradeSI, PlantsSI, ChillSI, News
from main.forms import CustomUserCreationForm
from main.models import AnimalsText, ChillText, PlantsText, TradeText
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
import json




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



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main/news.html')  # Перенаправление на главную страницу после успешного входа
        else:
            error_message = 'Неправильная комбинация почты и пароля'
            return render(request, 'main/login.html', {'error_message': error_message})
    else:
        return render(request, 'main/login.html')

def news_view(request):
    text_indexes = News.objects.order_by('-id')  # Assuming 'id' represents the date of creation or a relevant field
    return render(request, 'main/news.html',{'text_indexes': text_indexes})

from django.http import JsonResponse

@csrf_exempt
def contacts(request):
    if request.method == "POST":
        data = json.loads(request.body)
        UrFace = data.get("UrFace")
        Fio = data.get("Fio")
        Phone = data.get("Phone")
        address = data.get("address")
        appeal = data.get("appeal")

        if UrFace:
            # Создание и сохранение объекта в модели данных appealUR
            appeal_obj = appealUR.objects.create(
                UrFace=UrFace,
                Fio=Fio,
                Phone=Phone,
                address=address,
                appeal=appeal
            )
        else:
            # Создание и сохранение объекта в модели данных appealFIZ
            appeal_obj = appealFIZ.objects.create(
                Fio=Fio,
                Phone=Phone,
                address=address,
                appeal=appeal
            )

        return JsonResponse({"message": "Success"})
    else:
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


def Plants(request):
    text_indexes = PlantsText.objects.all()
    simg = PlantsSI.objects.all()
    return render(request, 'main/plants.html', {'simg': simg, 'text_indexes': text_indexes})


def Animals(request):
    text_indexes = AnimalsText.objects.all()
    simg = AnimalsSI.objects.all()
    return render(request, 'main/animals.html', {'simg': simg,'text_indexes': text_indexes})


def Trade(request):
    text_indexes = TradeText.objects.all()
    simg = TradeSI.objects.all()
    return render(request, 'main/trade.html', {'simg': simg, 'text_indexes': text_indexes})


def Chill(request):
    text_indexes = ChillText.objects.all()
    simg = ChillSI.objects.all()
    return render(request, 'main/chill.html', {'simg': simg, 'text_indexes': text_indexes})











