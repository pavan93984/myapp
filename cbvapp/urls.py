from django.urls import path
from cbvapp import views

urlpatterns = [
    path("",views.school_list.as_view(),name='list'),
    path("<int:pk>/",views.school_details.as_view(),name='details'),
    path("add_school/",views.schoolcreate.as_view(),name='add_school'),
    path("update/<int:pk>/",views.update.as_view(),name="update"),
    path("delete/<int:pk>",views.school_delete.as_view(),name="delete")
]