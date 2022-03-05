from django.urls import path
from .import views, my_views, views2, paypal_views

app_name='school'

urlpatterns = [
    path('create_student_profile/', views.AddStudentsProfile, name='create_student_profile'),
    path('edit-students/<str:pk>', views.EditStudents, name='edit-students'),
    path('delete-student/<str:pk>', views.DeleteStudent, name='delete-student'),

    path('create_lecturer_profile/', views.AddLecturerProfile, name='create_lecturer_profile'),
    path('edit-lecturer/<str:pk>', views.EditLecturer, name='edit-lecturer'),
    path('delete-lecturer/<str:pk>', views.DeleteLecturer, name='delete-lecturer'),
    
    path('add-faculty/', views.AddFaculty, name='add-faculty'),
    path('edit-faculty/<str:pk>', views.EditFaculty, name='edit-faculty'),
    path('delete-faculty/<str:pk>', views.DeleteFaculty, name='delete-faculty'),
    path('list-faculty/', views.ListFaculty, name='list-faculty'),

    path('add_gender/', views.AddGender, name='add_gender'),
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

    path('unit_registration1/', my_views.unit_registration, name='unit_registration1'),
    path('unregister_unit1/<str:pk>', my_views.unregister_unit1, name='unregister_unit1'),
    path('insert_marks/<str:pk>', my_views.insert_marks, name='insert_marks'),
    path('list_registered_units1/', my_views.list_registered_units1, name='list_registered_units1'),
    path('my_registered_units1/', my_views.my_registered_units1, name='my_registered_units1'),

    path('unit_registration2/', my_views.unit_registration2, name='unit_registration2'),
    path('unregister_unit2/<str:pk>', my_views.unregister_unit2, name='unregister_unit2'),
    path('insert_marks2/<str:pk>', my_views.insert_marks2, name='insert_marks2'),
    path('list_registered_units2/', my_views.list_registered_units2, name='list_registered_units2'),
    path('my_registered_units2/', my_views.my_registered_units2, name='my_registered_units2'),

    path('unit_registration3/', my_views.unit_registration3, name='unit_registration3'),
    path('unregister_unit3/<str:pk>', my_views.unregister_unit3, name='unregister_unit3'),
    path('insert_marks3/<str:pk>', my_views.insert_marks3, name='insert_marks3'),
    path('list_registered_units3/', my_views.list_registered_units3, name='list_registered_units3'),
    path('my_registered_units3/', my_views.my_registered_units3, name='my_registered_units3'),

    path('unit_registration4/', my_views.unit_registration4, name='unit_registration4'),
    path('unregister_unit4/<str:pk>', my_views.unregister_unit4, name='unregister_unit4'),
    path('insert_marks4/<str:pk>', my_views.insert_marks4, name='insert_marks4'),
    path('list_registered_units4/', my_views.list_registered_units4, name='list_registered_units4'),
    path('my_registered_units4/', my_views.my_registered_units4, name='my_registered_units4'),

    path('unit_registration5/', my_views.unit_registration5, name='unit_registration5'),
    path('unregister_unit5/<str:pk>', my_views.unregister_unit5, name='unregister_unit5'),
    path('insert_marks5/<str:pk>', my_views.insert_marks5, name='insert_marks5'),
    path('list_registered_units5/', my_views.list_registered_units5, name='list_registered_units5'),
    path('my_registered_units5/', my_views.my_registered_units5, name='my_registered_units5'),

    path('unit_registration6/', my_views.unit_registration6, name='unit_registration6'),
    path('unregister_unit5/<str:pk>', my_views.unregister_unit6, name='unregister_unit6'),
    path('insert_marks6/<str:pk>', my_views.insert_marks6, name='insert_marks6'),
    path('list_registered_units6/', my_views.list_registered_units6, name='list_registered_units6'),
    path('my_registered_units6/', my_views.my_registered_units6, name='my_registered_units6'),

    path('unit_registration7/', my_views.unit_registration7, name='unit_registration7'),
    path('unregister_unit7/<str:pk>', my_views.unregister_unit7, name='unregister_unit7'),
    path('insert_marks7/<str:pk>', my_views.insert_marks7, name='insert_marks7'),
    path('list_registered_units7/', my_views.list_registered_units7, name='list_registered_units7'),
    path('my_registered_units7/', my_views.my_registered_units7, name='my_registered_units7'),

    path('FeeReceiptList/', views2.FeeReceiptList, name='FeeReceiptList'),

    path('register_special_exam/', views2.register_special_exams, name='register_special_exam'),
    path('my_special_exams/', views2.my_special_exams, name='my_special_exams'),
    path('special_exams_marks/<str:pk>', views2.special_exams_marks, name='special_exams_marks'),
    path('delete_special_exams/<str:pk>', views2.delete_special_exams, name='delete_special_exams'),
    path('SpecialExamList/', views2.SpecialExamList, name='SpecialExamList'),
    
    path('create_edit_lecturer_units/', views2.add_lecturer_units, name='create_edit_lecturer_units'),
    path('lecturer_units_edit/<str:pk>', views2.lecturer_units_edit, name='lecturer_units_edit'),
    path('lecturer_units_delete/<str:pk>', views2.lecturer_units_delete, name='lecturer_units_delete'),
    path('ListAllLecturerUnits/', views2.ListAllLecturerUnits, name='ListAllLecturerUnits'),

    path('add_seats/', views2.seats, name='add_seats'),
    path('list_seats/', views2.list_seats, name='list_seats'),
    path('seats_edit/<str:pk>', views2.seats_edit, name='seats_edit'),
    path('seats_delete/<str:pk>', views2.seats_delete, name='seats_delete'),

    path('add_notice/', views2.add_notice, name='add_notice'),
    path('delete_notice/<str:pk>', views2.delete_notice, name='delete_notice'),
    path('list_notices/', views2.list_notices, name='list_notices'),
    
    path('register_polititian/', views2.register_polititian, name='register_polititian'),
    path('edit_polititian/<str:pk>', views2.edit_polititian, name='edit_polititian'),
    path('delete_polititian/<str:pk>', views2.delete_polititian, name='delete_polititian'),
    path('list_politicians/', views2.list_politicians, name='list_politicians'),

    path('add_suggestion/', views2.add_suggestion, name='add_suggestion'),
    path('delete_suggestion/<str:pk>', views2.delete_suggestion, name='delete_suggestion'),
    path('list_suggestions/', views2.list_suggestions, name='list_suggestions'),

    # pages
    path('my_reg_units_year_page/', views2.my_reg_units_year_page, name='my_reg_units_year_page'),
    path('list_marks_year_page/', views2.list_marks_year_page, name='list_marks_year_page'),
    path('my_resit_year_page/', views2.my_resit_year_page, name='my_resit_year_page'),
    path('list_resit_year_page/', views2.list_resit_year_page, name='list_resit_year_page'),

    # admin pages
    path('all_users/', views.all_users, name='all_users'),
    path('all_students/', views.all_students, name='all_students'),
    path('all_lecturers/', views.all_lecturers, name='all_lecturers'),
    path('all_fee_payment/', views.all_fee_payment, name='all_fee_payment'),
    path('all_fee_receipts/', views.all_fee_receipts, name='all_fee_receipts'),

    # public notices
    path('compose_notices/', views2.send_notice, name='compose_notices'),
    path('all_public_notices/', views2.list_notices, name='all_public_notices'),
    path('read_public_notices/<str:pk>', views2.read_notices, name='read_public_notices'),
    path('delete_notice/<str:pk>', views2.delete_notice, name='delete_notice'),

    # paypal
    path('send_payment/', paypal_views.send_payment, name='send_payment'),
    path('process-payment/', paypal_views.process_payment, name='process_payment'),
    path('payment-done/', paypal_views.payment_done, name='payment_done'),
    path('payment-cancelled/', paypal_views.payment_canceled, name='payment_cancelled')
]
