from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from profiles import views as profile_view
from teachers import views as teacher_view

router = DefaultRouter()
router.register('profiles', profile_view.UserProfileViewSet)
router.register('login', profile_view.LoginViewSet, base_name='login')

# Teacher router
router.register('teachers', teacher_view.TeacherViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
