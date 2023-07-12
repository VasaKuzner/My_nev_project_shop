
from django.urls import path , include

from .views import *

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]


# запис по старому
# urlpatterns = [
#     url(r'^$', views.product_list, name='product_list'),
#     url(r'^(?P<category_slug>[-\w]+)/$',
#         views.product_list,
#         name='product_list_by_category'),
#     url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
#         views.product_detail,
#         name='product_detail'),
# ]