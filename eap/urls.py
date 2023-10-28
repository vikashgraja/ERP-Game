"""
URL configuration for eap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from game.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('ins', instructions, name='ins'),

    path('h1', h1, name='h1'),
    path('h1q', h1q, name='h1q'),
    path('h1w', h1w, name='h1w'),
    path('h1t', h1t, name='h1t'),

    path('h2', h2, name='h2'),
    path('h2q', h2q, name='h2q'),
    path('h2w', h2w, name='h2w'),
    path('h2t', h2t, name='h2t'),

    path('h3', h3, name='h3'),
    path('h3q', h3q, name='h3q'),
    path('h3w', h3w, name='h3w'),
    path('h3t', h3t, name='h3t'),

    path('h4', h4, name='h4'),
    path('h4q', h4q, name='h4q'),
    path('h4w', h4w, name='h4w'),
    path('h4t', h4t, name='h4t'),

    path('end', end, name='end'),

    path('t1', test1, name='t1'),
    path('t2', test2, name='t2'),
    path('t3', test3, name='t3'),
    path('t4', test4, name='t4'),
    path('t5', test5, name='t5'),
    path('t6', test6, name='t6'),
    path('t7', test7, name='t7'),
]
