from django import forms
from .models import *

# Register
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

# MuneCount
class MuneCountForm(forms.Form):
    data = list((x, x) for x in range(1, 6))
    counts = forms.ChoiceField(label="食事回数", choices=data)

# Mune
class MuneCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


# # 子カテゴリー
# # 主食
# class MainCategoryForm(forms.Form):
#     choice = forms.ModelChoiceField(queryset=MainCategory.objects, label=MainCategory.objects)
    
#     class Meta:
#         model = ParentCategory
#         fields = ['name']


# # 副食
# class SubCategory(forms.Form):
#     choice = forms.ModelChoiceField(queryset=SubCategory.objects, label="副食")

# # 飲み物
# class DrinkCategory(forms.Form):
#     choice = forms.ModelChoiceField(queryset=DrinkCategory.objects, label="飲み物")