from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import (
    CreateUser, UpdateUser, DeleteUser,
    LoginUser, LogoutUser, ProfileUser,
    ResetPasswordView
)

app_name = "accounts"

urlpatterns = [
    path('', ProfileUser.as_view(), name= 'home_user'),
    path('create/', CreateUser.as_view(), name='create_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', LogoutUser.as_view(), name='logout_user'),
    path('update/', UpdateUser.as_view(), name='update_user'),
    path('delete/', DeleteUser.as_view(), name='delete_user'),
    path('change-password/',auth_views.PasswordChangeView.as_view(
            template_name='accounts/change_password.html',
            success_url = reverse_lazy('accounts:home_user')
        ),
        name='change_password'
    ),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url=reverse_lazy("accounts:password_reset_complete")
            ),
            name='password_reset_confirm'
        ),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'),
]