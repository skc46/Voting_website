# -*- coding: utf-8 -*-
from django.urls import path

from .views import (index, detail, results, vote) 

app_name = 'polls'  # this is helpful to navigate to URLs called Namespacing URL names

urlpatterns = [
           path('', index, name='index_view'),
           path('<int:question_id>/', detail, name='detail'),
           path('<int:question_id>/results/', results, name='results'),
           path('<int:question_id>/vote/', vote, name='vote'),
           
           ]