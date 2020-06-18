# lecture-django-4
lecture-django-4 how to use request &amp; session

session을 이용한 데이터 띄워놓는 방법
request를 통해 data를 전달받는 방법
 - POST를 이용할 시에 토큰 전송을 해야하므로 모든 데이터를 토큰화 함
 - POST를 받는 방법과 GET 방식이 있음
 - 제일 중요한 점은 session은 서버에 데이터를 저장하므로 데이터의 양이 많으면 많을 수록 부하가 일어남
 - cookie, cashe, local store 등등의 여러 방법이 있으나 복잡하므로 패스
 - js를 사용하여 패스워드가 맞는지 확인하는 구문을 넣었으나 신경쓰지 말고 다른 구절을 볼 수 있도록 하길 바람
