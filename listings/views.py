from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .choices import price_choices,state_choices,sublocality_choices,city_choices,category_choices
from decimal import Decimal
from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-posted').filter(is_valid=True)
    
    paginator = Paginator(listings,8)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings':paged_listings
    }
    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-posted')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        print(keywords)
        if keywords:
            queryset_list = queryset_list.filter(name__icontains=keywords)
    if 'price' in request.GET:
        price = Decimal(request.GET['price'])
        priceset=[]
        if price:
            for q in queryset_list:
                if q.newprice != None:
                    print(type(q.newprice),type(price))
                    if q.newprice<=price:
                        print(q.newprice,price)
                        priceset.append(q)
            queryset_list=priceset

    if 'city' in request.GET:
        city = request.GET['city']
        city1=city_choices[city]
        cityset=[]
        print(city1)
        if city1:
            for q in queryset_list:
                if q.merchant.city == city1:
                    print(q)
                    cityset.append(q)
                
            queryset_list = cityset

    if 'state' in request.GET:
        state = request.GET['state']
        state1=state_choices[state]
        stateset=[]
        if state1:
            for q in queryset_list:
                if q.merchant.state == state1:
                    stateset.append(q)

            queryset_list = stateset

    if 'sublocality' in request.GET:
        sublocality = request.GET['sublocality']
        print(sublocality)
        sub = sublocality_choices[sublocality]
        subset=[]
        if sub:
            for q in queryset_list:
                if q.merchant.sublocality==sub:
                    subset.append(q)

            queryset_list = subset

    if 'category' in request.GET:
        category = request.GET['category']
        print(category)
        for q in queryset_list:
            print(q.category)
        if category:
            queryset_list = queryset_list.filter(category__iexact=category)

    if 'brand' in request.GET:
        brand = request.GET['brand']
        print(brand)
        if brand:
            queryset_list = queryset_list.filter(brand__icontains=brand)
        

    context = {
        'listings':queryset_list,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'sublocality_choices':sublocality_choices,
        'city_choices':city_choices,
        'category_choices':category_choices
    }
    return render(request, 'listings/search.html',context)