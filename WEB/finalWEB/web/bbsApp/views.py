from django.shortcuts import render, redirect
from .models import *

# Create your views here.
# select * from table;
# modeName.objects.all()

# select * from table where id = xxxx;
# modelName.objects.get(id = xxxx)
# modelName.objects filter(id = xxxx)

# select * from table where id = xxxx and pwd =xxxx ;
# modelName.objects.get(id = xxxx, pwd = xxxx)
# modelName.objects filter(id = xxxx, pwd = xxxx)

# select * from table where id = xxxx or pwd =xxxx ;
# modelName.objects.filter(Q(id = xxxx) | Q(pwd = xxxx))

# select * from table where subject like '%공지%'
# modelName.objects.filter(subject_icontains='공지')
# select * from table where subject like '공지%'
# modelName.objects.filter(subject_startswith='공지')
# select * from table where subject like '%공지'
# modelName.objects.filter(subject_endswith='공지')

# insert into table values()
# model(attr=value, attr=value)
# model.save()

# delete * form tableName where id = xxxx
# modelName.objects.get(id=xxxx).delete()

# update tableName set attr = value where id = xxxx
# obj = modelName.objects.get(id=xxxx)
# obj.attr = value
# obj.save() --commit

def index(request):
    return render(request, 'login.html')

def loginProc(request) :
    print('request - loginProc')
    if request.method == 'GET' :
        return redirect('index')
    elif request.method == 'POST' :
        id = request.POST['id']
        pwd = request.POST['pwd']
        # if id == 'jslim' and pwd == 'jslim' :
        #     return render(request, 'home.html')
        # else:
        #     return redirect('index')
        user = BbsUserRegister.objects.get(user_id=id, user_pwd=pwd)
        print('user result - ' , user)
        if user is not None :
            return render(request, 'home.html')
        else :
            return redirect('index')

def registerForm(request) :
    return render(request, 'join.html')

def register(request) :
    if request.method == 'POST':
        id       = request.POST['id']
        pwd      = request.POST['pwd']
        name     = request.POST['name']
        register = BbsUserRegister(user_id =  id, user_pwd = pwd, user_name = name)
        register.save()
    return render(request, 'login.html')
