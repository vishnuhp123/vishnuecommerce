from django.urls import path
from . import views

app_name='searcha_app'
urlpatterns=[
    path('',views.SearchResult,name='SearchResult'),
]