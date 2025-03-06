# Create your views here.

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, nfactorial school!")


def add(request, first: int, second: int):
    return HttpResponse(str(first + second))


def upper(request, text: str):
    return HttpResponse(text.upper())
