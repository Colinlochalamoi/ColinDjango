from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
import pdb

# Create your views here.
def home(request): 
  products = Product.objects
  # pdb.set_trace()
  return render (request, 'products/home.html',{'products': products})

@login_required(login_url='/accounts/signup')
def create(request): 
  if request.method == 'POST':
    if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image'] : 
      title =  request.POST['title']
      body = request.POST['body']
      if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
        url = request.POST['url']
      else: 
        url = 'http://' + request.POST['url']
      image = request.FILES['image']
      icon = request.FILES['icon']
  
      product = Product()

      product.title = title 
      product.body = body
      product.url = url
      product.icon = icon 
      product.image = image  
      product.pub_date = timezone.datetime.now()
      product.hunter = request.user
      
      product.save()

      return redirect('/products/' + str(product.id))
    else: 
      return render (request, 'products/create.html', {'errors' : 'All fields are required'})

  else:
    return render (request, 'products/create.html')

def detail(request,product_id): 
  product = get_object_or_404(Product,pk=product_id)
  return render(request,'products/detail.html', {"product": product})

@login_required(login_url='/accounts/signup')
def upvote(request,product_id): 
  if request.method == 'POST':
    product = get_object_or_404(Product,pk=product_id)
    #does not work
    product.votes += 1
    product.save()
    return redirect('/products/' + str(product.id))

