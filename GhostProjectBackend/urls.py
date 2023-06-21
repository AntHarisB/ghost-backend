
from django.contrib import admin
from django.urls import path, include
from PerformanceTab.view_stats import ProjectStats
from PerformanceTab.view_projectcreation import ProjectCreationCount
from PerformanceTab.view_typeofproject import ProjectTypeCount
from PerformanceTab.views_hours import ProjectHours
from RevenueCosts.stats_rev_cost_view import StatsRevenueCost
from RevenueCosts.rev_cost_perp_view import ActualRevenueCosts
from RevenueCosts.rev_cost_perp_perm_view import RevenueCostPerMonth
from Projects.projects_view import ProjectInfo
from Projects.active_projects_view import ActiveProjectInfo
from Projects.inactive_projects_view import InactiveProjectInfo
from Projects.onhold_projects_view import OnholdProjectInfo
from Plan.plan_view import Plan
from django.urls import path, include
from django.contrib import admin
from loginAPI.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from loginAPI.views import UserViewSet
from Projects.add_project_view import ProjectCreateView
from Projects.update_project_view import ProjectUpdateView
from Projects.delete_project_view import ProjectDeleteView
from Invoicing.invoicing_view import InvoicingView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/project-statistics/<int:year>/', ProjectStats.as_view(), name='project-stats'),
    path('api/projectcreation-count/<int:year>/', ProjectCreationCount.as_view(), name='projectcreation-count'),
    path('api/projecttype-count/<int:year>/', ProjectTypeCount.as_view(), name='projecttype-count'),
    path('api/project-hours/<int:year>/', ProjectHours.as_view(), name='project-hours'),
    path('api/stats_revenue_costs/<int:year>/', StatsRevenueCost.as_view(), name='stats_revenue_costs'),
    path('api/actual_costs_revenue/<int:year>/', ActualRevenueCosts.as_view(), name='acutal_costs_revenue'),
    path('api/actual_planned_costs_revenue/<int:year>/', RevenueCostPerMonth.as_view(), name='actual_planned_costs_revenue'),
    path('api/projects/<int:page_size>/', ProjectInfo.as_view(), name='projects'),
    path('api/active_projects/<int:page_size>/', ActiveProjectInfo.as_view(), name='active_projects'),
    path('api/inactive_projects/<int:page_size>/', InactiveProjectInfo.as_view(), name='inactive_projects'),
    path('api/onhold_projects/<int:page_size>/', OnholdProjectInfo.as_view(), name='onhold_projects'),
    path('api/plan', Plan.as_view(), name='2023-plan'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/add_project/', ProjectCreateView.as_view(), name='create_project'),
    path('api/update_project/<int:pk>/', ProjectUpdateView.as_view(), name='update_project'),
    path('api/delete_project/<int:pk>/', ProjectDeleteView.as_view(), name='delete_project'),
    path('api/invoicing/<int:page_size>/', InvoicingView.as_view(), name='inovicing'),

]

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
urlpatterns += router.urls