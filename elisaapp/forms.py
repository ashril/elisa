from attr import field
from django.forms import ModelForm, forms
from django import forms
from elisaapp.models import Surat

class FormInputSurat(ModelForm):
    class Meta:
        model = Surat
        fields = '__all__'

        widgets = {
            'id_pic' : forms.TextInput({'class':'form-control'}),
            'nama_pic' : forms.TextInput({'class':'form-control'}),
            'instansi_asal' : forms.TextInput({'class':'form-control'}),
            'kontak_pic' : forms.TextInput({'class':'form-control'}),
            'email_pic' : forms.TextInput({'class':'form-control'}),
            'nomor_surat' : forms.TextInput({'class':'form-control'}),
            'tanggal_surat' : forms.TextInput({'class':'form-control'}),
            'tanggal_masuk' : forms.TextInput({'class':'form-control'}),
            'estimasi_deadline' : forms.TextInput({'class':'form-control'}),
            'perihal' : forms.TextInput({'class':'form-control'})

        }
