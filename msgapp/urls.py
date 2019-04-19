#! /usr/bin/env python# -*- coding: utf-8 -*-

from django.urls import path
from  . import views

urlpatterns = [
    path('',views.msgproc),
    path('', views.homeproc),
    path('', views.homeproc1),
    path('', views.homeproc2),
    path('', views.pgproc),

]