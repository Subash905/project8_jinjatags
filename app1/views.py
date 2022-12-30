from django.shortcuts import render

# Create your views here.
def jinjaprint(request):
    d={'name':'Subash', 'age':25}


    return render(request,'jinjaprint.html',context=d)