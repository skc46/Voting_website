# -*- coding: utf-8 -*-
from django.urls import path

#from .views import (index, detail, results, vote) 
from . import views    # for generic views

app_name = 'polls'  # this is helpful to navigate to URLs called Namespacing URL names
# If app_name has defined then in template while hyperlinkig
# {% url  app_name:urlname%}
# urlpatterns = [
#            path('', index, name='index'),
#            path('<int:question_id>/', detail, name='detail'),
#            path('<int:question_id>/results/', results, name='results'),
#            path('<int:question_id>/vote/', vote, name='vote'),
           
#            ]

""" To use class based views (which is more generic views), we change the 
URLoatterns"""

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    ]