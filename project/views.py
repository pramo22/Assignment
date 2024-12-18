from django.shortcuts import render,redirect,get_object_or_404
from .models import Items
from .forms import ItemsForm
# Create your views here.
def home(request):
    items = Items.objects.all()
    context = {'items': items}
    return render(request, 'home.html', context)

def create_data(request):
    if request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ItemsForm()

    context = {'form': form}
    return render(request,'createitem.html', context)

def view_data(request, pk):
    items = get_object_or_404(Items,id=pk)
    context = {'items': items}
    return render(request, "retrieveitem.html", context)

def update_data(request, pk):
    items = get_object_or_404(Items, id=pk)
    if request.method == "POST":
        forms = ItemsForm(request.POST, instance=items)
        if forms.is_valid():
            forms.save()
            return redirect("home")
    else:
        forms = ItemsForm(instance=items)

    context = {'forms':forms}
    return render(request, 'update_item.html',context)

def delete_data(request, pk):
    items = get_object_or_404(Items,id=pk)

    if request.method == "POST":
        items.delete()
        return redirect("home")
    
    context = {'items': items}
    return render(request, 'delete_item.html', context)