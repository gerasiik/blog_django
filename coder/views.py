from django.shortcuts import render



# Create your views here.
def coder(request):
    return render(request, "coder/coder.html")


