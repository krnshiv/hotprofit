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
    print(request.GET)
    queryset_list = Listing.objects.order_by('-posted')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        print(keywords)
        if keywords:
            queryset_list = queryset_list.filter(name__icontains=keywords).distinct()

    print(queryset_list)

    if 'city' in request.GET:
        city = request.GET['city']
        print(city)
        cityset=[]
        for q in queryset_list:
            if q.merchant.city == city:
                cityset.append(q)
        if cityset:            
            queryset_list = cityset

    print(queryset_list)

    if 'state' in request.GET:
        state = request.GET['state']
        print(state)
        stateset=[]
        for q in queryset_list:
            if q.merchant.state == state:
                stateset.append(q)
        if stateset:        
            queryset_list = stateset

    print(queryset_list)
    if 'sublocality' in request.GET:
        sublocality = request.GET['sublocality']
        print(sublocality)
        sub = sublocality_choices[sublocality]
        subset=[]
        if sub:
            for q in queryset_list:
                print(q.merchant.sublocality,sub)
                if q.merchant.sublocality==sublocality:
                    subset.append(q)
            if subset:
                queryset_list = subset

    print(queryset_list)
    if 'category' in request.GET:
        category = request.GET['category']
        catset=[]
        for q in queryset_list:
            print(q,q.category)
            if q.category==category:
                catset.append(q)
        if catset:
            queryset_list = catset
    
    print(queryset_list)

    if 'brand' in request.GET:
        print('k')
        brand = request.GET['brand']
        print(brand)
        braset=[]
        for q in queryset_list:
            if q.brand==brand:
                braset.append(q)
        if braset:        
            queryset_list = braset
        
    print(queryset_list)

    if 'price' in request.GET:
        price = Decimal(request.GET['price'])
        print(price)
        priceset=[]
        if price:
            for q in queryset_list:
                if q.newprice != None:
                    if q.newprice<=price:
                        print(q.newprice,price)
                        priceset.append(q)
            queryset_list=priceset
            
    print(queryset_list)
    
    context = {
        'listings':queryset_list,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'sublocality_choices':sublocality_choices,
        'city_choices':city_choices,
        'category_choices':category_choices
    }
    return render(request, 'listings/search.html',context)