from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


class RightUserMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Необходимо войти')
            return self.handle_no_permission()
        if request.user.is_authenticated:
            id = kwargs['pk']
            if request.user.id != id:
                messages.error(request, 'Нет прав доступа')
                return redirect(reverse_lazy('users:login'))
        return super().dispatch(request, *args, **kwargs)