from django.urls import path

from .views import AdminDashboardView, AdminProfileView, AdminProfileEditView, AdminFieldsView, AdminFieldsAddView, AdminFieldsEditView, AdminAccessoriesView, AdminAccessoriesAddView, AdminAccessoriesEditView, AdminReportView, AdminHistoryView, AdminHistoryDetailView

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('Profile/', AdminProfileView.as_view(), name='admin_profile'),
    path('Profile/Edit/', AdminProfileEditView.as_view(), name='admin_profile_edit'),
    path('Fields/', AdminFieldsView.as_view(), name='admin_fields'),
    path('Fields/Add', AdminFieldsAddView.as_view(), name='admin_fields_add'),
    path('Fields/Edit', AdminFieldsEditView.as_view(), name='admin_fields_edit'),
    path('Accessories/', AdminAccessoriesView.as_view(), name='admin_accessories'),
    path('Accessories/Add', AdminAccessoriesAddView.as_view(), name='admin_accessories_add'),
    path('Accessories/Edit', AdminAccessoriesEditView.as_view(), name='admin_accessories_edit'),
    path('Report/', AdminReportView.as_view(), name='admin_report'),
    path('History/', AdminHistoryView.as_view(), name='admin_history'),
    path('History/Detail', AdminHistoryDetailView.as_view(), name='admin_history_detail'),

]