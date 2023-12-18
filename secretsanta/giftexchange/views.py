from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import GiftExchange, Participant


def create_gift_exchange(request):
    if request.method == "POST":
        # handle form submission
        pass
    else:
        # display form
        pass


def list_gift_exchanges(request):
    exchanges = GiftExchange.objects.filter(participant__user=request.user)
    return render(request, "list.html", {"exchanges": exchanges})
