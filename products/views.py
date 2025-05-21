from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Product, Farmer

def home(request):
    featured_products = Product.objects.filter(is_featured=True, available=True)[:8]
    normal_categories = Category.objects.filter(category_type='normal')
    organic_categories = Category.objects.filter(category_type='organic')
    farmers = Farmer.objects.all()[:4]
    
    context = {
        'featured_products': featured_products,
        'normal_categories': normal_categories,
        'organic_categories': organic_categories,
        'farmers': farmers,
    }
    return render(request, 'home/index.html', context)

def about(request):
    farmers = Farmer.objects.all()
    return render(request, 'home/about.html', {'farmers': farmers})

def contact(request):
    return render(request, 'home/contact.html')

class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        self.category_type = self.kwargs.get('category_type', None)
        if self.category_type:
            return Category.objects.filter(category_type=self.category_type)
        return Category.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_type'] = self.category_type
        return context

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'products/category_detail.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        related_products = Product.objects.filter(
            category=product.category
        ).exclude(id=product.id)[:4]
        context['related_products'] = related_products
        return context
