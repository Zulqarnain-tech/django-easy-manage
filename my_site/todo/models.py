from django.db import models
from account.models import Account
# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return str(self.id)
class Task(models.Model):
    
    task_name = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=50)
    project = models.ForeignKey(Project, blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task_name
    
    # def get_absolute_url(self):
    #     return reverse('dashboard')


# , kwargs = {
#     'course_pk': self.course_id,
#     'step_pk': self.id
# }
# on_delete = models.SET_NULL
