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
