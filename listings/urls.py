from django.urls import path

from . import views

urlpatterns = [

    path('',views.index , name='listings'),
    path('<int:listing_id>',views.listing , name='listing'),
    path('update_listing/<int:listing_id>',views.update_listing , name='update_listing'),
    path('delete/<int:listing_id>',views.delete , name='delete'),
    path('search', views.search , name='search')

]