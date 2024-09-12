from django.shortcuts import redirect, render
from .models import Product , Commande
#from django.core.paginator import Paginator

# Create your views here.

def index(request):
    Product_object = Product.objects.all()
    item_name= request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        #categories_object = Category.objects.filter(
        Product_object = Product.objects.filter(title__icontains=item_name)
        Product_object = Product.objects.filter(description__icontains=item_name)

  #  paginator = Paginator(Product_object , 4 )
   # page = request.GET.get('page')
   # Product_object = paginator.get_page(page)
    return render (request,'shop/index.html' , {'Product_object' : Product_object})

def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items')
        total = request.POST.get('total')
        Nom = request.POST.get('Nom')
        Telephone = request.POST.get('Telephone')
        Address = request.POST.get('Address')
        Quartier = request.POST.get('Quartier')
        Regions = request.POST.get('Regions')
        zipcode = request.POST.get('zipcode')
        com = Commande(items=items, total=total , Nom=Nom, Telephone=Telephone, Address=Address,Quartier=Quartier , Regions=Regions, zipcode=zipcode)
        com.save()
        return redirect('confirmation')
    

    return render(request,'shop/checkout.html')


def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info :
        nom = item.Nom
    return render(request, 'shop/confirmation.html', {'name':nom})





#pour le site ecommerce il a fait une fonction detail dont on a pas besoin pour notre site 
#voir  a 1:42minutes mais cette fonction sera utile pour d'autres proget
