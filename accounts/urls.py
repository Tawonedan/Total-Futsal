from django.urls import path

from .views import CustomLogoutView, UserHomeView, UserBookView, UserProfileView, UserProfileEditView, UserAboutView, UserHistoryView

urlpatterns = [
    path('home/', UserHomeView.as_view(), name='user_home'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/Edit', UserProfileEditView.as_view(), name='user_profile_edit'),
    path('about/', UserAboutView.as_view(), name='user_about'),
    path('booking/', UserBookView.as_view(), name='user_book'),
    path('history/', UserHistoryView.as_view(), name='user_history'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),


]