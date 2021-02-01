from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
import csv

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

# 사용자의 상태정보 저장을 위해서는 session, cookie 필요
def index(request):
    if request.session.get('user_id') and request.session.get('user_name'):
        context = {'id' : request.session['user_id'],
                   'name' : request.session['user_name']}
        return render(request, 'home.html', context)
    else:
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
        context = {}
        if user is not None :
            # session create
            request.session['user_name'] = user.user_name
            request.session['user_id']   = user.user_id
            # session write
            context['name'] = request.session['user_name']
            context['id']   = request.session['user_id']
            return render(request, 'home.html', context)
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

def logout(request) :
    request.session['user_name'] = {}
    request.session['user_id']   = {}
    request.session.modified     = True
    return redirect('index')

# bbs
def bbs_list(request) :
    # select * from bbs;
    # modelName.objects.all()
    boards = Bbs.objects.all()
    print('bbs_list request - ', type(boards), boards)
    context = {'boards' : boards,
               'name'   : request.session['user_name'],
               'id'     : request.session['user_id']}
    return render(request, 'list.html', context)

def bbs_registerForm(request) :
    context = {'name' : request.session['user_name'],
               'id'   : request.session['user_id']}
    return render(request, 'bbsRegisterForm.html', context)

def bbs_register(request) :
    title   = request.POST['title']
    content = request.POST['content']
    writer  = request.POST['writer']
    board   = Bbs(title = title, content = content, writer =writer)
    board.save()
    return redirect('bbs_list')

def bbs_read(request, id) :
    print('request bbs_read param id - ', id)
    board = Bbs.objects.get(id=id)
    board.viewcnt = board.viewcnt + 1
    board.save()
    context = {'board' : board,
               'name'   : request.session['user_name'],
               'id'     : request.session['user_id']
               }
    return render(request, 'read.html', context)

def bbs_remove(request):
    id = request.POST['id']
    print('request bbs_remove_param - ', id)
    Bbs.objects.get(id=id).delete()
    return redirect('bbs_list')

def bbs_modifyForm(request):
    id = request.POST['id']
    print('request bbs_modifyForm param - ', id)
    board = Bbs.objects.get(id=id)
    context = {'board': board,
               'name' : request.session['user_name'],
               'id'   : request.session['user_id']
               }
    return render(request, 'modify.html', context)

def bbs_modify(request) :
    id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']
    writer = request.POST['writer']
    print('request bbs_modify param - ', id, title, content, writer)
    board = Bbs.objects.get(id=id)
    board.title = title
    board.content = content
    board.save()

    return redirect('bbs_list')

def bbs_search(request):
    type = request.POST['type']
    keyword = request.POST['keyword']
    #print('request bbs_search - ', type, keyword)
    if type == 'title':
        boards = Bbs.objects.filter(title__icontains = keyword)
    if type == 'writer':
        boards = Bbs.objects.filter(writer__startwith=keyword)
        #print('ajax -result -', boards)
    list = []
    for board in boards:
         list.append({
            'id' : board.id, 'title' : board.title, 'writer' : board.writer,
             'regdate' : board.regdate, 'viewcnt' : board.viewcnt
        })
    return JsonResponse(list, safe=False)

def csvUpload(request):
    file = request.FILES['csv_file']
    print('request upload : ', file)
    if not file.name.endswith('.csv'):
        return redirect('index')

    result_file = file.read().decode('utf8').splitlines()
    print('result file : ', result_file, type(result_file))

    reader = csv.reader(result_file)
    list = []
    for row in reader:
        print('row : ', row)
    file.close()
    csvModel.objects.bulk_create(list)
    return redirect('index')






