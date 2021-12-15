from django.views.generic import View
from django.shortcuts import render
from django.views import generic
from .forms import PostCreateForm
from .models import Profile, Post



class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
        })

class PostCreate(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = '/'# reverse_lazy等の方が良い。これは手抜き
