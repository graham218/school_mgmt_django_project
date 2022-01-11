from django.urls import path
from .import views

urlpatterns = [
    path('add-students/', views.AddStudents, name='add-students'),
    path('edit-students/<str:pk>', views.EditStudents, name='edit-students'),
    path('add-lecturer/', views.AddLecturer, name='add-lecturer'),
    path('edit-lecturer/<str:pk>', views.EditLecturer, name='edit-lecturer'),
    path('add-faculty/', views.AddFaculty, name='add-faculty'),
    path('edit-faculty/<str:pk>', views.EditFaculty, name='edit-faculty'),
    path('add-gender/', views.AddGender, name='add-gender'),
    path('edit-gender/<str:pk>', views.EditGender, name='edit-gender'),
    path('add-students/', views.AddStudents, name='add-students'),
]
