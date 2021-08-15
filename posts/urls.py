
from django.conf.urls import url
from django.urls import path
from posts.views import index, hi, dog_registration

urlpatterns = [
    path('', index, name=''),
    path('dog-registration', dog_registration, name='dog-registration'),
    path('hi', hi, name='hi'),

]
