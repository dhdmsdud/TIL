from django.shortcuts import render
from django.http      import JsonResponse

# Create your views here.
def index(request) :
    print('request debug : ')
    return render(request, 'frontDemo.html')

def nonAjax(request) :
    print('request ajax - nonAjax')
    list = [{'id': 'multicampus04', 'pwd': 'multicampus04'},
            {'id': 'multicampus05', 'pwd': 'multicampus05'}]

    return JsonResponse(list , safe=False)

def paramAjax(request) :
    id = request.POST['user_id']
    pwd =request.POST['user_pwd']
    print('ajax param - ', id, pwd)

    list = [{'id': 'multicampus04', 'pwd': 'multicampus04'},
            {'id': 'multicampus05', 'pwd': 'multicampus05'}]

    return JsonResponse(list , safe=False)

def chart(request) :
    data = [
          ['Task', 'Hours per Day'],
          ['Work',     11],
          ['Eat',      2],
          ['Commute',  2],
          ['Watch TV', 2],
          ['Sleep',    7]
        ]
    context = {'data' : data}
    return render(request, 'chartDemo.html', context)