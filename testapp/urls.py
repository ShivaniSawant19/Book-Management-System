from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.home_page),
    path('register/', views.register),
    path('list/', views.student_list),
    path('updaterecord/<int:id>/', views.update_record),
    path('deleterecord/<int:id>/', views.delete_record),
    path('create_account/',views.create_account)

]