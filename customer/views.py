from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView
from account.models import Products


# Create your views here.

# class CustomerHomeView(TemplateView):
#     def get(self,request):
#         res=Products.objects.all()
#         return render(request,"cust_home.html",{"data":})
    


class CustomerHomeView(ListView):
    template_name="cust_home.html"
    queryset=Products.objects.all()
    context_object_name="products"

class ProductDetailView(View):
    def get(self,request,**kwargs):
        pid=kwargs.get('id')
        pro=Products.objects.get(id=pid)
        return render(request,"product_details.html",{"data":pro})