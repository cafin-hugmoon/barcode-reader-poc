from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem
from .forms import FoodItemForm

def list_food_items(request):
    """Display a list of all food items."""
    food_items = FoodItem.objects.all()
    return render(request, 'fooditem_list.html', {'food_items': food_items})

def food_item_detail(request, pk):
    """Display details of a single food item."""
    food_item = get_object_or_404(FoodItem, pk=pk)
    return render(request, 'fooditem_detail.html', {'food_item': food_item})

def food_item_create(request):
    """Create a new food item."""
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fooditem_list')
    else:
        form = FoodItemForm()
    return render(request, 'fooditem_form.html', {'form': form, 'food_item': None})

def food_item_update(request, pk):
    """Update an existing food item."""
    food_item = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('fooditem_detail', pk=pk)
    else:
        form = FoodItemForm(instance=food_item)
    return render(request, 'fooditem_form.html', {'form': form, 'food_item': food_item})

def food_item_delete(request, pk):
    """Delete a food item."""
    food_item = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        food_item.delete()
        return redirect('fooditem_list')
    return render(request, 'fooditem_confirm_delete.html', {'food_item': food_item})
