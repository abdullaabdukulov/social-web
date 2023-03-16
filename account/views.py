from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from actions.utils import create_action
from .models import UserProfile, Contact
from .forms import LoginForm, UserRegisterForm, UserProfileEditForm, UserEditForm
from django.contrib.auth import views


def user_login(request):
    """
    View function for user login

    Accepts POST requests with valid user credentials, authenticates the user,
    and logs the user in if they are active.

    Args:
        request: HTTP request object

    Returns:
        HTTP response with success or error message
    """

    if request.method == 'POST':
        # If the form was submitted
        form = LoginForm(request.POST)

        if form.is_valid():
            # If the form data is valid
            cd = form.cleaned_data

            # If authentication the user
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'],
                                )

            if user is not None:
                # If authentication was successful
                if user.is_active:
                    # if the user account is active, log them in
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    # If the user account is disabled
                    return HttpResponse('Disable account')
            else:
                # If authentication failed
                return HttpResponse('Invalid login')
    else:
        # If the form was not submitted, create a new form
        form = LoginForm()

    # render the login page with the form
    return render(request, 'account/login.html', {'form': form})


class LoginView(views.LoginView):
    template_name = 'account/login.html'

    # Redirect to home page
    def get_success_url(self):
        return reverse_lazy('dashboard')


class LogoutView(views.LogoutView):
    template_name = 'account/logout.html'


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


class PasswordChangeView(views.PasswordChangeView):
    template_name = 'account/edit_password.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'account/edit_password_done.html'


class PasswordResetView(views.PasswordResetView):
    template_name = 'account/password_reset.html'


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            UserProfile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegisterForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = UserProfileEditForm(
            instance=request.user.userprofile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(
            instance=request.user.userprofile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    print(user_list)
    return render(request,
                  'account/user/list.html',
                  {'section': 'people',
                   'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username=username,
                             is_active=True)
    return render(request,
                  'account/user/detail.html',
                  {'section': 'people',
                   'user': user})


@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                    user_from=request.user,
                    user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user,
                                       user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})
