from django.urls import path
from details import views
urlpatterns=[
    path('details',views.func,name="con"),
    path('hi',views.func2,name="update"),
    path('',views.func3,name="delete")
]