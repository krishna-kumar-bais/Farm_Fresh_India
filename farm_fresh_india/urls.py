"""
URL configuration for farm_fresh_india project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from products import views as product_views
from users import views as user_views
from cart import views as cart_views
from django.conf.urls.i18n import i18n_patterns

# Base URL patterns (not translated)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# URL patterns that will be translated
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    
    # Home, About, Contact
    path('', product_views.home, name='home'),
    path('about/', product_views.about, name='about'),
    path('contact/', product_views.contact, name='contact'),
    
    # Products URLs
    path('categories/<str:category_type>/', product_views.CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', product_views.category_detail, name='category_detail'),
    path('product/<slug:slug>/', product_views.ProductDetailView.as_view(), name='product_detail'),
    
    # Cart URLs
    path('cart/', include([
        path('', cart_views.cart_detail, name='cart_detail'),
        path('add/<int:product_id>/', cart_views.cart_add, name='cart_add'),
        path('remove/<int:product_id>/', cart_views.cart_remove, name='cart_remove'),
        path('checkout/', cart_views.checkout, name='checkout'),
        path('order/<int:order_id>/', cart_views.order_detail, name='order_detail'),
    ])),
    
    # User URLs
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('my-orders/', user_views.my_orders, name='my_orders'),
    path('my-orders/<int:order_id>/', user_views.order_detail, name='user_order_detail'),
    prefix_default_language=False,
)

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
