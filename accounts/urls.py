from django.urls import path

from .views import CustomLogoutView, UserHomeView, UserProfileView, UserProfileEditView, UserAboutView, UserHistoryView

urlpatterns = [
    path('home/', UserHomeView.as_view(), name='user_home'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/Edit', UserProfileEditView.as_view(), name='user_profile_edit'),
    path('about/', UserAboutView.as_view(), name='user_about'),
    path('history/', UserHistoryView.as_view(), name='history'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),


]