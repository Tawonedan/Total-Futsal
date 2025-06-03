from django.urls import path

from .views import CustomLogoutView, UserHomeView, UserBookView, UserBookDetailView, UserBookCreateView, UserProfileView, UserProfileEditView, UserAboutView, UserContactView, UserHistoryView

urlpatterns = [
    path('home/', UserHomeView.as_view(), name='user_home'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/Edit', UserProfileEditView.as_view(), name='user_profile_edit'),
    path('about/', UserAboutView.as_view(), name='user_about'),
    path('contact/', UserContactView.as_view(), name='user_contact'),
    path('booking/', UserBookView.as_view(), name='user_book'),
    path('booking/<int:id>/', UserBookDetailView.as_view(), name='user_book_detail'),
    path('booking/submit/', UserBookCreateView.as_view(), name='user_book_process'),
    path('history/', UserHistoryView.as_view(), name='user_history'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),


]