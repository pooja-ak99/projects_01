from django.shortcuts import render
from Shop.models import product
from django.db.models import Q

def search(request):
    q = ""
    Product=None
    if(request.method=="POST"):
        q = request.POST['q']
        if q:
            Product=product.objects.filter(Q(name__icontains=q)|Q(description__icontains=q))
    return render(request, 'search.html', {"pro":Product, "que":q})

