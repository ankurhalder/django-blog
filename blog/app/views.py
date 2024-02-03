from django.shortcuts import render


def starting_page(request):
    return render(request, "app/index.html")


def posts(request):
    return render(request, "app/all-posts.html")


def post_details(request):
    pass
