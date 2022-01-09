from django.shortcuts import redirect, render
from django.views import View
from .models import *
from .forms import *
from .mixins import BaseCalendarMixin, MonthCalendarMixin


class IndexView(View):
    def __init__(self):
        profile_data = Profile.objects.all()
        self.params = {
            'profile_data': profile_data.order_by("-id")[0],
            'kcalselectform': KcalSelectForm(),
            'form': MuneCreateForm(),
            'formset': PostCreateFormSet(),
            'month_calendar': MonthCalendarMixin().get_month_calendar,
        }

    def get(self, request):
        return render(request, 'app/index.html', self.params)

    def post(self, request):
        self.params['kcalselectform'] = KcalSelectForm(request.POST)
        self.params['form'] = MuneCreateForm(request.POST)
        self.params['formset'] = PostCreateFormSet(request.POST)
        return render(request, 'app/index.html', self.params)

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

