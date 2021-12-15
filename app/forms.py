from django import forms
from .models import Post, ParentCategory

class PostCreateForm(forms.ModelForm):
    # 親カテゴリーの選択欄がないと絞り込めないので定義する。
    parete_category = forms.ModelChoiceField(
        label='主食・副食・飲み物',
        queryset=ParentCategory.objects,
        required=False 
    )

    class Meta:
        model = Post
        fields = '__all__'

    field_order = ('meal_no', 'parente_category', 'category')