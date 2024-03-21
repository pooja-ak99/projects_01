from ServiceApp.models import Category

def cat_link(request):
    c = Category.objects.all()
    return {'catlink':c}