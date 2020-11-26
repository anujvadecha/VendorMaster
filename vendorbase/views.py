from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexTemplateView(LoginRequiredMixin,TemplateView):

    def get_template_names(self):
        template_name="index.html"
        return template_name