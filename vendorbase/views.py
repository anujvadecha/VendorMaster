from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from order_engine.order_engine import OrderEngine


class IndexTemplateView(LoginRequiredMixin,TemplateView):

    def get_template_names(self):
        template_name="index.html"
        return template_name

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def startOrderEngine(request):
    cache.set("orderEngine",OrderEngine.getInstance())
    OrderEngine.getInstance().set_var("order engine started by admin")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])