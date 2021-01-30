from django.db import models
from django.urls import reverse
# Create your models here.
# 모델 : 데이터베이스를 SQL 없이 다루기 위함
# 데이터를 객체화해서 다루겠다는 목적
# 모델 = 테이블
# 모델의 변수 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드 값(인스턴트의 필드 값) = 레코드의 컬럼 데이터 값
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼종류
    # 2. 제약사항(몇글자까지인지)
    # 3. Form의 종류
    # 4. Form에서의 제약사항

    def __str__(self):
        return "이름 : "+self.site_name+",주소 : "+self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

# 모델을 만듬 : 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정
# makemigrations : 모댈의 변경사항을 추적해서 기록
# migrate : 데이터베이스에 모델의 내용을 반영(데이블 생성)
