from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView 
from django.http import HttpResponse
from cbvapp.models import school,student
from django.urls import reverse_lazy

# Create your views here.
# class myclass(View):
#     def get(self,request):
#         return HttpResponse("<h1>this is cbv project</h1>")

class mytemplate(TemplateView):
    template_name = "index.html"

class school_list(ListView):
    model = school

class school_details(DetailView):
    context_object_name = "school_details"
    model = school

class schoolcreate(CreateView):
    model = school
    fields = "__all__"

class update(UpdateView):
    model = school 
    fields = ["school_name","principal"]

class school_delete(DeleteView):
    model = school
    success_url = reverse_lazy("list")
    

    