"""User views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView

# Forms
from users.forms import ProfileForms, SignupForm

# Model
from django.contrib.auth.models import User
from posts.models import Post 

class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context
   
@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
          
   
        form = ProfileForms(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            if data['picture']:
                profile.picture = data['picture']
            profile.save()
            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)
    else:
        form = ProfileForms()        
    return render(
        request,
        'users/update_profile.html',
        context={
            'form':form
        }
    )
  
def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('posts:feed')
        else:

            return render(request, 'users/login.html')

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    
    return render(
        request=request,
        template_name='users/signup.html',
        context={
            'form':form
        }
    )

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

