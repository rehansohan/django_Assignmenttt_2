from django.urls import path 
from first_app.views import base,add_task,show_task,edit_task,delete_task,complete
urlpatterns = [
    path('',base,name="homepage"),
    path('add_task/',add_task,name="add_task"),
    path('show_task/',show_task,name="show_task"),
     path('edit_task/<int:id>',edit_task,name="edit_task"),
     path('delete_task/<int:id>',delete_task,name="delete_task"),
     path('complete/<int:id>',complete,name="complete"),
]


