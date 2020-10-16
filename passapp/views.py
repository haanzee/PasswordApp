from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm, SignUpForm, UpdateSignUpForm, PostForm
from django.contrib.auth.models import Group, User
from django.contrib import messages
from .models import Post

# Create your views here.
def HomePage(request):
    pdata = Post.objects.all()
    paginator = Paginator(pdata,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'passapp/home.html',{'pdata': pdata, 'page_obj': page_obj})

def AboutPage(request):
    return render(request, 'passapp/about.html')

def User_Login(request):
    if request.method == "POST":
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                messages.success(request, 'Log in Sucessfully')
                return HttpResponseRedirect('/')
    else:
        fm = LoginForm()
    return render(request, 'passapp/login.html', {'form': fm})

def User_SignUp(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                messages.success(request, 'Sucessfully login')
                user = fm.save()
                group = Group.objects.get(name='Author')
                user.groups.add(group)
        else:
            fm = SignUpForm()
        return render(request, 'passapp/signup.html',{'forms': fm})
    else:
        return HttpResponseRedirect('/')


def User_Profile(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = User.objects.get(pk=id)
            fm = SignUpForm(request.POST, instance = pi)
            if fm.is_valid():
                messages.success(request, 'Sucessfully login')
                fm.save()
                
        else:
            pi = User.objects.get(pk=id)
            fm = SignUpForm(instance=pi)
        return render(request, 'passapp/signup.html',{'forms': fm})
    else:
        return HttpResponseRedirect('/')

def User_Logout(request):
    logout(request)    
    return HttpResponseRedirect('/')

def Post_Create(request):
    if request.method == 'POST':
        frm = PostForm(request.POST)
        if frm.is_valid:
            messages.success(request, 'Record Success Entered')
            frm.save()
            return HttpResponseRedirect('/')
    else:
        frm = PostForm()
    return render(request, 'passapp/postcreate.html',{'form': frm})
 
def DashBoard(request):
    dt = Post.objects.all()
    paginator = Paginator(dt,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    user = request.user
    full_name = user.get_full_name()
    gps = user.groups.all()
    return render(request, 'passapp/dashboard.html',{'form': dt, 'full_name' : full_name, 'gps':gps, 'page_obj': page_obj})

def UpdatePost(request,id):
    if request.method == 'POST':
        pdata = Post.objects.get(pk=id)
        frm = PostForm(request.POST, instance=pdata)
        if frm.is_valid():
            frm.save()
            return HttpResponseRedirect('/')
    else:
        pd = Post.objects.get(pk=id)
        frm = PostForm(instance=pd)
    return render(request, 'passapp/postupdate.html', {'form':frm})


def DeletePost(request, id):
    if request.method == 'POST':
        deldata = Post.objects.get(pk=id)
        deldata.delete()
        return HttpResponseRedirect('/')


def contact(request):
    return render(request, 'passapp/contact.html')

def features(request):
    return render(request, 'passapp/feature.html')

def terms(request):
    return render(request, 'passapp/core/terms.html')

def refund(request):
    return render(request, 'passapp/core/refund.html')

def disclaimer(request):
    return render(request, 'passapp/core/disclaimer.html')

def privacy(request):
    return render(request, 'passapp/core/privacy.html')
