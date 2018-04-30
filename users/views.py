from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
# 并集运算
from django.db.models import Q
# 基于类实现需要继承的view
from django.views.generic.base import View
#密码明文加密
from django.contrib.auth.hashers import make_password

from use_ckeditor.models import *
from users.models import UserProfile
from utils.eamil_send import EmailVerifyRecord
from .forms import LoginForm,RegisterForm
from utils.eamil_send import send_email
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        第一步查找用户名是否存在，若存在，则继续验证密码，如果都通过，则返回user。
        有任何异常都直接返回空，一般是用户名不存在。
        同样的道理，既然可以先检查用户名是否存在来确认用户（因为用户名唯一）那么我们也可以使用email
        """
        try:
            user_obj = UserProfile.objects.get(Q(username=username) |Q(email=username))
            if user_obj.check_password(password):
                return user_obj
        except Exception as e:
            return None

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html', {})

    def post(self,request):
        login_form = LoginForm(request.POST)
        # 1.  先判断是否通过验证
        if login_form.is_valid():
            user_name = request.POST.get("user_name", "")
            pass_word = request.POST.get("user_password", "")
            user = authenticate(username=user_name, password=pass_word)
            # 用户登录分两步   第一步认证通过则user是对象，否则是None
            if user is not None:
                if user.is_active:
                # 第二步 login，向request里面写东西，然后返回到render里面(在激活的前提下)    ==  激活后才能登录
                    login(request, user)
                    # 正常应该返回到首页
                    return render(request, 'index.html',{}
                              )
                else:
                    return  render(request, 'login.html', {"error_msg": "该用户没有激活哦！请激活后再来登录"})
            else:
                return render(request, 'login.html', {"error_msg": "没有此用户，请检查用户名或密码是否正确"})
        else:
            return render(request, 'login.html', {"login_form":login_form})


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request, 'register.html', {
                'register_form': register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        # 1.  先判断是否通过验证
        if register_form.is_valid():
            user_name = request.POST.get("email", "")

            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {"register_form": register_form,"msg": "用户已存在"})
            else:
                pass_word = request.POST.get("password", "")
                # 实例化一个user_profile对象，将前台值存入
                user_profile = UserProfile()
                user_profile.username = user_name
                user_profile.email = user_name
                user_profile.password = make_password(pass_word)  #密码明文加密
                # 默认激活状态为false
                user_profile.is_active = False

                try:
                    send_email_status = send_email(user_name,"register")
                    if send_email_status ==1:
                        user_profile.save()
                        return render(request, "login.html",{"msg":"恭喜您注册成功！请点击邮箱链接激活账户"} )
                except Exception as e:
                    return render(request, "login.html", {"msg": "发送邮件失败！请重新注册"})
        else:
            return render(request, 'register.html', {"register_form":register_form})



class UserActiveView(View):
    def get(self,request,activecode):
        all_activecode_record = EmailVerifyRecord.objects.filter( code = activecode )
        print(activecode)
        if all_activecode_record:
            for record in all_activecode_record:
                active_user = UserProfile.objects.get(email = record.email )
                active_user.is_active = True
                active_user.save()

        return render(request, "login.html", {'msg':'用户激活成功!  请登录'})

