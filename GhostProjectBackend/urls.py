from django.contrib import admin
from django.urls import path, include
from PerformanceTab.view_stats import ProjectStats
from PerformanceTab.view_projectcreation import ProjectCreationCount
from PerformanceTab.view_typeofproject import ProjectTypeCount

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project-statistics/<int:year>/', ProjectStats.as_view(), name='project-stats'),
    path('projectcreation-count/<int:year>/', ProjectCreationCount.as_view(), name='projectcreation-count'),
    path('projecttype-count/<int:year>/', ProjectTypeCount.as_view(), name='projecttype-count'),
]
