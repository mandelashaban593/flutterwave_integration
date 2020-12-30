# stdlib imports

# django imports
from django.views.generic import TemplateView

# 3rd party imports

# project imports
from flutterwave.models import FlwPlanModel,FlwPlanModel1,FlwTransactionModel
from django.shortcuts import render
from .forms import PlanForm,PlansForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.shortcuts import render,redirect,get_object_or_404

def plan(request):
    context={
        "plans":FlwPlanModel.objects.all(),
        "naturals":FlwPlanModel1.objects.all()
  
    }
    return render(request, "integration/signup1.html",context)
def login_view(request):
    if request.method == "GET":
        return render(request, "integration/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('/')
        else:
            return render(request, "integration/login.html", {"message": "Invalid credentials."})


def uganda(request):
    context={
        "naturals":FlwPlanModel1.objects.all()
    }
    return render(request, "integration/display.html",context)

def createplan(request,pk):
    plan = FlwPlanModel.objects.get(id=pk)
    form = PlanForm(instance=plan)
    if request.method == 'POST':
       form = PlanForm(request.POST, instance=plan)
       if form.is_valid():
          form.save()
          return redirect('/')
    context = {
     "form":form
    }
    return render(request,"integration/update.html",context)


def create_plan(request,pk):
    natural= FlwPlanModel1.objects.get(id=pk)
    p_form = PlansForm(instance=natural)
    if request.method == 'POST':
       p_form = PlanForm(request.POST, instance=natural)
       if p_form.is_valid():
          p_form.save()
          return redirect('/')
    context = {
     "p_form":p_form
    }
    return render(request,"integration/update1.html",context)