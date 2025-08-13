from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("polls/", include("polls.urls")),  #localhost:8000/polls/
    path('admin/', admin.site.urls),        #localhost:8000/admin/
] + debug_toolbar_urls()
