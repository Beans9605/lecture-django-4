from django.shortcuts import render, redirect
from .models import CusUser

# Create your views here.

def home(request) :
    return render(request, 'mainsite/home.html')

def create_user(request) :
    # request로 오는 방식이 POST방식으로 데이터를 받았는지 확인
    if request.method == 'POST' :
        # request POST 에서 데이터를 하나씩 이름 별로 꺼내오는 작업
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        isMale = request.POST['isCheck']
        # checkbox 사용 시에는 True/False로 오지 않음, on/off 문자열로 오기 때문에 boolean형 재작업 필요
        if isMale == 'on' :
            isMale = True
        else :
            isMale = False
        # 받아온 데이터를 모델에 맞게 넣어서 저장하는 작업
        cususer = CusUser (
            email = email,
            name = name,
            password = password,
            isMale = isMale
        )
        # 데이터 저장
        cususer.save()
        # redirect는 이미 있는 url과 views의 함수로 이동해주는 역할, 렌더링을 통해 html에 접근하지 않음
        return redirect('login')


def login(request) :
    if request.method == 'POST' :
        email = request.POST['email']
        password = request.POST['password']
        
        try :
            user = CusUser.objects.get(email=email)

            if user.password == password :
                request.session['user'] = user.email
                return redirect('home')
            else :
                context = {'err' : "Check your password"}
                return render(request, "mainsite/login.html", context)
        except :
            context = {'err' : "Check your email or password"}
            return render(request, "mainsite/login.html", context)

    return render(request, "mainsite/login.html")