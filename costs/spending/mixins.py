from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

class AuthorAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.is_authenticated:
            if request.user != self.get_object().author or request.user.is_staff:
                messages.error(request, 'Изменение и удаление задачи доступно только автору')
                return redirect(reverse_lazy('main'))
        return super().dispatch(request, *args, **kwargs)