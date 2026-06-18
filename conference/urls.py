from django.urls import path

from .views import (
    home,
    register,
    submit_paper,
    dashboard,
    contact_message
)

urlpatterns = [

    path('', home, name='home'),

    path(
        'register/',
        register,
        name='register'
    ),

    path(
        'submit-paper/',
        submit_paper,
        name='submit_paper'
    ),

    path(
    'dashboard/',
    dashboard,
    name='dashboard'
),
path(
    'contact/',
    contact_message,
    name='contact'
),

]

