from django import forms
from .models import *


class MuneCreateForm(forms.ModelForm):
    # 親カテゴリー:主食・副食・飲み物
    parent_category = forms.ModelChoiceField(
        label="主食・副食・飲み物",
        queryset=ParentCategory.objects,
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'

    field_order = ('parent_category', 'main_category', 'sub_category', 'drink_category')


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