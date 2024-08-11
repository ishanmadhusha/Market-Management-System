from django.shortcuts import render
from .models import*
from .forms import*
from django.core.paginator import Paginator





# Create your views here.
def categoryview(request):
    page_number = request.GET.get('page')
    categories = Category.objects.all()
    paginator = Paginator(categories, 3)
    if page_number is None:
        page_number = 1
    page = paginator.get_page(page_number)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()
    
    context = {'form': form, 'page': page}
    return render(request, 'category.html', context)

def unitview(request):
    units= Unit.objects.all() 
    if request.method == 'POST':
        form=UnitForm(request.POST) 
        if form.is_valid():
            form.save()

    else :
        form=UnitForm()  

    context= {'form':form,'uts' : units}
    return render (request,'unit.html',context)

def itemview(request):
    items= Item.objects.all() 
    if request.method == 'POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            form.save() 

    else :
        form=ItemForm()  

    context= {'form':form,'itms' : items}
    return render (request,'item.html',context)


def supplierview(request):
    supplier= Supplier.objects.all()
    if request.method == 'POST':
        form=SupplierForm(request.POST) 
        if form.is_valid():
            form.save()

    else :
        form=SupplierForm()  

    context= {'form':form,'supplrs' : supplier}
    return render (request,'supplier.html',context)  

def orderview(request):
    orders= Order.objects.all() 
    if request.method == 'POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save() 

    else :
        form=OrderForm()  

    context= {'form':form,'odrs' : orders}
    return render (request,'order.html',context)

def employeeview(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()

    context = {'form': form, 'employees': employees}
    return render(request, 'employee.html', context)

def home(request):
    return render(request, 'home.html')