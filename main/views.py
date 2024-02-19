from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
from typing import Any
from .models import (
    HeaderText, FeatureItem, About, WorkProcess , WorkProcessItem , 
    Row , Team_content , Pricing_Plans , Price , Counter , Blog , Blog_list
)

from .forms import ContactUsForm
from django.core.mail import send_mail
from SoftyPinko.settings import EMAIL_HOST_USER



class HomeListView(ListView):
    template_name = 'index.html'


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        header = HeaderText.objects.first()
        feature_items = FeatureItem.objects.all()
        about_left = About.objects.first() # [0]
        about_right = About.objects.all()[1]
        work_proccess = WorkProcess.objects.first()
        work_proccess_items = WorkProcessItem.objects.all()
        row = Row.objects.first()
        team_content = Team_content.objects.all()
        pricing_plans = Pricing_Plans.objects.first()
        price = Price.objects.all()
        counter = Counter.objects.first()
        blog = Blog.objects.first()
        blog_list = Blog_list.objects.first()


        context = {
            'header':header,
            'feature_items':feature_items,
            'about_left':about_left,
            'about_right':about_right,
            'work_proccess':work_proccess,
            'work_proccess_items':work_proccess_items,
            'row' :row,
            'team_content' :team_content,
            'pricing_plans' :pricing_plans,
            'price' :price,
            'counter' :counter,
            'blog' :blog,
            'blog_list' :blog_list
        }

        return render(request, self.template_name, context=context)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        form = ContactUsForm(request.POST) 

        if form.is_valid():
            email = form.cleaned_data.get('email')
            send_mail(
                recipient_list=[email],
                from_email=EMAIL_HOST_USER,
                subject="SoftyPinko",
                message="We got your feedback, Thanks for attension;)"
            )

            form.save()
        else:
            form = ContactUsForm()

        return redirect('home')
