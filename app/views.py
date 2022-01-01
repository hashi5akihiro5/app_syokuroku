from django.forms import fields
from django.shortcuts import redirect, render
from django.views import generic, View
from django.shortcuts import resolve_url

from .models import *
from .forms import *


class IndexView(View):
    def __init__(self):
        profile_data = Profile.objects.all()
        self.params = {
            'profile_data': profile_data.order_by("-id")[0],
            'kcalselectform': KcalSelectForm(),
            'form': MuneCreateForm(),
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

# class MuneCreateView(generic.CreateView):
#     model = Post
#     form_class = MuneCreateForm
#     success_url = '/'# reverse_lazy等のほうが良い。これは手抜き

#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         context['parent_categorys'] = ParentCategory.objects.all()
#         return render('app/munecreate.html', context)

    # def get_success_url(self):
    #     return resolve_url('apps:index', pk=self.object.pk)


# class PostCreate(generic.CreateView):
#     model = Post
#     form_class = ParentCategoryChoice
#     success_url = '/'# reverse_lazy等の方が良い。これは手抜き

#     # これが追加
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['parentcategory_list'] = ParentCategory.objects.all()
#         return context
    
# def home_view(request):
#     if request.method == 'GET':
#         return render(request, 'app/index.html', {
#             'form': ParentCategoryForm(),
#         })
#     elif request.method == 'POST':
#         form = ParentCategoryForm(request.POST)
#         if not form.is_valid():
#             return render(request, 'myapp/home.html', {
#                 'form': form
#             })
#         fields = form.cleaned_data['name']
#         return render(request, 'app/index.html', {
#             'form': ParentCategoryForm(),
#         })
