from django.shortcuts import render
from datetime import datetime

blog_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Ankur Halder",
        "date": datetime.now(),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened next.",
        "content": """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        """,
    },
    {
        "slug": "sunset-at-the-beach",
        "image": "beach.jpg",
        "author": "Ankur Halder",
        "date": datetime.now(),
        "title": "Sunset at the Beach",
        "excerpt": "Witness the breathtaking beauty of a sunset at the beach and let your worries drift away.",
        "content": """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        """,
    },
    {
        "slug": "exploring-the-city",
        "image": "city.jpg",
        "author": "Ankur Halder",
        "date": datetime.now(),
        "title": "Exploring the City",
        "excerpt": "Embark on an adventure through the bustling streets and hidden gems of the city.",
        "content": """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        """,
    },
    {
        "slug": "adventures-in-nature",
        "image": "nature.jpg",
        "author": "Ankur Halder",
        "date": datetime.now(),
        "title": "Adventures in Nature",
        "excerpt": "Immerse yourself in the wonders of nature and discover the magic that awaits.",
        "content": """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        """,
    },
]


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_post = sorted(blog_posts, key=get_date)
    latest_post = sorted_post[-3:] if sorted_post else []
    return render(request, "app/index.html", {"posts": latest_post})


def posts(request):
    return render(request, "app/all-posts.html")


def post_details(request, slug):
    return render(request, "app/post-detail.html")
