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
from Plan.plan_view import Plan
from django.urls import path, include
from django.contrib import admin
from loginAPI.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from loginAPI.views import UserViewSet
from Employees.employees_view import Employee
from Employees.edit_employee_view import EmployeeUpdateView

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
    path('api/plan', Plan.as_view(), name='2023-plan'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/employees/<int:page_size>/', Employee.as_view(), name='employees'),
    path('api/employees/edit/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),


]

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
urlpatterns += router.urls