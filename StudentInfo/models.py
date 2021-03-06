from django.db import models

class StudentInfo(models.Model):
    name = models.CharField(max_length=150)
    roll = models.IntegerField(default=0)
    s_class = models.CharField(max_length=150)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
