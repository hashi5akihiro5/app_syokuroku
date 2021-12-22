from django import forms
from .models import ParentCategory, MainCategory, SubCategory, DrinkCategory

# 親カテゴリー
# カテゴリー種類:主食・副食・飲み物
class ParentCategoryForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=ParentCategory.objects, label="主食・副食・飲み物")
    # class Meta:
    #     model = ParentCategory
    #     fields = ['name']


# 子カテゴリー
# 主食
class MainCategoryForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=MainCategory.objects, label="主食")

# 副食
class SubCategory(forms.Form):
    choice = forms.ModelChoiceField(queryset=SubCategory.objects, label="副食")

# 飲み物
class DrinkCategory(forms.Form):
    choice = forms.ModelChoiceField(queryset=DrinkCategory.objects, label="飲み物")