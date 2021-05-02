django-admin startproject baseWEB



settings들어가서 localhost, 127.0.0.1

Asia/Seoul



cd  djangoWEB -->manage.py파일이 있는지 확인

dir/w



서버실행 명령어

python manage.py runserver



서버다운 명령어

컨 + c



크롬 브라우저 이용해서 서버접속 명령어

http://127.0.0.1:8000/



manage.py파일이 있는 디렉토리에서 앱 만들기

python manage.py startapp GreetingApp



settibngs에 app추가



static 위치를 지정해주는 작업, 각각의 app에 흩어져 있는 static을 한곳으로 모음

web> python manage.py collectstatic



model생성 후 admin등록

python manage.py makemigrations

python manage.py migrate



orm을 통한 데이터베이스 관리를 위한 계정생성 및 접근

python manage.py createsuperuser





