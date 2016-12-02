from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^$',views.register_student,name='registeration'),
    url(r'^success$',views.register_success,name='registered'),
]
urlpatterns += staticfiles_urlpatterns()

