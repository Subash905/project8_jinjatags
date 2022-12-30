from django.shortcuts import render

# Create your views here.
def jinja2(request):
    d={'branch':'marathahalli'}

    return render(request,'jinja2.html',d)
    