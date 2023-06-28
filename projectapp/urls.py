# 우리가 설정할 view 에 대한 라우팅
from django.urls import path

from projectapp.views import ProjectListView, ProjectCreateView, ProjectDetailView

app_name = 'projectapp'

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'),

    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
]

