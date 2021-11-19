from collections import defaultdict
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, response
from .forms import NameForm
from .models import TbUserInfo
from django.core import serializers




# Create your views here.
def index(request):

    userinfo = TbUserInfo.objects.filter()
    userinfo_id = serializers.serialize("json",userinfo)
    print(userinfo_id)
    #userinfo_id = [TbUserInfo.as_dict() for TBuserInfo in userinfo]
    if request.method =='POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print(form['id'])
            return render(request, 'account/index.html', {'form': form, 'userinfo_id' : userinfo_id})
    else : 
        form = NameForm()

        return render(request, 'account/index.html', {'form': form, 'userinfo_id':userinfo_id })        

def sign(request):

    user_id = request.POST['user_id']
    user_password = request.POST['passWord']
    user_name = request.POST['name']
    user_email = request.POST['email']
    user_phone = request.POST['phone_number']

    userDB = TbUserInfo()
   
    userDB.user_id = str(user_id)
    userDB.user_pwd = str(user_password)
    userDB.user_name = str(user_name)
    userDB.user_email = str(user_email)
    userDB.user_phone = str(user_phone)
  

    userDB.save()

    return HttpResponse("가입이 정상적으로 완료되었습니다.")        

def main(request):
    # POST방식일 경우
    if request.method =="POST":
        userid = request.POST.get('id',None)
        userpwd = request.POST.get('password',None)

        context = {}
        
        if not (userid and userpwd):
            context['error'] = '모든 값을 입력해야 합니다.'
        else:
            userinfo =   get_object_or_404(TbUserInfo, pk=userid)
            print(userpwd)
            print(userinfo.user_pwd)
            if userpwd == userinfo.user_pwd:
                request.session['user'] = userinfo.user_id
                
                context['session_id'] = request.session['user']
                
                print(context['session_id'])
                return render(request, 'account/main.html', context)
            else:
                context['error'] = '모든 값을 입력해야 합니다.'    

        return render(request, 'account/main.html')
    # 아닐경우
    else:
        return render(request, 'account/main.html')

def logout(request):
    print("logout")
    print("logout : "+request.session['user'])

    if request.session['user']:
        
        del request.session['user']

    return render(request, 'account/main.html')
    


 