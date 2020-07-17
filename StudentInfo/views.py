from django.shortcuts import render
from .models import StudentInfo
from .forms import StudentAddForm

def student_list(request):
    studentinfo = StudentInfo.objects.all()
    context = {
        'student_info': studentinfo,
    }

    return render(request,'blog/post_list_new.html', context)