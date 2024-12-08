from django.shortcuts import render, redirect , get_object_or_404
from .models import Product,Staff
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import ProductForm
# Create your views here.
def editproduct(req,pk):
    product = get_object_or_404(Product, id = pk)
    form = ProductForm(req.POST, req.FILES, instance=product or None)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("product")
        else:
            form = ProductForm(instance=product)
 
    return render(req, "editproduct.html", context= { 'form': form, 'product': product})
def product(req):
    product= Product.objects.all()
    return render(req,'product.html',context={'data':product})
def home(req):
    product= Product.objects.all()
    paginator = Paginator(product, 6)
    pageNumber = req.GET.get('page')
    try:
        product= paginator.page(pageNumber)
    except PageNotAnInteger:
        product=paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    return render(req, 'home.html',context={'data':product}) 

def signin(req):
    return render(req, 'signin.html')
def signup(req):
    return render(req, 'signup.html')

def getStaff(req):
    staff= Staff.objects.all()
    return render(req,'staff.html',context={'data':staff})
def login_user(req):
    if req.method =="POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req,username = username, password = password)
        if user is not None:
            return redirect("home")
        else:
            return redirect('login')
    else:
        return render(req,'login.html')
    
def logout_user(req):
    logout(req)
    return redirect("home")

def search(req):
    #Kiểm tra nếu phương thức là POST
    if req.method == "POST":
        #Lấy ra từ khóa mà người dùng nhập vào
        user_input = req.POST.get("search")
        #Lọc data từ bảng Staff xem có đối tượng nào có tên trùng với từ khóa mà người dùng nhập vào
        rs_search = Product.objects.filter(name__icontains = user_input)
        return render(req, 'search.html', context= { 'data': rs_search })

def product_create(request):   
    if request.method == 'POST':      
        form = ProductForm(request.POST, request.FILES)        
        if form.is_valid():            
            form.save()    
            return redirect('product_view')
        else:        
            form = ProductForm()    
    return render(request, 'product1.html', context = {'form': form})

def product_update(request, pk):    
    product = get_object_or_404(Product, pk=pk)  
    # Lấy bài blog theo pk    
    form = ProductForm(request.POST, request.FILES, instance=product or None)        
    if request.method == 'POST':        
        if form.is_valid():            
            form.save()  
            # Lưu thay đổi           
            return redirect('product_view')  
        # Chuyển hướng về danh sách blog    
        else:        
            form = ProductForm(instance=product)    
    return render(request, 'editproduct.html', context = {'form': form, 'product': product})

def product_view(req):
    product = Product.objects.all()
    return render(req,"view_product.html",{'product': product})

def product_delete(req, pk):
    product = get_object_or_404(Product, pk = pk)
    product.delete()
    return redirect('product_view')