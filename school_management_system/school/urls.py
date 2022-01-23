from django.urls import path
from .import views, my_views

app_name='school'

urlpatterns = [
    path('add-address/', views.AddAddress, name='add-address'),
    path('edit-address/<str:pk>', views.UpdateAddress, name='edit-address'),
    path('delete-address/<str:pk>', views.DeleteAddress, name='delete-address'),
    path('show-address/', views.ShowAddress, name='show-address'),

    path('add-students/', views.AddStudents, name='add-students'),
    path('edit-students/<str:pk>', views.EditStudents, name='edit-students'),
    path('delete-student/<str:pk>', views.DeleteStudent, name='delete-student'),
    path('list-students/', views.ListStudents, name='list-students'),

    path('add-lecturer/', views.AddLecturer, name='add-lecturer'),
    path('edit-lecturer/<str:pk>', views.EditLecturer, name='edit-lecturer'),
    path('delete-lecturer/<str:pk>', views.DeleteLecturer, name='delete-lecturer'),
    path('list-lecturer/', views.Listlectures, name='list-lecturer'),
    
    path('add-faculty/', views.AddFaculty, name='add-faculty'),
    path('edit-faculty/<str:pk>', views.EditFaculty, name='edit-faculty'),
    path('delete-faculty/<str:pk>', views.DeleteFaculty, name='delete-faculty'),
    path('list-faculty/', views.ListFaculty, name='list-faculty'),

    path('add-gender/', views.AddGender, name='add-gender'),
    path('edit-gender/<str:pk>', views.EditGender, name='edit-gender'),
    path('delete-gender/<str:pk>', views.DeleteGender, name='delete-gender'),
    path('list-gender/', views.ListGender, name='list-gender'),

    path('add-programme/', views.AddProgramme, name='add-programme'),
    path('edit-programme/<str:pk>', views.EditProgramme, name='edit-programme'),
    path('delete-programme/<str:pk>', views.DeleteProgramme, name='delete-programme'),
    path('list-programme/', views.ListProgrammes, name='list-programme'),

    path('add-stage/', views.AddStage, name='add-stage'),
    path('edit-stage/<str:pk>', views.EditStage, name='edit-stage'),
    path('delete-stage/<str:pk>', views.DeleteStage, name='delete-stage'),
    path('list-stage/', views.ListStage, name='list-stage'),

    path('add-unit/', views.AddUnit, name='add-unit'),
    path('edit-unit/<str:pk>', views.EditUnit, name='edit-unit'),
    path('delete-unit/<str:pk>', views.DeleteUnit, name='delete-unit'),
    path('list-unit/', views.ListUnits, name='list-unit'),

    path('edit-student-profile/<str:pk>', my_views.EditStudentsProfile, name='edit-student-profile'),
    path('edit-lecturer-profile/<str:pk>', my_views.EditLecturerProfile, name='edit-lecturer-profile'),

    path('unit_registration/', my_views.unit_registration, name='unit_registration'),
    path('unregister_unit/<str:pk>', my_views.unregister_unit, name='unregister_unit'),
    path('insert_marks/<str:pk>', my_views.insert_marks, name='insert_marks'),
    path('list_registered_units/', my_views.list_registered_units, name='list_registered_units'),
]
