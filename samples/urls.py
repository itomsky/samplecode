from django.urls import path
from samples import views

urlpatterns = [
    path("new/", views.samples_new, name="samples_new"),
    path("<int:samples_id>/", views.samples_detail, name="samples_detail"),
    path("<int:samples_id>/edit/", views.samples_edit, name="samples_edit"),
]