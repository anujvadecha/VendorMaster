from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


def fallback_404(request):
    return redirect("/")
# from django.contrib.admin.views.decorators import staff_member_required
#
# @staff_member_required
# def startOrderEngine(request):
#     cache.set("orderEngine",OrderEngine.getInstance())
#     OrderEngine.getInstance().set_var("order engine started by admin")
#     return HttpResponseRedirect(request.META["HTTP_REFERER"])