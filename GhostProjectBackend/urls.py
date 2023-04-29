from django.contrib import admin
from django.urls import path, include
from PerformanceTab.views import ProjectStats

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project-statistics/<int:year>/', ProjectStats.as_view(), name='project-stats')

]
