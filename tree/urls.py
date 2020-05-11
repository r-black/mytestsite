from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tree import views

urlpatterns = [
    path('trees/', views.TreeList.as_view()),
    path('trees/<int:pk>/', views.TreeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)