from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Stock
from .services import AngelBrokingService

class StockListView(ListView):
    model = Stock
    template_name = 'stock_trading/stock_list.html'
    context_object_name = 'stocks'

class StockCreateView(CreateView):
    model = Stock
    fields = ['stock_name', 'stock_code']
    success_url = reverse_lazy('stock_trading:stock-list')

    def form_valid(self, form):
        messages.success(self.request, 'Stock added successfully.')
        return super().form_valid(form)

class StockUpdateView(UpdateView):
    model = Stock
    fields = ['stock_name', 'stock_code']
    success_url = reverse_lazy('stock_trading:stock-list')

    def form_valid(self, form):
        messages.success(self.request, 'Stock updated successfully.')
        return super().form_valid(form)

class StockDeleteView(DeleteView):
    model = Stock
    success_url = reverse_lazy('stock_trading:stock-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Stock deleted successfully.')
        return super().delete(request, *args, **kwargs)

def get_balance(request):
    service = AngelBrokingService()
    try:
        balance = service.get_balance()
        return JsonResponse({'status': 'success', 'balance': balance})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def get_stock_ltp(request, stock_code):
    service = AngelBrokingService()
    try:
        ltp_data = service.get_ltp(stock_code)
        return JsonResponse({'status': 'success', 'ltp': ltp_data})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
