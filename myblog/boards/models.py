from django.db import models


class Board(models.Model):  # 게시글 등록/검색/수정/삭제를 위한 모델 클래스
    title = models.CharField(max_length=200, unique=True)  # 제목 : 중복 불가능
    author = models.CharField(max_length=30)  # 작성자
    content = models.TextField()  # 내용. TextField() : 길이 제한이 없는 문자열 입력
    created_on = models.DateTimeField(auto_now_add=True)  # 작성 시간

    # DateTimeField(auto_now_add=True) : 해당 데이터 생성시 현재 시간 자동 저장

    # 전체 데이터를 create_on 기준으로 정렬하기 위한 Meta 클래스
    class Meta:
        ordering = ['-created_on']