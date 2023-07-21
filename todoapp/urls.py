from django.urls import path

from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='TaskListView'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='TaskDetailView'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='TaskUpdateView'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='TaskDeleteView')



 ]