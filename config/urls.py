from django.contrib import admin
from django.urls import path, include
from notes.views import home, note_create, note_edit, note_delete

urlpatterns = [
    path("", home),
    path("notes/new/", note_create),
    path("notes/<int:note_id>/edit/", note_edit),
    path("notes/<int:note_id>/delete/", note_delete),
    path("admin/", admin.site.urls),
    path("api/", include("notes.urls")),
]