from django.urls import path
from . import views

app_name = 'stock_trading'

urlpatterns = [
    path('', views.StockListView.as_view(), name='stock-list'),
    path('stock/add/', views.StockCreateView.as_view(), name='stock-add'),
    path('stock/<int:pk>/update/', views.StockUpdateView.as_view(), name='stock-update'),
    path('stock/<int:pk>/delete/', views.StockDeleteView.as_view(), name='stock-delete'),
    path('api/balance/', views.get_balance, name='get-balance'),
    path('api/ltp/<str:stock_code>/', views.get_stock_ltp, name='get-stock-ltp'),
]
