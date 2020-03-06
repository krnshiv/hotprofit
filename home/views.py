from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices,state_choices,sublocality_choices,city_choices,category_choices
from listings.models import Listing
from merchants.models import Merchant

def index(request):
    if request.method == 'GET':
        listings = Listing.objects.order_by('-posted').filter(is_valid=True)
        context = {
            'listings':listings,
            'price_choices':price_choices,
            'state_choices':state_choices,
            'sublocality_choices':sublocality_choices,
            'city_choices':city_choices,
            'category_choices':category_choices
        }
        return render(request,"home/index.html",context)

def about(request):
    merchants = Merchant.objects.order_by('-last_active')[:3]
    mvps = Merchant.objects.all().filter(mvp=True)
    context = {
        'merchants':merchants,
        'mvp': mvps
    }
    return render(request,"home/about.html",context)
