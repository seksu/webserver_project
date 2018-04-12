from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
# from source import views
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url, include
from rest_framework import routers

from account.views import LoginViewSet, LogoutView, RegisterViewSet, UserDeleteViewSet, AccountViewSet, \
                        ImageViewSet, ListAccountViewSet, InActiveUserViewSet
from camera.views import CompanyViewSet, CameraViewSet, AddCameraViewSet, DeleteCameraViewSet, \
                        AddCompanyViewSet, DeleteCompanyViewSet
from source.views import SearchViewSet, DeleteSearchingDetailViewSet, SearchAdminViewSet


schema_view = get_swagger_view(title='Seksu API')
router = routers.DefaultRouter()

router.register(r'login', LoginViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'user/register', RegisterViewSet)
router.register(r'user/delete', UserDeleteViewSet)
router.register(r'user', AccountViewSet)
router.register(r'user/image', ImageViewSet)
router.register(r'search', SearchViewSet)
router.register(r'delete/searching_detail', DeleteSearchingDetailViewSet)
router.register(r'camera/list', CameraViewSet)
router.register(r'camera/add', AddCameraViewSet)
router.register(r'camera/delete', DeleteCameraViewSet)
router.register(r'search/admins', SearchAdminViewSet)
router.register(r'company/add', AddCompanyViewSet)
router.register(r'company/delete', DeleteCompanyViewSet)
router.register(r'user/list', ListAccountViewSet)
router.register(r'user/inactive', InActiveUserViewSet)
# router.register(r'insert', InsertViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', schema_view),
    # url(r'^user/upload-image/(?P<filename>[^/]+)$', ImageUploadView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    # url(r'sek/',views.sek),
    # url(r'template/',views.template),
    url(r'^', include(router.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
