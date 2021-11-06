from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View, DetailView, CreateView, FormView, UpdateView
from user.models import User
from user.forms import RegisterUserForm, LoginForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = 'http://localhost:8000/user/login/'


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/dashboard/'

    def form_valid(self, form):
        email = self.request.POST['email']
        password = self.request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(self.request, user)

        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('http://localhost:8000/user/login/')


class ProfileView(DetailView):
    template_name = 'user/profile.html'
    queryset = User.objects.all()


@method_decorator(login_required(login_url='/user/login/'), name='dispatch')
class PasswordChangeView(UpdateView):
    template_name = 'user/change_password.html'
    form_class = ChangePasswordForm
    success_url = '/dashboard/'
    queryset = User.objects.all()

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.id != self.request.user.id:
            raise Http404('You\'re not allowed to view this profile!')
        return super(PasswordChangeView, self).dispatch(request, *args, **kwargs)



