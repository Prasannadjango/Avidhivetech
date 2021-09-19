from django import forms
from.models import Products
from.models import Signup
from.models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductsForm(forms.ModelForm):
	class Meta:
		model = Products
		fields = ['Product_id','Product_name','Product_price','Product_manufacturer','Product_image']

class SignupForm(forms.ModelForm):
	class Meta:
		model = Signup
		fields = ['Name','Mailid','Contactnumber','Location']


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['Fullname','Location','Contactnumber','Emailid','Shippingaddress','Nearbylandmark']



class RegisterUserForm(UserCreationForm):

	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:

		model = User

		fields = ['username','first_name','last_name','email','password1','password2']

	def __init__(self,*args,**kwargs):

		super(RegisterUserForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

