from django.urls import re_path

from api_project.app_name.views import ExampleViewset

urlpatterns = [
    re_path(
        r'(?P<protocol>\w+)/?',
        ExampleViewset.as_view({'patch': 'function_example'})
    ),
    re_path(
        '',
        ExampleViewset.as_view({'get': 'list', 'post': 'create'})
    ),
]
