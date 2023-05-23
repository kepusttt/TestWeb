from django.shortcuts import render, redirect
from main.models import Image, TextIndex, SubImage, CustomUser, productCards, appealFIZ, appealUR, AnimalsSI, TradeSI, PlantsSI, ChillSI, News
from main.forms import CustomUserCreationForm
from main.models import AnimalsText, ChillText, PlantsText, TradeText, PlantsCard, ProductOrderUr, ProductOrderFiz, AnimalsCard
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
import json
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from django.db.models import Q




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
    search_query = request.GET.get('search_query', '')
    sort_order = request.GET.get('sort_order', '-id')  # Добавлен параметр сортировки

    text_indexes = News.objects.order_by(sort_order)

    if search_query:
        text_indexes = text_indexes.filter(
            Q(title__icontains=search_query) |
            Q(big_text__icontains=search_query) |
            Q(created_at__icontains=search_query)
        )

    context = {
        'text_indexes': text_indexes,
        'search_query': search_query,
        'sort_order': sort_order,  # Передача параметра сортировки в контекст
    }

    return render(request, 'main/news.html', context)



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
    cards = PlantsCard.objects.all()
    return render(request, 'main/plants.html', {'simg': simg, 'text_indexes': text_indexes, 'cards': cards})




def Animals(request):
    text_indexes = AnimalsText.objects.all()
    simg = AnimalsSI.objects.all()
    cards = AnimalsCard.objects.all()
    return render(request, 'main/animals.html', {'simg': simg,'text_indexes': text_indexes, 'cards': cards})


def Trade(request):
    text_indexes = TradeText.objects.all()
    simg = TradeSI.objects.all()
    return render(request, 'main/trade.html', {'simg': simg, 'text_indexes': text_indexes})


def Chill(request):
    text_indexes = ChillText.objects.all()
    simg = ChillSI.objects.all()
    return render(request, 'main/chill.html', {'simg': simg, 'text_indexes': text_indexes})




@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        product = request.POST.get('productfiz')
        fio = request.POST.get('fiofiz')
        phone = request.POST.get('phonefiz')
        address = request.POST.get('addressfiz')
        colvo = request.POST.get('colvo')

        order = ProductOrderFiz.objects.create(
            product=product,
            FIO=fio,
            Phone=phone,
            Address=address,
            Colvo=colvo
        )

        # Отправка уведомления на почту всем пользователям с правами superuser
        subject = 'Новый заказ'
        # message = f''
        message = f'Вам поступил новый заказ! Проверьте таблицу "Заказы Физ. Лиц"\n\n' \
                  f'Продукт: {product}\n' \
                  f'ФИО: {fio}\n' \
                  f'Телефон: {phone}\n' \
                  f'Адрес: {address}\n' \
                  f'Количество: {colvo}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = User.objects.filter(is_superuser=True).values_list('email', flat=True)
        send_mail(subject, message, from_email, recipient_list)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@csrf_exempt
def create_order_ur(request):
    if request.method == 'POST':
        product = request.POST.get('productur')
        ur_face = request.POST.get('urfacei')
        fio_ruk = request.POST.get('fioruki')
        phone = request.POST.get('phoneuri')
        ur_address = request.POST.get('addressuri')
        colvo = request.POST.get('colvouri')

        order = ProductOrderUr.objects.create(
            product=product,
            UrFace=ur_face,
            FioRuk=fio_ruk,
            Phone=phone,
            UrAddress=ur_address,
            Colvo=colvo
        )

        # Отправка уведомления на почту всем пользователям с правами superuser
        subject = 'Новый заказ'
        # message = f'Продукт: {product}\nФИО: {fio}\nТелефон: {phone}\nАдрес: {address}\nКоличество: {colvo}'
        message = f'Вам поступил новый заказ! Проверьте таблицу "Заказы Юр. Лиц"\n\n' \
                  f'Продукт: {product}\n' \
                  f'Юр. Лицо: {ur_face}\n' \
                  f'ФИО Руководителя: {fio_ruk}\n' \
                  f'Телефон: {phone}\n' \
                  f'Юр. Адрес: {ur_address}\n' \
                  f'Количество: {colvo}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = User.objects.filter(is_superuser=True).values_list('email', flat=True)
        send_mail(subject, message, from_email, recipient_list)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

def card_detail(request, card_id):
    card = get_object_or_404(PlantsCard, pk=card_id)
    return render(request, 'main/card_detail.html', {'card': card})


def animal_card(request, card_id):
    card = get_object_or_404(AnimalsCard, pk=card_id)
    return render(request, 'main/card_detail.html', {'card': card})






