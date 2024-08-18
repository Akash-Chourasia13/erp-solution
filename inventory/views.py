from django.shortcuts import render, get_object_or_404
from .models import Product
from rest_framework import viewsets,filters
from rest_framework.response import Response


class productlistViewSet(viewsets.ViewSet):
    def list(self,request):
        print("111")
        if request.method == 'POST':
            barcode = request.POST.get('barcode')
            if barcode:
                product = get_object_or_404(Product, barcode=barcode)
                # Add additional logic if needed (e.g., add to cart, adjust stock)
                context = {'product': product}
                return render(request, 'productDetail.html', context)

        products = Product.objects.all()
        # return Response(request,'pro')
        return render(request, 'productList.html', {'products': products})
