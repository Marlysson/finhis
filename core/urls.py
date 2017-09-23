
from django.conf.urls import url
from core.views import *
from rest_framework.authtoken import views

urlpatterns = [
        
        url(r'^token/', views.obtain_auth_token,name="auth-token"),

	url(r'^$',
        ApiRoot.as_view(),
        name=ApiRoot.name),

	url(r'^profiles/$', 
        ProfileViewList.as_view(), 
        name=ProfileViewList.name),

	url(r'^profiles/(?P<pk>[0-9]+)/$', 
        ProfileViewDetail.as_view(),
        name=ProfileViewDetail.name),
	
	url(r'^categories/$', 
        CategoryViewList.as_view(), 
        name=CategoryViewList.name),

	url(r'^categories/(?P<pk>[0-9]+)/$', 
        CategoryViewDetail.as_view(),
        name=CategoryViewDetail.name),
	
        url(r'^movements/$', 
        MovementViewList.as_view(), 
        name=MovementViewList.name),

        url(r'^movements/(?P<pk>[0-9]+)/$', 
        MovementViewDetail.as_view(),
        name=MovementViewDetail.name),

	url(r'^requests/$', 
        RequestCategoryViewList.as_view(), 
        name=RequestCategoryViewList.name),

	url(r'^requests/(?P<pk>[0-9]+)/$', 
        RequestCategoryViewDetail.as_view(),
        name=RequestCategoryViewDetail.name),
	    	    

]