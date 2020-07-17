from django.urls import path
from . views import *


urlpatterns = [
    path('info', student_list, name='student-list'),

]
