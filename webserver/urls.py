from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
# from source import views
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url, include
from rest_framework import routers

from account.views import LoginViewSet, LogoutView, RegisterViewSet, UserDeleteViewSet, AccountViewSet
from camera.views import CompanyViewSet


schema_view = get_swagger_view(title='Seksu API')
router = routers.DefaultRouter()

router.register(r'login', LoginViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'user/register', RegisterViewSet)
router.register(r'user/delete', UserDeleteViewSet)
router.register(r'user', AccountViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', schema_view),
    url(r'^logout/$', LogoutView.as_view()),
    # url(r'sek/',views.sek),
    # url(r'template/',views.template),
    url(r'^', include(router.urls))
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
