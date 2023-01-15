from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import *
from logging import exception
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductView(View):
				def get(self, request):

					topwear = Product.objects.filter(category='TW')
					

					bottomwear = Product.objects.filter(category='BW')
			

					shoes = Product.objects.filter(category='SH')
					watch = Product.objects.filter(category='W')
	

					return render(request, 'app/home.html', {'topwear': topwear, 'bottomwear': bottomwear, 'shoes': shoes,'watch':watch})


class ProductDetailView(View):
  def get(self, request, pk):
    product = Product.objects.get(pk=pk)
 

    item_already_in_cart = False
    if request.user.is_authenticated:
          item_already_in_cart = Cart.objects.filter(
              Q(product=product.id) & Q(user=request.user)).exists()

    return render(request, 'app/productdetail.html', {'product': product,'item_already_in_cart': item_already_in_cart})


@login_required
def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod.id')
 size_id = request.GET.get('size.id')
 if size_id == None:
  size_id = "watch"
 print(size_id)
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product, Size=size_id).save()
 return redirect('/cart/')


@login_required
def show_cart(request):
  if request.user.is_authenticated:
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    
    if cart_product:
         for p in cart_product:
           tempamount = (p.quantity * p.product.discount_price)
           amount += tempamount
           totalamount = amount+shipping_amount
         return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})
    else:
      return render(request, 'app/emptycart.html')


@login_required
def plus_cart(request):
  if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0

        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
               tempamount = (p.quantity * p.product.discount_price)
               amount += tempamount
               totalamount = amount+shipping_amount
        data = {
                 'quantity': c.quantity,
                 'amount': amount,
                 'totalamount': totalamount
                              }
        return JsonResponse(data)


@login_required
def minus_cart(request):
      if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if c.quantity != 1:
          
          c.quantity -= 1
          c.save()
          amount = 0.0
          shipping_amount = 70.0
          total_amount = 0.0
          cart_product = [p for p in Cart.objects.all() if p.user == user]
          for p in cart_product:
               tempamount = (p.quantity * p.product.discount_price)
               amount += tempamount
               totalamount = amount+shipping_amount
          data = {
                 'quantity': c.quantity,
                 'amount': amount,
                 'totalamount': totalamount
                              }
        return JsonResponse(data)


@login_required
def remove_cart(request):
      if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
               tempamount = (p.quantity * p.product.discount_price)
               amount += tempamount
               totalamount = amount+shipping_amount
        data = {

                 'amount': amount,
                 'totalamount': totalamount
                              }
        return JsonResponse(data)


@login_required
def buy_now(request):
 user = request.user
 product_id = request.GET.get('prod.id')
 size_id = request.GET.get('size.id')
 product = Product.objects.get(id=product_id)


 Cart(user=user, product=product, Size=size_id).save()
 return redirect('/cart/')


@login_required
def address(request):
 add = Customer.objects.filter(user=request.user)

 return render(request, 'app/address.html', {'add': add})


@login_required
def orders(request):
      op = OrderPlaced.objects.filter(user=request.user)
      return render(request, 'app/orders.html', {'order_placed': op})


@method_decorator(login_required, name='dispatch')
class orderDeleteView(View):
  def get(self, request, pk):
    O = OrderPlaced.objects.get(pk=pk)
    print(O.status)
    if O.status == "ACCEPTED" or O.status == "Packed" or O.status == "Pending":
      O.delete()
    return redirect("/orders/")


def mobile(request):
 return render(request, 'app/mobile.html')


def login(request):
 return render(request, 'app/login.html')


class CustomerRegistrationView(View):
 def get(self, request):
   form = CustomerRegistrationForm()
   return render(request, 'app/customerregistration.html', {'form': form})

 def post(self, request):
     form = CustomerRegistrationForm(request.POST)
     if form.is_valid():
       messages.success(request, 'congrates registeration successfull')
       form.save()
     return render(request, 'app/customerregistration.html', {'form': form})


@login_required
def checkout(request):
      user = request.user
      add = Customer.objects.filter(user=user)

      if add:
         cart_items = Cart.objects.filter(user=user)
         amount = 0.0
         shipping_amount = 70.0
         totalamount = 0.0
         cart_product = [p for p in Cart.objects.all() if p.user == user]
         if cart_product:
               for p in cart_product:
   
                     tempamount = (p.quantity * p.product.discount_price)
        
                     amount += tempamount
               totalamount = amount+shipping_amount
               
         return render(request, 'app/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items})
      return redirect("/profile/")


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
      form = CustomerProfileForm()
      add = Customer.objects.filter(user=request.user)

      return render(request, 'app/profile.html', {'form': form, 'add': add[0:2]})

    def post(self, request):
         form = CustomerProfileForm(request.POST)
         add = Customer.objects.filter(user=request.user)
         if form.is_valid():
           usr = request.user
           name = form.cleaned_data['name']
           locality = form.cleaned_data['locality']
           city = form.cleaned_data['city']
           state = form.cleaned_data['state']
           zipcode = form.cleaned_data['zipcode']
           phoneNumber= form.cleaned_data['phoneNumber']

           reg = Customer(user=usr, name=name, locality=locality,
                          city=city, state=state, zipcode=zipcode,phoneNumber=phoneNumber)
           reg.save()
           messages.success(request, 'congratulation address is added')
         return render(request, 'app/profile.html', {'form': form, 'add': add})
      




          

@login_required
def payment_done(request):
  user = request.user
  custid = request.GET.get('custid')
  customer = Customer.objects.get(id=custid)
  cart = Cart.objects.filter(user=user)
  for c in cart:
    print(c.Size)

    OrderPlaced(user=user,customer=customer, product=c.product,Size=c.Size,quantity=c.quantity).save()
    c.delete()
  return redirect("/orders/")




@method_decorator(login_required, name='dispatch')
class CustomerDeleteView(View):
  def get(self, request, pk):
    c = Customer.objects.get(pk=pk)
    c.delete()
    return redirect("/profile/")


def Contact(request):
  form = ContactForm(request.POST)
  if form.is_valid():
    form.save()
  return render(request,'app/contact.html',{'form':form})

  # 404 pages

def err_404(request, exception):
    err = '404'
    return render(request, 'app/404.html', {'err':err, 'msg':'Page not found'})

def err_500(request, *args,):
    err = '500'
    return render(request, 'app/404.html', {'err':err, 'msg':'There is a Server Error'})

# def handler_500_page(request, *args, **argv):
#   return render(request, 'app/404page.html')

