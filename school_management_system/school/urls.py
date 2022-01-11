from django.urls import path
from .import views

urlpatterns = [
    path('add-students/', views.AddStudents, name='add-students'),
    path('edit-students/<str:pk>', views.EditStudents, name='edit-students'),
    path('add-lecturer/', views.AddLecturer, name='add-lecturer'),
    path('edit-lecturer/<str:pk>', views.EditLecturer, name='edit-lecturer'),
    path('add-students/', views.AddStudents, name='add-students'),
    path('add-students/', views.AddStudents, name='add-students'),
    path('add-students/', views.AddStudents, name='add-students'),
    path('add-students/', views.AddStudents, name='add-students'),
    path('add-students/', views.AddStudents, name='add-students'),
]
