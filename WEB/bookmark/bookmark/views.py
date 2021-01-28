from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# 클래스형 뷰, 함수형 뷰
# 웹 페이지에 접속한다. -> 페이지를 본다.
# URL 압력 -> 웹 서버가 뷰를 찾아서 동작 -> 응답

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView) :
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'
