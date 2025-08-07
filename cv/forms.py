from django import forms
from .models import CVData

class CVForm(forms.ModelForm):
    class Meta:
        model = CVData
        fields = '__all__'
        exclude = ['created_at']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Lengkap'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'nomor_hp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '08xxxxxxxxxx'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Alamat lengkap'}),
            'pendidikan': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Contoh:\nS1 Teknik Informatika - Universitas ABC (2020-2024)\nSMA Negeri 1 - Jurusan IPA (2017-2020)'}),
            'pengalaman': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Contoh:\nWeb Developer - PT ABC (2023-sekarang)\n- Mengembangkan website company profile\n- Maintenance sistem internal'}),
            'keterampilan': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Contoh:\nProgramming: Python, JavaScript, PHP\nFramework: Django, React\nDatabase: MySQL, PostgreSQL'}),
            'sertifikasi': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Contoh:\nGoogle IT Support Certificate (2023)\nAWS Cloud Practitioner (2024) - Opsional'}),
        }