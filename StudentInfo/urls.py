from django.urls import path
from . views import *


urlpatterns = [
    path('student', student_list, name='student-list'),

]
