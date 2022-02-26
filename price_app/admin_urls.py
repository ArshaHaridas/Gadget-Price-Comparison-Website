
from django.urls import path
from django.urls.conf import include

from price_app import admin_views
from price_app.admin_views import View_Comment

urlpatterns = [
    path('', admin_views.IndexView, name="IndexView"),
    path('cpmment',View_Comment.as_view())


]
