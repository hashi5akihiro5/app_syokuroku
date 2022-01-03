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

# Mune
class MuneCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


# モデルフォームセット
PostCreateFormSet = forms.modelformset_factory(
    Post, form=MuneCreateForm, extra=0
)


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