from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
# auth_views : login/logout 기능을 수행하는 모듈


urlpatterns = [
    path('', views.BoardList.as_view(), name='index'),
    path('detail/<int:board_id>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('write/write-board/', views.write_board, name='write-board'),
    path('update/<int:board_id>', views.update, name='update'),
    path('update/update-board/<int:board_id>', views.update_board, name='update-board'),
    path('delete-board/<int:board_id>', views.delete_board, name='delete-board'),
    path('signup/', views.signup, name='signup'),
    path('signup/add-user/', views.add_user, name='add-user'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
