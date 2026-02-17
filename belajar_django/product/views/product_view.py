from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Product, Category, Status, ProductSerializer


def product_index(request):
    products = Product.objects.select_related("category", "status").filter(
        status__name="bisa dijual"
    )
    return render(request, "product_index.html", {"products": products})


def product_create(request):
    if request.method == "POST":
        serializer = ProductSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Produk berhasil ditambahkan!")
            return redirect("product_list")
        else:
            readable_errors = ", ".join(
                [f"{k}: {v[0]}" for k, v in serializer.errors.items()]
            )
            messages.error(request, readable_errors)

    categories = Category.objects.all()
    statuses = Status.objects.all()
    return render(
        request, "product_form.html", {"categories": categories, "statuses": statuses}
    )


def product_update(request, id):
    product_obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        serializer = ProductSerializer(instance=product_obj, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Produk berhasil diperbarui!")
            return redirect("product_list")
        else:
            readable_errors = ", ".join(
                [f"{k}: {v[0]}" for k, v in serializer.errors.items()]
            )
            messages.error(request, readable_errors)

    categories = Category.objects.all()
    statuses = Status.objects.all()
    return render(
        request,
        "product_form.html",
        {"product": product_obj, "categories": categories, "statuses": statuses},
    )


def product_delete(request, id):
    product_obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product_obj.delete()
        messages.success(request, "Produk berhasil dihapus!")
    return redirect("product_list")
