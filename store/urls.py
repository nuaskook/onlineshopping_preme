from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('payment/', views.payment, name="payment"),
	path('transfer/', views.transfer, name="transfer"),
	path('credit/', views.credit, name="credit"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('test/', views.test, name="test"),
	path('home/', views.home, name="home"),
	path('track/', views.track, name="tracker"),
	path('indexmenu/',views.indexmenu,name='indexmenu'),

]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
