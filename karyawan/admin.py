from django.contrib import admin
from karyawan.models import *

# Register your models here.
class DivisiAdmin (admin.ModelAdmin):
	list_display = ['nama', 'keterangan']
	list_filter = ()
	search_fields = ['nama', 'keterangan']
	list_per_page = 25

admin.site.register(Divisi, DivisiAdmin)

class JabatanAdmin (admin.ModelAdmin):
	list_display = ['nama', 'keterangan']
	list_filter = ()
	search_fields = ['nama', 'keterangan']
	list_per_page = 25

admin.site.register(Jabatan, JabatanAdmin)

class KaryawanAdmin (admin.ModelAdmin):
	list_display = ['nama', 'alamat', 'jenis_kelamin', 'jenis_karyawan', 'jabatan', 'divisi', 'email', 'no_telepon']
	list_filter = ('jenis_kelamin', 'jenis_karyawan', 'jabatan', 'divisi')
	search_fields = ['nama', 'alamat', 'email', 'no_telepon']
	list_per_page = 25

admin.site.register(Karyawan, KaryawanAdmin)

class AkunAdmin (admin.ModelAdmin):
	list_display = ['akun', 'karyawan', 'jenis_akun']
	list_filter = ('jenis_akun',)
	search_fields = []
	list_per_page = 25

admin.site.register(Akun, AkunAdmin)