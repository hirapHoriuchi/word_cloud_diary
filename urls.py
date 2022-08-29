from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.index, name='index'), #一覧ページ
    path('add/', views.add, name='add'), #追加ページ
    path('update/<int:pk>/', views.update, name='update'), #更新ページ
    path('delete/<int:pk>', views.delete, name='delete'), #削除ページ
    path('detail/<int:pk>', views.detail, name='detail'), #詳細ページ

]
