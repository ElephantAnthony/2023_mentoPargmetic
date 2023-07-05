
from django.urls import path, include

from profileapp.views import ProfileCreateView, ProfileUpdateView
from subscribeapp.views import SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe')
]