from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import CVData
from .forms import CVForm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def cv_form(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            cv = form.save()
            return redirect('cv_preview', cv_id=cv.id)
    else:
        form = CVForm()
    
    return render(request, 'cv/form.html', {'form': form})

def cv_preview(request, cv_id):
    cv = get_object_or_404(CVData, id=cv_id)
    return render(request, 'cv/preview.html', {'cv': cv})

def cv_export_pdf(request, cv_id):
    cv = get_object_or_404(CVData, id=cv_id)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="CV_{cv.nama}.pdf"'
    
    # Buat PDF sederhana
    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Header
    story.append(Paragraph(f"<b>{cv.nama}</b>", styles['Title']))
    story.append(Spacer(1, 12))
    
    # Data Pribadi
    story.append(Paragraph(f"Email: {cv.email}", styles['Normal']))
    story.append(Paragraph(f"No HP: {cv.nomor_hp}", styles['Normal']))
    story.append(Paragraph(f"Alamat: {cv.alamat}", styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Pendidikan
    story.append(Paragraph("<b>PENDIDIKAN</b>", styles['Heading2']))
    story.append(Paragraph(cv.pendidikan.replace('\n', '<br/>'), styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Pengalaman
    story.append(Paragraph("<b>PENGALAMAN KERJA</b>", styles['Heading2']))
    story.append(Paragraph(cv.pengalaman.replace('\n', '<br/>'), styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Keterampilan
    story.append(Paragraph("<b>KETERAMPILAN</b>", styles['Heading2']))
    story.append(Paragraph(cv.keterampilan.replace('\n', '<br/>'), styles['Normal']))
    
    # Sertifikasi (jika ada)
    if cv.sertifikasi:
        story.append(Spacer(1, 12))
        story.append(Paragraph("<b>SERTIFIKASI</b>", styles['Heading2']))
        story.append(Paragraph(cv.sertifikasi.replace('\n', '<br/>'), styles['Normal']))
    
    doc.build(story)
    return response