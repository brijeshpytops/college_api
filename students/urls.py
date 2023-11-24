from django.urls import path
from .views import *

urlpatterns = [
    path('', studentList, name='studentList'),
    path('student/<int:id>', studentDetails, name='studentDetails'),
]