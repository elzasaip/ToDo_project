from django.shortcuts import render

def homepage(request):
    return render(request,"index.html")

def test(request):
    return render (request, "test.html")