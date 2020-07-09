from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
# Create your views here.
from app.forms import *

# RENDERING A HTML FILE BY USING TEMPLATEVIEW

class CBV_templateview(TemplateView):
    template_name='CBV_template.html'


# rendering of html file along with sending context data by using TemplateVIew

class CBV_templateContext(TemplateView):
    template_name='CBV_templatecontext.html'


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context['data']=' Data of TemplateView'
        #context['data1']='second data of Templateview'
        context['form']=Student()
        return context

    def post(self,request):
        form_data=Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))




class CBV_formview(FormView):
    form_class=Student          #in the name of form it will send the data
    template_name='CBV_templatecontext.html'


    def form_valid(self,form):
        data=form.cleaned_data
        return HttpResponse(str(data))



class CBV_FormModel(FormView):
    form_class=TopicForm
    template_name='CBV_FormModel.html'


    def form_valid(self,form):
        form.save()
        return HttpResponse('form data saved successfully')



































    

