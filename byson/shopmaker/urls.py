from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start', views.start, name='start'),
    path('import_products', views.import_products, name='import-products'),
    path('preview', views.preview_layout, name='preview-layout'),
    path('tweak_layout', views.tweak_layout, name='tweak-layout'),
    path('shop/<int:pk>', views.ShopDetailView.as_view(), name='shop-detail'),
    path('image_import', views.image_import, name='image-import'),
    path('detect', views.detect, name='detect-products'),
    path('detect2', views.detect2, name='detect-products2'),
]