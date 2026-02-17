from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Status


def status_index(request):
    statuses = Status.objects.all()
    return render(request, "status_index.html", {"statuses": statuses})


def status_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Status.objects.create(name=name)
        messages.success(request, "Status berhasil ditambahkan")
        return redirect("status_list")

    return render(request, "status_form.html")


def status_update(request, id):
    status = get_object_or_404(Status, id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        status.name = name
        status.save()
        messages.success(request, "Status berhasil diupdate")
        return redirect("status_list")

    return render(request, "status_form.html", {"status": status})


def status_delete(request, id):
    status = get_object_or_404(Status, id=id)
    if request.method == "POST":
        status.delete()
    messages.success(request, "Status berhasil dihapus")
    return redirect("status_list")
