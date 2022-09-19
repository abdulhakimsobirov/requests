from django.urls import path
from .views import (user_login, menu, requests, objects, brigadirs, base,
                         update_brigadirs, update_objects, update_requests,
                          create_brigadirs, create_objects, create_requests,
                          delete_request)


urlpatterns = [
    path('', user_login, name='login'),
    path('base/', base, name='base'),
    
    path('menu/', menu, name='menu'),
    path('requests/', requests, name='requests'),
    path('objects/', objects, name='objects'),
    path('brigadirs/', brigadirs, name='brigadirs'),

    path('create_request/', create_requests, name='create_request'),
    path('create_object/', create_objects, name='create_object'),
    path('create_brigadir/', create_brigadirs, name='create_brigadir'),

    path('update_request/<str:rid>/', update_requests, name='update_request'),
    path('update_object/<str:oid>/', update_objects, name='update_object'),
    path('update_brigadir/<str:bid>/', update_brigadirs, name='update_brigadir'),

    path('delete_request/<str:rid>', delete_request, name="delete_request")


]
