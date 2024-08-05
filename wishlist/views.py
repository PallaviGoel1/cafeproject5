from django.shortcuts import render, redirect, get_object_or_404, reverse
from products.models import Product, Category
from wishlist.models import wishList
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required
def wishlist(request):
    """ A view that provides the wishlist of products """
    if request.user.is_authenticated:
        my_wishlist = wishList.objects.filter(user=request.user)
    
        my_wishlist_products = []
        queryset = Product.objects.none()
        for val in my_wishlist:
            my_wishlist_products.append(val.product)
            queryset |= Product.objects.filter(sku=val.product.sku)
        my_wishlist = queryset

        query = None
        categories = None
        sort = None
        direction = None

        if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    my_wishlist = my_wishlist.annotate(lower_name=Lower('name'))
                if sortkey == 'category':
                    sortkey = 'category__name'
                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                my_wishlist = my_wishlist.order_by(sortkey)
                print(my_wishlist)    
            if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                my_wishlist = my_wishlist.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)

            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('wishlist'))            
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                my_wishlist = my_wishlist.filter(queries)
        
        current_sorting = f'{sort}_{direction}'
        context = {
            'wishlist': my_wishlist,
            'search_term': query,
            'current_categories': categories,
            'current_sorting': current_sorting,
        }
        return render(request, 'wishlist/wishlist.html', context)


def Add_to_wishlist(request, product_id):
    """ A view that provides a form for creating a new entry in
    Wishlist """

    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_authenticated:
        messages.error(
            request, "You must be logged in to add items to your wishlist.")
        return redirect('login')
    else:
        # Create a new entry in the user's wishlist for the product
        my_wishlist = wishList.objects.filter(user=request.user)
        my_wishlist_products = []
        for val in my_wishlist:
            my_wishlist_products.append(val.product)
        
        wishlist_item = wishList(user=request.user, product=product)
        if product not in my_wishlist_products:
            wishlist_item.save()
            messages.success(
                request, f"{product.name} has been added to your wishlist.")
        else:
            messages.error(request, f"{product.name} is already in wishlist.")

    return redirect('wishlist')


def Remove_from_wishlist(request, product_id):
    """ To remove products from wishlist """

    product = get_object_or_404(Product, pk=product_id)
    my_wishlist_item = get_object_or_404(
        wishList, user=request.user, product=product)
    
    my_wishlist_item.delete()
    messages.success(request, f"{product.name} is remove from wishlist.")

    return redirect('wishlist')