from django.urls import path
from .views import LandingPageView, AboutListView, PropertyListView, ContactListView, BlogListView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('about/', AboutListView.as_view(), name='about'),
    path('property/', PropertyListView.as_view(), name='property'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('blog/', BlogListView.as_view(), name='blog'),

]