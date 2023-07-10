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
from loginAPI.forgot_password import confirm_password_reset
from django_rest_passwordreset import views as password_reset_views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from loginAPI.views import UserViewSet
from Projects.projects_view import ProjectInfo1
from Employees.employees_view import Employee, EmployeeList
from Employees.getEmployeeId_view import EmployeeId
from Employees.edit_employee_view import EmployeeUpdateView
from Employees.add_employee_view import EmployeeAddView
from Employees.delete_employee_view import EmployeeDeleteView
from Employees.deletedEmployees_view import PastEmployeesList, PastEmployeesListPages
from Projects.getProjectId_view import ProjectId
from Projects.add_project_view import ProjectCreateView
from Projects.update_project_view import ProjectUpdateView
from Projects.delete_project_view import ProjectDeleteView
from Invoicing.invoicing_view import InvoicingView, InvoicingViewAll
from Invoicing.paid_invoicing_view import PaidInvoicingView
from Invoicing.sent_invoicing_view import SentInvoicingView
from Invoicing.delete_invoicing_view import InvoicingDeleteView
from Invoicing.pdf_invoicing_view import generate_invoice_pdf
from Invoicing.invoicing_status_view import StatusInvoicingView

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
    path('api/project_id/<int:id>/', ProjectId.as_view(), name='project_id'),
    path('api/projects/', ProjectInfo1.as_view(), name='projects'),
    path('api/active_projects/<int:page_size>/', ActiveProjectInfo.as_view(), name='active_projects'),
    path('api/inactive_projects/<int:page_size>/', InactiveProjectInfo.as_view(), name='inactive_projects'),
    path('api/onhold_projects/<int:page_size>/', OnholdProjectInfo.as_view(), name='onhold_projects'),
    path('api/plan', Plan.as_view(), name='2023-plan'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/password_reset/confirm/', confirm_password_reset, name='password_reset_confirm'),
    path('api/employees/<int:page_size>/', Employee.as_view(), name='employees'),
    path('api/employees_list/', EmployeeList.as_view(), name='employees_list'),
    path('api/employees_id/<int:id>/', EmployeeId.as_view(), name='employee_id'),
    path('api/employees/edit/<int:user_id>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('api/add_employee/', EmployeeAddView.as_view(), name='employee-add'),
    path('api/delete_employee/<int:id>/', EmployeeDeleteView.as_view(), name='delete_employee'),
    path('api/past_employees/', PastEmployeesList.as_view(), name='past_employees'),
    path('api/past_employees/<int:page_size>/', PastEmployeesListPages.as_view(), name='past_employees_pages'),
    path('api/add_project/', ProjectCreateView.as_view(), name='create_project'),
    path('api/update_project/<int:project_id>/', ProjectUpdateView.as_view(), name='update_project'),
    path('api/delete_project/<int:project_id>/', ProjectDeleteView.as_view(), name='delete_project'),
    path('api/invoicing/<int:page_size>/', InvoicingView.as_view(), name='inovicing'),
    path('api/invoicing/', InvoicingViewAll.as_view(), name='all_inovicing'),
    path('api/paid_invoicing/<int:page_size>/', PaidInvoicingView.as_view(), name='paid_inovicing'),
    path('api/sent_invoicing/<int:page_size>/', SentInvoicingView.as_view(), name='sent_inovicing'),
    path('api/delete_invoicing/<int:id>/', InvoicingDeleteView.as_view(), name='delete_inovicing'),
    path('api/invoices_pdf/<int:invoice_id>/', generate_invoice_pdf, name='generate_invoice_pdf'),
    path('api/invoice_status/<int:id>/', StatusInvoicingView.as_view(), name='status_invoice'),

]

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
urlpatterns += router.urls