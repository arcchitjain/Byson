from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import DetailView

from .forms import NameForm, ImageForm
from .models import Shop


def index(request):
    return render(request, "shopmaker/index.html")


def tweak_layout(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            image = "shopmaker/oxfam.jpg"
            return render(request, "shopmaker/tweak_layout.html", {'image': image})

    else:
        form = ImageForm()

    return render(request, "shopmaker/tweak_layout.html", {'form': form})


def preview_layout(request):
    image = "shopmaker/oxfam.jpg"
    return render(request, "shopmaker/preview_layout.html", {'image': image})


def image_import(request):
    return render(request, "shopmaker/image_import.html")


def detect(request):
    return render(request, "shopmaker/detect.html")

def detect2(request):
    return render(request, "shopmaker/detect2.html")


def import_products(request):
    return render(request, "shopmaker/import_products.html")


def start(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            shop = Shop(name=form.cleaned_data["shop_name"])
            shop.save()
            return HttpResponseRedirect(f"shopmaker/shop/{shop.id}")

    else:
        form = NameForm()

    return render(request, "shopmaker/start.html", {'form': form})


class ShopDetailView(DetailView):
    model = Shop
