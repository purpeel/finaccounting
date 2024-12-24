from django.shortcuts import render
from django.views import View

class IndexMainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')