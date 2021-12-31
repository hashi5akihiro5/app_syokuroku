from django import forms
from .models import *

# Register
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

# kcal_Select
class KcalSelectForm(forms.Form):
    data = [
        (1, "500 Kcal"),
        (2, "1000 Kcal"),
        (3, "2000 Kcal"),
    ]
    counts = forms.ChoiceField(label="摂取カロリー", choices=data)

# Mune_Count
class MuneCountForm(forms.Form):
    data = [
        (1, "1 食"),
        (2, "2 食"),
        (3, "3 食"),
        (4, "4 食"),
        (5, "5 食"),
    ]
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