"""mini_hrd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from homepage import views as homepage_views
from karyawan import views as karyawan_views
from kehadiran import views as kehadiran_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', karyawan_views.profil),
    url(r'^ganti_foto/', karyawan_views.ganti_foto),
    url(r'^login/', homepage_views.login_view),
    url(r'^logout/', homepage_views.logout_view),
    url(r'^daftar_hadir/$', kehadiran_views.daftar_hadir),
    url(r'^pengajuan_izin/', kehadiran_views.pengajuan_izin),
    url(r'^daftar_izin/', kehadiran_views.daftar_izin),
    url(r'^daftar_hadir/grafik/(?P<bulan>\d+)/(?P<tahun>\d+)$', kehadiran_views.tampil_grafik),
    url(r'^daftar_hadir/cetak/(?P<bulan>\d+)/(?P<tahun>\d+)$', kehadiran_views.cetak_daftar_hadir),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)