from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Board
from django.views import generic
from .forms import UserForm


class BoardList(generic.ListView):
    queryset = Board.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3 # 한 페이지당 게시글 3개씩 페이징 처리


def index(request):
    boards = Board.objects.all().values()
    template = loader.get_template('index.html')  # templates 폴더에 있는 html 파일 정보를 가져온다.
    context = {
        'boards': boards,
    }
    return HttpResponse(template.render(context, request))  # template을 view에 표현한다.


def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    template = loader.get_template('detail.html')
    context = {'board': board}
    return HttpResponse(template.render(context, request))


def write(request):
    template = loader.get_template('write.html')
    return HttpResponse(template.render({}, request))


def write_board(request):
    title = request.POST['title']  # input name="title" 값
    author = request.POST['author']  # input name="author" 값
    content = request.POST['content']  # input name="content" 값
    board = Board(title=title, author=author, content=content)
    board.save()  # 모델 객체 저장(DB에 등록)
    return HttpResponseRedirect(reverse('index'))  # index로 이동


def update(request, board_id):
    board = Board.objects.get(id=board_id)
    template = loader.get_template('update.html')
    context = {
        'board': board,
    }
    return HttpResponse(template.render(context, request))


def update_board(request, board_id):
    title = request.POST['title']  # input name="title" 값
    author = request.POST['author']  # input name="author" 값
    content = request.POST['content']  # input name="content" 값
    board = Board.objects.get(id=board_id)
    board.title = title  # 기존 데이터 수정
    board.author = author  # 기존 데이터 수정
    board.content = content  # 기존 데이터 수정
    board.save()  # 모델 객체 저장(DB에 등록)
    return HttpResponseRedirect(reverse('index'))  # index로 이동


def delete_board(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete()
    return HttpResponseRedirect(reverse('index'))  # index로 이동


def signup(request):
    template = loader.get_template('signup.html')
    form = UserForm()  # forms.py 파일에서 작성된 사용자 회원가입 form 객체
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def add_user(request):
    form = UserForm(request.POST)  # signup.html 파일에서 전송된 데이터를 UserForm에 적용
    if form.is_valid():  # form 규칙에 맞는 형태로 작성되면
        form.save()  # form 데이터를 User에 저장한다.
        return HttpResponseRedirect(reverse('index'))  # index로 이동
    template = loader.get_template('signup.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))
