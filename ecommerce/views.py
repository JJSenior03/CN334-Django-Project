from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ecommerce_index_view(request):
    """This Function render index page of ecommerce views"""

    return HttpResponse("Welcome to 6410742024 Sathit Juntanasatan views!!!")


def item_view(request, item_id):
    
    context_data = {"item_id": item_id}

    return render(request, "index.html", context=context_data)
