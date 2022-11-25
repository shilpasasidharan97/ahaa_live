from django.shortcuts import render, redirect

from website.models import Cart, CartItems, FrontBanner, Product, ProductPageBanner, Restaurant, Category, SubCategory
from django.http import JsonResponse
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request,id):
    resto = Restaurant.objects.get(id=id)
    categories = Category.objects.filter(restaurent=resto)
    main_banner = FrontBanner.objects.all().order_by('-image')
    # print(len(main_banner),"$"*10)
    if len(main_banner) >= 2:
        fist_banner = main_banner[0]
        footer_banner = main_banner[1]
    elif len(main_banner) >=1:
        fist_banner = main_banner[0]
        footer_banner = main_banner[0]
    context = {
        "categories":categories,
        "first":fist_banner,
        "footer_banner":footer_banner,
    }
    return render(request, 'menucard/home.html',context)


def products(request,id):
    catag = Category.objects.get(id=id)
    subcategories = SubCategory.objects.filter(is_active=True,Category=id)
    products = Product.objects.filter(subcategory__Category__id=id,is_available=True)
    product_banner = ProductPageBanner.objects.all().order_by('-image')
    # prd = Product.objects.filter(subcategory__Category__restaurent=sub.Category.restaurent)
    catagories = Category.objects.filter(restaurent = catag.restaurent)
    # print(prd)
    if len(products) <= 10:
        if len(product_banner) >= 2:
            fist_banner = product_banner[0]
            second_banner = product_banner[1]
            print(fist_banner,'first if')
        elif len(product_banner) >= 1:
            fist_banner = product_banner[0]
            second_banner = product_banner[0]
        
    context = {
        "subcategories":subcategories,
        "products":products,
        "fist_banner":fist_banner,
        "second_banner":second_banner,
        "prd":catagories,
    }
    return render(request, 'menucard/product.html',context)


def productData(request,id):
    products_data = Product.objects.get(id=id)
    data = {
        'name':products_data.name,
        'price':products_data.price,
        'ingrediants':products_data.ingrediants,
        'description':products_data.description,
        'image':products_data.image.url,
    }
    return JsonResponse(data)



def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def AddToCart(request,pid):
    product = Product.objects.get(id=pid)
    resto = product.subcategory.Category.id
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItems.objects.get(product=product, cart=cart)
        cart_item.quantity = cart_item.quantity+1
        cart_item.save()
        total_price = float(cart_item.quantity) * float(product.price)
        cart_item.total = total_price
        cart_item.save()
        cart.save()
    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
        total_price = 1 * float(product.price)
        cart_item.total = total_price
        cart_item.save()
        cart.save()
    return redirect('/menucard/product/'+str(resto))


def addQuantity(request):
    quantity = request.GET['quantity']
    id = request.GET['id']
    cart_obj = CartItems.objects.get(id=id)
    new_quantity = int(quantity) +1 
    product_total = float(new_quantity) * float(cart_obj.product.price)
    cart_obj.total = product_total
    cart_obj.save()
    CartItems.objects.filter(id=id).update(quantity=new_quantity, total=product_total)
    data = {
        'total':cart_obj.total,
        'unitprice':cart_obj.product.price,
    }
    return JsonResponse(data)

def lessQuantity(request):
    quantity = request.GET['quantity']
    id = request.GET['id']
    cart_obj = CartItems.objects.get(id=id)
    new_quantity = int(quantity) - 1
    product_total = float(new_quantity) * float(cart_obj.product.price)
    cart_obj.total = product_total
    cart_obj.save()
    CartItems.objects.filter(id=id).update(quantity=new_quantity, total=product_total)
    data = {
        'total':cart_obj.total,
        'unitprice':cart_obj.product.price,

    }
    return JsonResponse(data)

@csrf_exempt
def tableNumber(request):
    table_name = request.POST['tablenumber']
    messagestring = ''
    grandtotal=0
    cart_obj = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItems.objects.filter(cart=cart_obj)
    tresto_number  = CartItems.objects.filter(cart=cart_obj).last()
    phonenumber = tresto_number.product.subcategory.Category.restaurent.phone
    sub_total = CartItems.objects.filter(cart__cart_id=_cart_id(request)).aggregate(Sum('total'))
    # print(phonenumber,"|%"*20)
    data = []
    try:
        messagestring = 'https://wa.me/+91'+phonenumber+'?text=Table Number :'+table_name+\
                "%0a------Order Details------"
        print(messagestring)
        for i in cart_items:
            data1 = {
                # 'id':i['id'],
                'name':i.product.name,
                'quantity':i.quantity,
                'price':i.product.price,
                'sub_total': i.total,           
            }
            data.append(data1)
            i.delete()
            # grandtotal+=int(cart['quantity']) * int(cart['product_price'])   
        for i in data:
            messagestring +="%0aProduct-Name:"+str(i['name'])+"%0aQuantity:"+str(i['quantity'])+"%0aUnit-Price:"+str(i['price'])+"%0aTotal :"+str(i['sub_total'])+"%0a-----------------------------"
            messagestring+="%0a-----------------------------"
        messagestring+="%0a-----------------------------\
        Grand Total :"+str(sub_total)+"%0a-----------------------------"
        cart_obj.delete()
        # data = {
        #     "link":messagestring,
        # }
        # return JsonResponse(data)
    except Exception as e:
        pass
    data = {
        "link":messagestring,
    }
    return JsonResponse(data)


def cart(request):
    # cart = Cart.objects.filter(cart_id=_cart_id(request))
    cart_items = CartItems.objects.filter(cart__cart_id=_cart_id(request))
    sub_total = CartItems.objects.filter(cart__cart_id=_cart_id(request)).aggregate(Sum('total'))
    # categories = CartItems.objects.filter(cart_items__product__subcategory__Category=resto)
    context = {
        'cartitems':cart_items,
        "sub_total":sub_total,
        # "link":messagestring
    }
    return render(request, 'menucard/cart.html', context)


def orderSuccess(request):
    return render(request, 'menucard/order-success.html')


def deleteCart(request,id):
    CartItems.objects.get(id=id).delete()
    return redirect('menucard:cart')