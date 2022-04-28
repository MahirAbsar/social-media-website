from django.urls import path
from . import views
urlpatterns = [

        path('sign-up/',views.sign_up,name='sign-up'),
        path('sign-in/',views.sign_in,name="sign-in"),
        path('sign-out/',views.sign_out,name='sign-out'),
        path('edit-profile/',views.edit_profile,name="edit-profile"),
        path('info-profile/',views.info_profile,name="info-profile"),
        path('user-other/<str:username>/',views.user_other,name="user-other"),
        path('follow/<str:username>',views.follow,name="follow"),
        path('unfollow/<str:username>',views.unfollow,name="unfollow")

]
