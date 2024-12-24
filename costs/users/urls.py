from django.urls import path
from costs.users import views

urlpatterns = [path('login/', views.LoginPerson.as_view(), name='login'),
               path('create/', views.CreatePerson.as_view(), name='create'),
               path('logout/', views.logout_user, name='logout'),
               path('<int:pk>/update/', views.PersonUpdate.as_view(), name='update'),
               path('<int:pk>/delete/', views.PersonDelete.as_view(), name='delete'),
               path('<int:pk>/show/', views.PersonShowView.as_view(), name='show')]