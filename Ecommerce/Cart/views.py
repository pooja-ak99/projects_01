from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Shop.models import product
from Cart.models import cart,Account,Order
from django.http import HttpResponse
from django.contrib import messages


def cartview(request):
    total = 0
    u = request.user
    try:
        Cart = cart.objects.filter(user=u)
        for i in Cart:
            total += (i.quantity*i.Product.price)
    except:
        pass
    return render(request,'cart.html',{'c':Cart, 'total':total})


@login_required()
def add_to_cart(request,p):
    products = product.objects.get(name=p)
    u = request.user
    try:
        carts = cart.objects.get(user=u,Product=products)
        if (carts.quantity < carts.Product.stock):
            carts.quantity+=1
        carts.save()
    except:
        carts=cart.objects.create(Product=products,user=u,quantity=1)
        carts.save()
    # return render(request, 'cart.html')
    return redirect('Cart:cartview')

@login_required()
def remove(request,p):
    products = product.objects.get(name=p)
    u = request.user
    try:
        carts = cart.objects.get(user=u, Product=products)
        if carts.quantity>1:
            carts.quantity -= 1
            carts.save()
        else:
            carts.delete()
    except:
        pass
    return redirect('Cart:cartview')

@login_required()
def delete(request,p):
    products = product.objects.get(name=p)
    u = request.user
    carts = cart.objects.filter(user=u, Product=products)
    carts.delete()
    return redirect('Cart:cartview')


def orderform(request):
    if request.method=="POST":
        a = request.POST["a"]
        p = request.POST["p"]
        n = request.POST["n"]
        u = request.user
        Cart = cart.objects.filter(user=u)

        #total amount
        total = 0
        for i in Cart:
            total += (i.quantity * i.Product.price)

        #chack whether user has sufficient amount in account
        ac = Account.objects.get(accnum=n)
        if ac.amount > total:
            ac.amount = ac.amount-total
            ac.save()

            for i in Cart:
                o = Order.objects.create(user=u,Product=i.Product,address=a,phone=p,no_of_items=i.quantity,order_status="paid")
                o.save()
                i.Product.stock=i.Product.stock-i.quantity #to decrease the stock
                i.Product.save()

            Cart.delete() #clears the cart after placing order
            msg="Order placed successfully"
            return render(request, 'orderdetail.html', {"m":msg})

        else:
            msg="Insufficient balance in your account.Cannot place order."
            return render(request, 'orderdetail.html', {"m": msg})

    return render(request, 'orderform.html')


def orderview(request):
    u = request.user
    o = Order.objects.filter(user=u)
    return render(request, 'orderview.html', {"or":o})

