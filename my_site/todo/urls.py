from django.urls import path
from . import views
urlpatterns = [
    path('dashboard', views.index, name='dashboard'),
    path('update/<int:project_id>',views.project_edit,name="update_project"),
    path('delete/<int:project_id>', views.project_delete, name="delete_project"),
    path('detail/<int:project_id>', views.project_detail, name="detail_project"),

    path('update_task/<int:task_id>', views.task_edit, name="update_task"),
    path('delete_task/<int:task_id>', views.task_delete, name="delete_task"),
    path('detail_task/<int:project_id>/<int:task_id>', views.task_detail, name="detail_task"),
    path('add_task/<int:project_id>', views.add_task, name="add_task"),
]
