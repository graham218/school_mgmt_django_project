from django.urls import path
from .import views, my_views, views2

app_name='school'

urlpatterns = [
    path('add-address/', views.AddAddress, name='add-address'),
    path('edit-address/<str:pk>', views.UpdateAddress, name='edit-address'),
    path('delete-address/<str:pk>', views.DeleteAddress, name='delete-address'),
    path('show-address/', views.ShowAddress, name='show-address'),

    path('add-students/', views.AddStudents, name='add_students'),
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

    path('unit_registration2/', my_views.unit_registration2, name='unit_registration2'),
    path('unregister_unit2/<str:pk>', my_views.unregister_unit2, name='unregister_unit2'),
    path('insert_marks2/<str:pk>', my_views.insert_marks2, name='insert_marks2'),
    path('list_registered_units2/', my_views.list_registered_units2, name='list_registered_units2'),

    path('unit_registration3/', my_views.unit_registration3, name='unit_registration3'),
    path('unregister_unit3/<str:pk>', my_views.unregister_unit3, name='unregister_unit3'),
    path('insert_marks/<str:pk>', my_views.insert_marks, name='insert_marks'),
    path('list_registered_units3/', my_views.list_registered_units3, name='list_registered_units3'),

    path('unit_registration4/', my_views.unit_registration4, name='unit_registration4'),
    path('unregister_unit4/<str:pk>', my_views.unregister_unit4, name='unregister_unit4'),
    path('insert_marks4/<str:pk>', my_views.insert_marks4, name='insert_marks4'),
    path('list_registered_units4/', my_views.list_registered_units4, name='list_registered_units4'),

    path('unit_registration5/', my_views.unit_registration5, name='unit_registration5'),
    path('unregister_unit5/<str:pk>', my_views.unregister_unit5, name='unregister_unit5'),
    path('insert_marks5/<str:pk>', my_views.insert_marks5, name='insert_marks5'),
    path('list_registered_units5/', my_views.list_registered_units5, name='list_registered_units5'),

    path('unit_registration6/', my_views.unit_registration6, name='unit_registration6'),
    path('unregister_unit5/<str:pk>', my_views.unregister_unit6, name='unregister_unit6'),
    path('insert_marks6/<str:pk>', my_views.insert_marks6, name='insert_marks6'),
    path('list_registered_units6/', my_views.list_registered_units6, name='list_registered_units6'),

    path('unit_registration7/', my_views.unit_registration7, name='unit_registration7'),
    path('unregister_unit7/<str:pk>', my_views.unregister_unit7, name='unregister_unit7'),
    path('insert_marks7/<str:pk>', my_views.insert_marks7, name='insert_marks7'),
    path('list_registered_units7/', my_views.list_registered_units7, name='list_registered_units7'),

    path('FeeReceiptList/', views2.FeeReceiptList, name='FeeReceiptList'),
    path('special_exams/', views2.special_exams, name='special_exams'),
    path('special_exams_marks/<str:pk>', views2.special_exams_marks, name='special_exams_marks'),
    path('SpecialExamList/', views2.SpecialExamList, name='SpecialExamList'),
    path('lecturer_units/', views2.lecturer_units, name='lecturer_units'),
    path('lecturer_units_edit/<str:pk>', views2.lecturer_units_edit, name='lecturer_units_edit'),
    path('lecturer_units_delete/', views2.lecturer_units_delete, name='lecturer_units_delete'),
]
