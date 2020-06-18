from django.db import models


# Create your models here.

# 예시를 위한 유저 모델을 생성
class CusUser (models.Model) :
    # 이메일 로그인을 위해서 이메일을 속성 값으로 지정
    email = models.EmailField()
    # 이름은 캐릭터형 속성
    name = models.CharField(max_length=10)
    # 패스워드의 암호화 및 복호화는 후에 알려주도록 하고 지금은 그냥 넘어가는걸로 하겠음
    password = models.CharField(max_length=20)
    # 남자인지 여자인지 성별을 구분하기 위한 True/False만 데이터로 받을 수 있는 Boolean속성 지정
    isMale = models.BooleanField(default=True)