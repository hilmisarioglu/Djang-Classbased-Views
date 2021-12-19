from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
from django.views.generic import TemplateView , ListView , DetailView , CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = "app/home.html"

class StudentListView(ListView):
    model = Student
    # default template name : # app/modelname_list.html
    # this fits our template name no need to use this time
    # template_name = "app/student_list.html"
    context_object_name = 'students' # default context name : object_list
    paginate_by = 10

class StudentDetailView(DetailView):
    model = Student
    pk_url_kwarg = 'id'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'app/student_add.html'
    success_url = reverse_lazy('list')

class StudentUpdateView(UpdateView):
    model = Student
    pk_url_kwarg = 'id'
    form_class = StudentForm
    template_name = 'app/student_update.html'
    success_url = reverse_lazy('list')
    
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'app/student_delete.html'
    success_url = reverse_lazy('list')
    pk_url_kwarg = 'id'
