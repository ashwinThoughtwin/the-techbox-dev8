from django import forms
from .models import Employee, Team, Item,Catagory,AssignItem

class EmployeeForm(forms.ModelForm):  
    class Meta:
        model = Employee
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'team': forms.Select(attrs={'class':'form-control'}),
            'mobile' : forms.TextInput(attrs={'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'number','class':'form-control'}), 
            'address' : forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
       }
        fields = "__all__"
         

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team'].queryset = Team.objects.all()

class ItemForm(forms.ModelForm):  
    class Meta:
        model = Item
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'model_no' : forms.TextInput(attrs={'class':'form-control','placeholder':'Model_no'}),
            'add_date' : forms.TextInput(attrs={'class':'form-control','type':'date'}), 
            'catagory' : forms.Select(attrs={'class':'form-control'}),
            # 'employee' : forms.Select(attrs={'class':'form-control'}),
       }
        fields = "__all__"
         

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['catagory'].queryset = Catagory.objects.all()
        # self.fields['employee'].queryset = Employee.objects.all()

class TeamForm(forms.ModelForm):  
    class Meta:
        model = Team
        widgets = {
            'designation' : forms.TextInput(attrs={'class':'form-control','placeholder':'designation'}),
            #'add_date' : forms.TextInput(attrs={'class':'form-control','type': 'date'}),
            
            
       }
        fields = "__all__"

    
class CatagoryForm(forms.ModelForm):  
    class Meta:
        model = Catagory
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            #'add_date' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            
        }

        fields = "__all__"

   
    

class AssignGadgetForm(forms.ModelForm):
    class Meta:
        model = AssignItem
        widgets = {
            'employee' : forms.Select(attrs={'class':'form-control'}),
            'item' : forms.Select(attrs={'class':'form-control'}),
            'expire_date' : forms.TextInput(attrs={'class':'form-control','type': 'date'}),
            # 'status'    :forms.TextInput(attrs={'class':'form-control'}),
       }
        fields = "__all__"
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['item'].queryset =Item.objects.all()
            self.fields['employee'].queryset = Employee.objects.all()

# class ItemForm(forms.ModelForm):  
#     class Meta:
#         model = Item
#         widgets = {
#             'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
#             'model_no' : forms.TextInput(attrs={'class':'form-control','placeholder':'Model_no'}),
#             'status':    forms.BooleanField(attrs={'class':'form-control'}),
#             'add_date' : forms.TimeField(attrs={'class':'form-control'}), 
#             'catagory' : forms.Select(attrs={'class':'form-control'}),
#             'employee' : forms.Select(attrs={'class':'form-control'}),
#        }
#         fields = "__all__"
         

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['catagory'].queryset = Catagory.objects.all()
#         self.fields['employee'].queryset = Employee.objects.all()    

# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder" : "Username",                
#                 "class": "form-control"
#             }
#         ))
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder" : "Password",                
#                 "class": "form-control"
#             }
#         ))

# class SignUpForm(forms.ModelForm):

    
#     class Meta:
#         model = Employee
#         fields = ['name','team','address','email','mobile']

#     def clean_mobile(self):
#         mobile = self.cleaned_data.get('mobile')
#         try:
#             match = Emp.objects.get(mobile=mobile)
#         except Emp.DoesNotExist:
#             return mobile
#         raise forms.ValidationError('This mobile number is already in use.')