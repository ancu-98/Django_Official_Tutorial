from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),  #localhost:8000/polls/
    path('admin/', admin.site.urls),        #localhost:8000/admin/
]
