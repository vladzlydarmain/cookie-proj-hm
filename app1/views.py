from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Product



def view_main_page (request):
    context = {
        'product_list': Product.objects.all(),
    }
    response = render(request, 'main.html', context)

    try: 
        if request.method == "POST":
            id_product = request.POST.get('go_to_basket')
            old_cookie = request.COOKIES["id_products"]
            
            print(id_product)
            print(old_cookie)

            if id_product not in old_cookie:
                old_cookie += id_product
                response.set_cookie("id_products", old_cookie)
                print(old_cookie)
                
    except KeyError:
            response.set_cookie("id_products", "")


    return response


def view_basket (request):
    try:
        id_product_from_cookie = request.COOKIES["id_products"]
    except KeyError:
        id_product_from_cookie = ""

    list_of_id = []
    for i in id_product_from_cookie:
        list_of_id.append(i)

    list_id_in_busket = list(set(list_of_id))


    context = {
        'product_list': Product.objects.filter(pk__in = list_id_in_busket),
    }
    
    response = render(request, 'basket.html', context)

    list_cookie = ''
    if request.method == "POST":
        id_basket = request.POST.get('go_into_basket')

        for i in id_product_from_cookie:
            print(i)
            if i != id_basket:
                list_cookie += i
            
        print(list_cookie)
        response.set_cookie("id_products", list_cookie)
        # print(list_id_in_busket)
        # print(id_basket)

    return response
