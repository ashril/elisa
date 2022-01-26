from re import search
from django.contrib import admin
from elisaapp.models import Role, Keterangan, Surat, User, Disposisi


class SuratAdmin(admin.ModelAdmin):
    list_display = ['nama_pic', 'instansi_asal', 'nomor_surat', 'perihal', 'tanggal_masuk', 'estimasi_deadline']
    search_fields = ['nomor_surat']
    list_filter = ['perihal']
    list_per_page = 10

# class PicAdmin(admin.ModelAdmin):
#     list_display = ['nama_pic', 'kontak_pic', 'instansi_asal']
#     list_filter = ['instansi_asal']
#     list_per_page = 10



# Register your models here.
admin.site.register(Role)
admin.site.register(Keterangan)
admin.site.register(Surat, SuratAdmin)
admin.site.register(User)
admin.site.register(Disposisi)
