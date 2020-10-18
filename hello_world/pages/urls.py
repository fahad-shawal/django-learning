from django.urls import path
from pages.views import homePageView

urlpatterns = [
    # when ever we hit the main server url it will be passed to `homePageView` defined in pages.views
    path(route='', view=homePageView, name='Home'),
]
