from django.forms import fields
from django.shortcuts import redirect, render
from django.views import generic, View
from django.shortcuts import resolve_url

from .models import *
from .forms import *


class IndexView(View):
    def __init__(self):
        profile_data = Profile.objects.all()
        formset = PostCreateFormSet()
        self.params = {
            'profile_data': profile_data.order_by("-id")[0],
            'kcalselectform': KcalSelectForm(),
            'form': MuneCreateForm(),
            'formset': formset
        }

    def get(self, request):
        return render(request, 'app/index.html', self.params)

    def post(self, request):
        munecount = request.POST['counts']

# Register
def register(request):
    if (request.method == 'POST'):
        obj = Profile()
        register_data = RegisterForm(request.POST, instance=obj)
        register_data.save()
        return redirect(to='/app')
    params = {
        'form': RegisterForm(),
    }
    return render(request, 'app/register.html', params)

