from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ParentCategoryForm, MainCategoryForm, SubCategory, DrinkCategory



class IndexView(View):
    def __init__(self):
        profile_data = Profile.objects.all()
        self.params = {
            'profile_data': profile_data.order_by("-id")[0],
            'parentcategoryform': ParentCategoryForm(),
            'maincategoryform': MainCategoryForm(),
            'subcategory': SubCategory(),
            'drinkcategory': DrinkCategory()
        }

    def get(self, request):
        return render(request, 'app/index.html', self.params)


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
