from django.shortcuts import render, redirect, get_object_or_404
from .models import Seller


def create_seller(request):
    if request.method == "GET":
        return render(request, "create_seller.html")
    else:
        seller = Seller(name=request.POST['name'],
                        email=request.POST['email'],
                        phone_number=request.POST['phonenumber'],
                        dt_entrance=request.POST['dt_entrance'])
        seller.save()
        return render(request, "create_seller.html", {"message": f"Seller {request.POST['name']} added."})


def sellers_list(request):
    sellers = Seller.objects.all()
    return render(request, "seller_list.html", {"sellers": sellers})


def seller(request, id):
    seller = get_object_or_404(Seller, id_code=id)
    return render(request, "seller.html", {"seller": seller})


def update_seller(request, id_code):
    if request.method == "POST":

        """
        # Just another option to update data, but i think 'get_object_or_404() is better to use.'
        seller = Seller.objects.filter(id_code=id_code)
        seller.update(name=request.POST["name"],
                      email=request.POST['email'],
                      phone_number=request.POST['phonenumber'],
                      dt_entrance=request.POST['dt_entrance'])
        """

        seller = get_object_or_404(Seller, id_code=id_code)
        seller.name = request.POST['name']
        seller.email = request.POST['email']
        seller.phone_number = request.POST['phonenumber']
        seller.dt_entrance = request.POST['dt_entrance']
        seller.save()
        return render(request, "seller.html", {"seller": seller, "message": "Data updated"})


def delete_seller(request, id_code):
    if request.method == "POST":
        seller = get_object_or_404(Seller, id_code=id_code)
        seller.delete()
    return redirect("sellers_list")
