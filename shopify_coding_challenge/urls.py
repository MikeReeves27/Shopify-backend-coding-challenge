from django.urls import path
from inventory.views import view_items, add_item, save_item, get_item, edit_item, delete_item, download

# Store each URL and their respective function in a list
urlpatterns = [
    path('', view_items),
    path('add/', add_item),
    path('save/', save_item),
    path('get/<int:item_id>/', get_item),
    path('edit/<int:item_id>/', edit_item),
    path('delete/<int:item_id>/', delete_item),
    path('download/', download)
]
