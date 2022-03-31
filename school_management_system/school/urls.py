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

    
    path('create_edit_lecturer_units/', views2.add_lecturer_units, name='create_edit_lecturer_units'),
    path('lecturer_units_edit/<str:pk>', views2.lecturer_units_edit, name='lecturer_units_edit'),
    path('lecturer_units_delete/<str:pk>', views2.lecturer_units_delete, name='lecturer_units_delete'),
    path('ListAllLecturerUnits/', views2.ListAllLecturerUnits, name='ListAllLecturerUnits'),

    path('add_seats/', views2.seats, name='add_seats'),
    path('list_seats/', views2.list_seats, name='list_seats'),
    path('seats_edit/<str:pk>', views2.seats_edit, name='seats_edit'),
    path('seats_delete/<str:pk>', views2.seats_delete, name='seats_delete'),
    
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
    path('exam_results_page/', views2.exam_results_page, name='exam_results_page'),

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
    path('payment-cancelled/', paypal_views.payment_canceled, name='payment_cancelled'),

    # Resits/Retakes
    path('resit_reg_year1/', views2.resit_reg_year1, name='resit_reg_year1'),
    path('unregister_resit_yr1/<str:pk>', views2.unregister_resit_yr1, name='unregister_resit_yr1'),
    path('list_registered_resits1/', views2.list_registered_resits1, name='list_registered_resits1'),
    path('my_registered_resits_yr1/', views2.my_registered_resits_yr1, name='my_registered_resits_yr1'),

    path('resit_reg_year2/', views2.resit_reg_year2, name='resit_reg_year2'),
    path('unregister_resit_yr2/<str:pk>', views2.unregister_resit_yr2, name='unregister_resit_yr2'),
    path('list_registered_resits2/', views2.list_registered_resits2, name='list_registered_resits2'),
    path('my_registered_resits_yr2/', views2.my_registered_resits_yr2, name='my_registered_resits_yr2'),
    
    path('resit_reg_year3/', views2.resit_reg_year3, name='resit_reg_year3'),
    path('unregister_resit_yr3/<str:pk>', views2.unregister_resit_yr3, name='unregister_resit_yr3'),
    path('list_registered_resits3/', views2.list_registered_resits3, name='list_registered_resits3'),
    path('my_registered_resits_yr3/', views2.my_registered_resits_yr3, name='my_registered_resits_yr3'),
    
    path('resit_reg_year4/', views2.resit_reg_year4, name='resit_reg_year4'),
    path('unregister_resit_yr4/<str:pk>', views2.unregister_resit_yr4, name='unregister_resit_yr4'),
    path('list_registered_resits4/', views2.list_registered_resits4, name='list_registered_resits4'),
    path('my_registered_resits_yr4/', views2.my_registered_resits_yr4, name='my_registered_resits_yr4'),
    
    path('resit_reg_year5/', views2.resit_reg_year5, name='resit_reg_year5'),
    path('unregister_resit_yr5/<str:pk>', views2.unregister_resit_yr5, name='unregister_resit_yr5'),
    path('list_registered_resits5/', views2.list_registered_resits5, name='list_registered_resits5'),
    path('my_registered_resits_yr5/', views2.my_registered_resits_yr5, name='my_registered_resits_yr5'),
    
    path('resit_reg_year6/', views2.resit_reg_year6, name='resit_reg_year6'),
    path('unregister_resit_yr6/<str:pk>', views2.unregister_resit_yr6, name='unregister_resit_yr6'),
    path('list_registered_resits6/', views2.list_registered_resits6, name='list_registered_resits6'),
    path('my_registered_resits_yr6/', views2.my_registered_resits_yr6, name='my_registered_resits_yr6'),
    
    path('resit_reg_year7/', views2.resit_reg_year7, name='resit_reg_year1'),
    path('unregister_resit_yr7/<str:pk>', views2.unregister_resit_yr7, name='unregister_resit_yr7'),
    path('list_registered_resits7/', views2.list_registered_resits7, name='list_registered_resits7'),
    path('my_registered_resits_yr7/', views2.my_registered_resits_yr7, name='my_registered_resits_yr7'),
    # End of Resit/Retake URLs

    # Print Exam Card URLs
    path('exam_card_yr1/', my_views.exam_card_yr1, name='exam_card_yr1'),
    path('exam_card_yr2/', my_views.exam_card_yr2, name='exam_card_yr2'),
    path('exam_card_yr3/', my_views.exam_card_yr3, name='exam_card_yr3'),
    path('exam_card_yr4/', my_views.exam_card_yr4, name='exam_card_yr4'),
    path('exam_card_yr5/', my_views.exam_card_yr5, name='exam_card_yr5'),
    path('exam_card_yr6/', my_views.exam_card_yr6, name='exam_card_yr6'),
    path('exam_card_yr7/', my_views.exam_card_yr7, name='exam_card_yr7'),

    # Print Resit/Retake Card URLs
    path('resit_card_yr1/', views2.resit_card_yr1, name='resit_card_yr1'),
    path('resit_card_yr2/', views2.resit_card_yr2, name='resit_card_yr2'),
    path('resit_card_yr3/', views2.resit_card_yr3, name='resit_card_yr3'),
    path('resit_card_yr4/', views2.resit_card_yr4, name='resit_card_yr4'),
    path('resit_card_yr5/', views2.resit_card_yr5, name='resit_card_yr5'),
    path('resit_card_yr6/', views2.resit_card_yr6, name='resit_card_yr6'),
    path('resit_card_yr7/', views2.resit_card_yr7, name='resit_card_yr7'),

    #Print Resuts slip
    path('results_slip_year1/', my_views.results_slip_year1, name='results_slip_year1'),
    path('results_slip_year2/', my_views.results_slip_year2, name='results_slip_year2'),
    path('results_slip_year3/', my_views.results_slip_year3, name='results_slip_year3'),
    path('results_slip_year4/', my_views.results_slip_year4, name='results_slip_year4'),
    path('results_slip_year5/', my_views.results_slip_year5, name='results_slip_year5'),
    path('results_slip_year6/', my_views.results_slip_year6, name='results_slip_year6'),
    path('results_slip_year7/', my_views.results_slip_year7, name='results_slip_year7'),

    # school fee structure
    path('create_fee_structure/', my_views.create_fee_structure, name='create_fee_structure'),
    path('update_fee_structure/<str:pk>', my_views.update_fee_structure, name='update_fee_structure'),
    path('delete_fee_structure/<str:pk>', my_views.delete_fee_structure, name='delete_fee_structure'),
    path('list_fee_structure/', my_views.list_fee_structure, name='list_fee_structure'),
    path('print_fee_structure/', my_views.print_fee_structure, name='print_fee_structure'),

    # fee_payments
    path('pay_fee/', views2.pay_fee, name='pay_fee'),
    path('update_fee_payment/<str:pk>', views2.update_fee_payment, name='update_fee_payment'),
    path('delete_fee_payment/<str:pk>', views2.delete_fee_payment, name='delete_fee_payment'),
    path('fee_payment_records/', views2.fee_payment_records, name='fee_payment_records'),
    # salary payments

]
