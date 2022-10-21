from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first(request):
    print("thakkudu reached")
    if request.method == "POST":
        print("Thakkudu found")
    return render(request, "home.html")

def second(request):

    return render(request, "second.html")
