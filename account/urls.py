from django.urls import path
from . import views

urlpatterns = [
    # login / logout urls
    # path('login/', views.user_login, name='login'), # path for user login page: 1st way
    path('login/', views.LoginView.as_view(), name='login'),  # path for user login page: 2nd way
    path('logout/', views.LogoutView.as_view(), name='logout'),  # path for user log out page

    # change password urls
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),  # path for user change password page
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),  # path for user change password done page

    # reset-password urls
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # register url
    path('register/', views.register, name='register'),

    path('', views.dashboard, name='dashboard'),  # path for user dashboard page
]
