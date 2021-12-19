from django.urls import path
from .views import student_delete
# from .views import home,student_list, student_add, student_detail, student_update,student_delete
from .views import HomeView , StudentListView , StudentDetailView , StudentCreateView , StudentUpdateView

urlpatterns = [
    # path('', home, name="home"),
    path('' , HomeView.as_view() , name='home'),
    
    # path('student_list/', student_list, name="list"),
    path('student_list/', StudentListView.as_view(), name="list"),
    
    # path('detail/<int:id>/', student_detail, name="detail"),
    path('student_detail/<int:id>/' , StudentDetailView.as_view(), name = "detail"),
    
    # path('student_add/', student_add, name="add"),
    path('student_add/' , StudentCreateView.as_view(), name = "add"),
    
    # path('update/<int:id>/', student_update, name="update"),
    path('update/<int:id>/', StudentUpdateView.as_view()    , name="update"),
    
    
    path('delete/<int:id>/', student_delete, name="delete"),
]