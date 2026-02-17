from django.shortcuts import render

# Create your views here.
def root_index(request):
    return render(request, "root_index.html")