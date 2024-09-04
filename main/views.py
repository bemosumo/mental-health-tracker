from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275582',
        'name': 'Muhammad Fawwaz Edsa Fatin Setiawan',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)