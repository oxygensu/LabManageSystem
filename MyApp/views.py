from django.shortcuts import render

# Create your views here.
def MainWindowPage(request):

    return render(request, "mainPage.html")