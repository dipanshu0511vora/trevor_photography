from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def gallery_single(request):
    return render(request, 'gallery-single.html')

def gallery(request):
    return render(request, 'gallery.html', {'range': range(1,17)})

def services(request):
    return render(request, 'services.html')