from . import views
from django.urls import path

app_name = "trevor"

urlpatterns =[
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('gallery-single/',views.gallery_single,name="gallery-single"),
    path('gallery/',views.gallery,name="gallery"),
    path('services/',views.services,name="services"),
]