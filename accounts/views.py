from django.shortcuts import render, redirect, reverse,HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.models import User ,Group
from merchants.models import Merchant
from listings.models import Listing
from django.core.files.storage import FileSystemStorage
from listings.choices import price_choices,state_choices,sublocality_choices,city_choices,category_choices

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now Logged in')
            return redirect('index')
        else:
            messages.error(request, 'Incorrect')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    print(Group.objects.get())
    context = {
        'price_choices':price_choices,
        'state_choices':state_choices,
        'sublocality_choices':sublocality_choices,
        'city_choices':city_choices,
        'category_choices':category_choices
    }
    if request.method=='POST':
        photo = request.FILES['myfile']
        #get form values
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        zipcode = request.POST['zipcode']
        description = request.POST['description']
        group = Group.objects.get(name='merchants')
        print(group)
        print('11')
        is_staff = True
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username taken' )
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email taken' )
                    return redirect('register') 
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,is_staff=is_staff)
                    user.save()
                    if group:
                        user.groups.add(group)
                    m = Merchant(name=first_name,photo=photo,email=email,city=city,state=state,phone=phone,zipcode=zipcode,description=description)
                    m.save()
                    
                    # login after registeration
                    auth.login(request,user)
                    messages.success(request, 'You are logged in')
                    # return redirect('index')
        #             if is_staff:
        #                 m = Merchant(name=username)
        #                 m.save()
        #                 user.groups.add(group)
                    # messages.success(request, 'You are registered. You can now login')
                    # return render('login')
                
        else:    
            messages.error(request, 'invalid info')
            return redirect('register')
        return render(request,'accounts/register.html',context )
    else:
        return render(request, 'accounts/register.html',context)

def logout(request):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    print(request.user.username)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
        else:    
            m = Merchant.objects.get(email=request.user.email)
            print(m)
            l = Listing.objects.filter(merchant__email__iexact=request.user.email)
            context = {
            'merchant':m,
            'listings':l,
            'category_choices':category_choices
            }
        if request.method=='POST':
            photo = request.FILES.get('myfile')
            name = request.POST.get('name')
            category = request.POST.get('category')
            brand=request.POST.get('brand')
            description=request.POST.get('description')
            oldprice=request.POST.get('oldprice')
            newprice=request.POST.get('newprice')
            qty = request.POST.get('qty')
            link = request.POST.get('link')
            if not oldprice:
                oldprice=None
            if not newprice:
                newprice = None
            if not qty:
                qty=None
            
            listing = Listing(merchant=m,name=name,photo=photo,category=category_choices[category],brand=brand,description=description,oldprice=oldprice,newprice=newprice,qty=qty,link=link)
            listing.save()
    else:
        return redirect('login')
    return render(request, 'accounts/dashboard.html',context)