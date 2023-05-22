
from django.contrib import admin
from django.urls import path, include
from PerformanceTab.view_stats import ProjectStats
from PerformanceTab.view_projectcreation import ProjectCreationCount
from PerformanceTab.view_typeofproject import ProjectTypeCount
from PerformanceTab.views_hours import ProjectHours
from RevenueCosts.stats_rev_cost_view import StatsRevenueCost
from RevenueCosts.rev_cost_perp_view import ActualRevenueCosts
from RevenueCosts.rev_cost_perp_perm_view import RevenueCostPerMonth
from django.urls import path, include
from django.contrib import admin
from loginAPI.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from loginAPI.views import UserViewSet

urlpatterns = [
    path('project-statistics/<int:year>/', ProjectStats.as_view(), name='project-stats'),
    path('projectcreation-count/<int:year>/', ProjectCreationCount.as_view(), name='projectcreation-count'),
    path('projecttype-count/<int:year>/', ProjectTypeCount.as_view(), name='projecttype-count'),
    path('project-hours/<int:year>/', ProjectHours.as_view(), name='project-hours'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/stats_revenue_costs/<int:year>/', StatsRevenueCost.as_view(), name='stats_revenue_costs'),
    path('api/actual_costs_revenue/<int:year>/', ActualRevenueCosts.as_view(), name='acutal_costs_revenue'),
    path('api/actual_planned_costs_revenue/<int:year>/', RevenueCostPerMonth.as_view(), name='actual_planned_costs_revenue')

]

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
urlpatterns += router.urls