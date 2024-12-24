from django.urls import path
from costs.income import views


urlpatterns = [
    path('create/', views.IncomeCreateView.as_view(), name='create'),
    path('creat_acc/', views.IncomeAccountCreateView.as_view(), name='create_acc'),
    path('<int:pk>/update/', views.IncomeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.IncomeDeleteView.as_view(), name='delete'),
    path('', views.IndexIncomesView.as_view(), name='index')
]