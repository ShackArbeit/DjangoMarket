from django.shortcuts import render,redirect
from item.models import Category,Items
from .forms import SignupForm

# 將從 item app 裡面所定義的 Category,Items models 拿過來用
def index(request):
      items=Items.objects.filter(is_sold=False)[0:6]
      categories=Category.objects.all()
      return render(request,'core/index.html',{
            'categories':categories,
            'items':items
      })
# Contact Page 目前只是暫時用來顯示一個 route 而已，並無實質作用
def contact(request):
      return render(request,'core/contact.html')

# 在定義在 forms.py 中的 SignupForm 拿過來用並實例化於變數 form
# 變數 form 將會用在 signup.html 中
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
