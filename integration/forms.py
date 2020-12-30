from django.forms import ModelForm
from django import forms
from flutterwave.models import FlwPlanModel,FlwPlanModel1,FlwTransactionModel

class PlanForm(ModelForm):
	class Meta:
		model = FlwPlanModel
		fields = '__all__'
class PlansForm(ModelForm):
	class Meta:
		model = FlwPlanModel1
		fields = '__all__'
class TransForm(ModelForm):
	class Meta:
		model = FlwTransactionModel
		fields ='__all__'