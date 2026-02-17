from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Category, CategorySerializer


def category_index(request):
    categories = Category.objects.all()
    return render(request, "category_index.html", {"categories": categories})


def category_create(request):
    if request.method == "POST":
        serializer = CategorySerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Kategori berhasil ditambahkan!")
            return redirect("category_list")
        else:
            messages.error(request, serializer.errors)

    return render(request, "category_form.html")


def category_update(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        serializer = CategorySerializer(
            instance=category,
            data=request.POST
        )

        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Kategori berhasil diperbarui!")
            return redirect("category_list")
        else:
            messages.error(request, serializer.errors)

    return render(request, "category_form.html", {"category": category})


def category_delete(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        category.delete()
        messages.success(request, "Kategori berhasil dihapus!")
        return redirect("category_list")

    return render(request, "category_delete.html", {"category": category})
