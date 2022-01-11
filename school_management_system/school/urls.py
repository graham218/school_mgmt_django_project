from django.urls import path
from .import views

app_name='school'

urlpatterns = [
    path('add-address/', views.AddAddress, name='add-address'),
    path('edit-address/<str:pk>', views.UpdateAddress, name='edit-address'),
    path('add-students/', views.AddStudents, name='add-students'),
    path('edit-students/<str:pk>', views.EditStudents, name='edit-students'),
    path('add-lecturer/', views.AddLecturer, name='add-lecturer'),
    path('edit-lecturer/<str:pk>', views.EditLecturer, name='edit-lecturer'),
    path('add-faculty/', views.AddFaculty, name='add-faculty'),
    path('edit-faculty/<str:pk>', views.EditFaculty, name='edit-faculty'),
    path('add-gender/', views.AddGender, name='add-gender'),
    path('edit-gender/<str:pk>', views.EditGender, name='edit-gender'),
    path('add-programme/', views.AddProgramme, name='add-programme'),
    path('edit-programme/<str:pk>', views.EditProgramme, name='edit-programme'),
    path('add-stage/', views.AddStage, name='add-stage'),
    path('edit-stage/<str:pk>', views.EditStage, name='edit-stage'),
    path('add-unit/', views.AddUnit, name='add-unit'),
    path('edit-unit/<str:pk>', views.EditUnit, name='edit-unit'),
]
