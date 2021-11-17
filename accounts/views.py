from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView
from .forms import CustomUserCreationForm, ProfilePageForm
from .models import Profile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserEditView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['platform']
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile

    
class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_object(self):
        return self.request.user


class HomePageView(TemplateView):
    template_name = 'home.html'