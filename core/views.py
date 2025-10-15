from django.shortcuts import render
from .models import About, Contact, GalleryCategory, SkillCategory
from django.core.mail import send_mail  
from django.contrib import messages

def skills_trained(request):
    categories = SkillCategory.objects.prefetch_related('skill_set').all()
    return render(request, 'core/skills_trained.html', {'categories': categories})  # Fix template name

def gallery(request):
    categories = GalleryCategory.objects.prefetch_related('galleryimage_set').all()
    return render(request, 'core/gallery.html', {'categories': categories})

def index(request):
    about = About.objects.first()
    contact = Contact.objects.first()
    categories = SkillCategory.objects.all() 
    return render(request, 'core/index.html', {'about': about, 'categories': categories, 'contact': contact})  # Removed services

def about(request):
    about = About.objects.first()
    return render(request, 'core/about.html', {'about': about})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject="New Contact Form Submission",
            message=full_message,
            from_email=email,
            recipient_list=['deeptrainersuganda@gmail.com'],
        )

        messages.success(request, "Your message has been sent successfully!")
    
    return render(request, 'core/contact.html')
