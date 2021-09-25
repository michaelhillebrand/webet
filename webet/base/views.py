# import os
from pathlib import Path
from django.shortcuts import render

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# def index(request):
#     return render(request,  os.path.join(BASE_DIR, 'frontend', "build", "index.html"))


def index(request):
    return render(request, "index.html")
