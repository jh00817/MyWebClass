from django.contrib import admin
from django.urls import include, path


urlpatterns = [
   path('', include('boards.urls')),
   path('admin/', admin.site.urls), # 관리자 사이트 url 정보 적용
]