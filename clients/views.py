from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class ClientLoginView(LoginView):

    template_name = "form.html"
    next_page = reverse_lazy("list_product")


class ClientLogoutView(LogoutView):
    next_page = reverse_lazy("login")
