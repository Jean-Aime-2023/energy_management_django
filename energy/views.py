from django.shortcuts import render

# landing page
def home(request):
    return render(request,'landing.html')


