from django.urls import path
from .import views


app_name = 'account'

urlpatterns = [
	path('signup/', views.signup_view, name='signup'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('profile/', views.profile_view, name='profile'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),
	path('change-password/', views.change_password, name='change_password'),
	# path('simple_upload/', views.simple_upload, name='simple_upload'),

] 


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)