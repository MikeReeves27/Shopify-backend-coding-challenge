import csv

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Item


# Function for viewing items. It retrieves all data from the database and stores it in a dictionary
def view_items(request):
    all_items = Item.objects.all()
    return render(request, 'view.html', {'all_inventory': all_items})


# Function for adding a new item. It redirects user to the 'add.html' template page
def add_item(request):
    return render(request, 'add.html')


# Function for saving the data from a new item in the database
def save_item(request):
    new_item = Item(product_id=request.POST['product_id'], product_name=request.POST['product_name'],
                    product_quantity=request.POST['product_quantity'], product_price=request.POST['product_price'])
    new_item.save()
    return HttpResponseRedirect('/add/')


# Function for retrieving the data of an existing item in the database
def get_item(request, item_id):
    current_item = Item.objects.get(id=item_id)
    return render(request, 'edit.html', {'item': current_item})


# Function for editing the data of an existing item in the database
def edit_item(request, item_id):
    current_item = Item.objects.get(id=item_id)
    current_item.product_id = request.POST['product_id']
    current_item.product_name = request.POST['product_name']
    current_item.product_quantity = request.POST['product_quantity']
    current_item.product_price = request.POST['product_price']
    current_item.save()
    return HttpResponseRedirect('/')


# Function for deleting an existing item in the database
def delete_item(request, item_id):
    Item.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/')


# Function for downloading all items in the database and storing them in a .CSV file
def download(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="inventory.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Product ID', 'Product Name', 'Quantity', 'Price'])

    all_items = Item.objects.all()
    for item in all_items:
        writer.writerow([item.product_id, item.product_name, item.product_quantity, item.product_price])

    return response
