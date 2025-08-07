from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_form, name='cv_form'),
    path('preview/<int:cv_id>/', views.cv_preview, name='cv_preview'),
    path('export/<int:cv_id>/', views.cv_export_pdf, name='cv_export_pdf'),
]