from atexit import register
from django.urls import path
from register import views
from register.views import ThanksTemplateView, TeacherCreateView, TeacherListview, TeacherDetailview, TeacherUpdateView, TeacherDeleteView


app_name = 'register'

urlpatterns = [
    path('', views.home_views, name = 'home'),
    path('thank_you/', ThanksTemplateView.as_view(), name = 'thanks'),
    path('teacher-form/', TeacherCreateView.as_view(), name = 'teacher_form'),
    path('teacher-list/', TeacherListview.as_view(), name = 'teacher_list'),
    path('register/teacher-detail/<int:pk>', TeacherDetailview.as_view(), name = 'detail_list'),
    path('register/teacher-update/<int:pk>', TeacherUpdateView.as_view(), name = 'update_list'),
    path('register/delete-teacher/<int:pk>', TeacherDeleteView.as_view(), name = 'delete_list'),
]