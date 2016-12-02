from django.conf.urls import url
from . import views
app_name='login'
urlpatterns = [
		url(r'^$',views.home,name='home'),
		url(r'^login/$',views.login_user,name='login'),
		url(r'^logout/$',views.logout_page,name='logout'),
		url(r'^edit/$',views.edit,name='edit')
    
]
