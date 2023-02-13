from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from item.models import Item, Category

from item.forms import AddNewItem, AddNewCategories
from django.db.models import Q

# Create your views here.

def index(request):
    categories = Category.objects.all()
    query = request.GET.get('query', '')
    print(query)
    if query:
        categories = categories.filter(Q(name__icontains=query))
    context = {'categories':categories, 'query':query}
 
    return render(request, 'item/category_list.html', context)

def item_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    print(category.id)
    query = request.GET.get('query', '')
    print(query)
    items = Item.objects.filter(category_id=category.id, is_sold=False)
    print(items)

    if query:
        items = items.filter(Q(name__icontains=query))
    context = {'items':items, 'query':query}
    return render(request, 'item/item_list.html', context)

@login_required(login_url='account:login')
def add_item(request):
    if request.method == 'POST':
        form = AddNewItem(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:item_list', pk=item.category.id)
    else:
        form = AddNewItem()

    context = {'form':form}
    return render(request, 'item/add_item.html', context)

@login_required(login_url='account:login')
def add_category(request):
    if request.method == 'POST':
        form = AddNewCategories(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item:category')
        
    else:
        form = AddNewCategories()
    
    context = {'form':form}
    
    return render(request, 'item/add_category.html', context)