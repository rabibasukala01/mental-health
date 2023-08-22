from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == "POST":
        age = float(request.POST["age"])

        return render(request, "result.html", {})
    return render(request, "home.html", {})
