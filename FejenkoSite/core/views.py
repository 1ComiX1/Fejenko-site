import telebot

from django.shortcuts import render, redirect
from django.http import HttpResponse

from datetime import datetime as dt

from .components.forms.FeedbackForm import FeedbackForm
from .models import FeedbackModel
from .scripts import scripts

# telebot settings
bot = telebot.TeleBot("5753443599:AAH1PcN3hGdvzF4oSeuPnsorZXzFOpF_d-M", parse_mode=None)
owner_id = "226372957"

# View of index page
def index(request):
    print(f"[+]{scripts.format_time()} Rendering 'Index' page...")
    return render(request, 'index.html')

# View of Services page
def services(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        print(f"[+]{scripts.format_time()} Received POST method. Starting form processing...")

        if form.is_valid():
            post = form.save(commit='False')

            print(f"[+]{scripts.format_time()} Form is valid!")

            if 'checkbox' in dict(request.POST):
                checkboxes = dict(request.POST)['checkbox']

                print(f"[+]{scripts.format_time()} Checkboxes that was selected: {checkboxes}")
                checkboxes = scripts.idx_to_bool(checkboxes)

                post.logo = checkboxes[0]
                post.presentation = checkboxes[1]
                post.social_networks = checkboxes[2]
                post.identity = checkboxes[3]
                post.infographics = checkboxes[4]
                post.offline_adds = checkboxes[5]

            post.save()

            send_data(FeedbackModel.objects.last().client_id)

            print(f"[+]{scripts.format_time()} Form's data was saved to the database!")
        else:
            print(f"[+]{scripts.format_time()} Form isn't valid!")

        print(f"[+]{scripts.format_time()} Rendering services page...")
        return render(request, 'services.html', {})
    else:
        print(f"[+]{scripts.format_time()} Received GET method. Starting rendering services page...")
        form = FeedbackForm()
        return render(request, 'services.html', {'core': form})

# View of About Me page
def aboutme(request):
    print(f"[+]{scripts.format_time()} Rendering 'About Me' page...")
    return render(request, 'aboutme.html')

# View of Confidentiality page
def confidentiality(request):
    print(f"[+]{scripts.format_time()} Rendering 'Confidentiality' page...")
    return render(request, 'confidentiality.html')

# View of Portfolio page
def portfolio(request):
    print(f"[+]{scripts.format_time()} Rendering 'Portfolio' page...")
    return render(request, 'portfolio.html')

# View of 400-error page
def error_403(request, exception):
    print(f"[+]{scripts.format_time()} Caught 403 Error. Rendering appropriate page...")
    return render(request, '400.html', status=403)

# View of 404-error page
def error_404(request, exception):
    print(f"[+]{scripts.format_time()} Caught 404 Error. Rendering appropriate page...")
    return render(request, '404.html', status=404)


def error_502(request, exception):
    print(f"[+]{scripts.format_time()} Caught 502 Error. Rendering appropriate page...")
    return render(request, '502.html', status=502)


def error_503(request, exception):
    print(f"[+]{scripts.format_time()} Caught 503 Error. Rendering appropriate page...")
    return render(request, '503.html', status=503)


def error_504(request, exception):
    print(f"[+]{scripts.format_time()} Caught 504 Error. Rendering appropriate page...")
    return render(request, '504.html', status=504)


# ----------------------------------------------------------------
# Telebot functions
def format_data(data: FeedbackModel):
    formated_data = f"Заказ номер: {data.client_id}\n" \
                    f"Имя клиента: {data.client_name}\n" \
                    f"Запрошенные услуги: {checkboxes_to_str(data)}\n" \
                    f"Описание задания:\n" \
                    f"{data.task_brief}\n" \
                    f"Время заказа: {data.task_timestamp}\n"

    return formated_data

def checkboxes_to_str(data: FeedbackModel):
    checkboxes = [data.logo,
                  data.presentation,
                  data.social_networks,
                  data.identity,
                  data.infographics,
                  data.offline_adds]

    result = ""
    if checkboxes[0]:
        result += "Логотип, "
    if checkboxes[1]:
        result += "Презентация, "
    if checkboxes[2]:
        result += "Социальные сети, "
    if checkboxes[3]:
        result += "Айдентика, "
    if checkboxes[4]:
        result += "Инфографика, "
    if checkboxes[5]:
        result += "Реклама, "

    result = result[:-2]

    return result

def send_data(data_pk):
    data = FeedbackModel.objects.get(client_id=data_pk)
    bot.send_message(owner_id, format_data(data))