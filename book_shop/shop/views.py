from django.shortcuts import get_object_or_404,HttpResponse
from django.views.generic import ListView, DetailView
from .models import Product, Category
from cart.forms import CartAddProductForm
import requests


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.filter(available=True)

        if 'category_slug' in self.kwargs:
            category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
            context['products'] = Product.objects.filter(category=category)
            context['category'] = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        context['product']= get_object_or_404(Product, slug=self.kwargs['slug'])
        context['cart_product_form'] = CartAddProductForm()  #add product  to cart
        return context


#
# def product_detail(request, pk, slug):
#     product = get_object_or_404(Product, id=pk, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product/detail.html',
#                   {'product': product,
#                    'cart_product_form': cart_product_form})

