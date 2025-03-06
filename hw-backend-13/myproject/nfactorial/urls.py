from django.urls import path

from .views import home, add, upper

urlpatterns = [
    path('', home),
    path('<int:first>/add/<int:second>/', add),
    path('transform/<str:text>/', upper),
]
