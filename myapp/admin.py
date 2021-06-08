from django.contrib import admin
from .models import *

class RincianAdmin(admin.ModelAdmin):
	exclude = ('jumlahnya',)

admin.site.register(Surat_perintah)
admin.site.register(Sppd)
admin.site.register(Pegawai)
admin.site.register(Instansi)
# admin.site.register(Biaya)
# admin.site.register(Anggaran)
admin.site.register(Pengeluaran)
admin.site.register(Rincian, RincianAdmin)