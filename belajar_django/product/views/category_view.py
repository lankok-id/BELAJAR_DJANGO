from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Category, CategorySerializer


def category_index(request):
    categories_obj = Category.objects.all()
    serializer = CategorySerializer(categories_obj, many=True)

    return render(request, "category_index.html", {"categories": serializer.data})


def category_create(request):
    if request.method == "POST":
        serializer = CategorySerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Kategori berhasil ditambahkan!")
            return redirect("category_list")
        else:
            readable_errors = ", ".join([f"{k}: {v[0]}" for k, v in serializer.errors.items()])
            messages.error(request, readable_errors)

    return render(request, "category_form.html")


def category_update(request, id):
    category_obj = get_object_or_404(Category, id=id)

    if request.method == "POST":
        serializer = CategorySerializer(instance=category_obj, data=request.POST)

        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Kategori berhasil diperbarui!")
            return redirect("category_list")
        else:
            readable_errors = ", ".join([f"{k}: {v[0]}" for k, v in serializer.errors.items()])
            messages.error(request, readable_errors)

    return render(request, "category_form.html", {"category": category_obj})

def category_delete(request, id):
    category_obj = get_object_or_404(Category, id=id)

    if request.method == "POST":
        category_obj.delete()
        messages.success(request, "Kategori berhasil dihapus!")
        return redirect("category_list")

    return render(request, "category_delete.html", {"category": category_obj})