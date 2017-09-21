
from django.conf.urls import url
from core import views

urlpatterns = [

	url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),

	url(r'^profiles/$', 
        views.ProfileViewList.as_view(), 
        name=views.ProfileViewList.name),

	url(r'^profiles/(?P<pk>[0-9]+)/$', 
        views.ProfileViewDetail.as_view(),
        name=views.ProfileViewDetail.name),
	
	url(r'^categories/$', 
        views.CategoryViewList.as_view(), 
        name=views.CategoryViewList.name),

	url(r'^categories/(?P<pk>[0-9]+)/$', 
        views.CategoryViewDetail.as_view(),
        name=views.CategoryViewDetail.name),
	
        url(r'^movements/$', 
        views.MovementViewList.as_view(), 
        name=views.MovementViewList.name),

        url(r'^movements/(?P<pk>[0-9]+)/$', 
        views.MovementViewDetail.as_view(),
        name=views.MovementViewDetail.name),

	url(r'^requests/$', 
        views.RequestCategoryViewList.as_view(), 
        name=views.RequestCategoryViewList.name),

	url(r'^requests/(?P<pk>[0-9]+)/$', 
        views.RequestCategoryViewDetail.as_view(),
        name=views.RequestCategoryViewDetail.name),
	    	    

]