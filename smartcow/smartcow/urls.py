from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from annotation import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('annotate/<int:id>', views.annotate),
    url(r'^upload/$', views.UploadView.as_view(), name='upload'),
    path('', views.signup),
    path('confirm/<int:id>', views.confirm),
    url(r'^checkannotate/(?P<id>[-\w]+)/$', views.check_my_annotate_n_csv_download, name='check_my_annotate_n_csv_download'),
    url(r'^downloadcsv/(?P<id>[-\w]+)/$', views.downloadcsv, name='downloadcsv'),
    path('myannonate/', views.myannonate),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
