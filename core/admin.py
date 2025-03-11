from django.contrib import admin
from .models import About, Contact
from .models import GalleryCategory, GalleryImage
from .models import SkillCategory, Skill

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Display skills in table format
    list_filter = ('category',)  # Filter by category in admin panel
    search_fields = ('name',)  # Enable search by skill name
admin.site.register(GalleryCategory)
admin.site.register(GalleryImage)
admin.site.register(SkillCategory)
admin.site.register(Skill, SkillAdmin)
admin.site.register(About)
admin.site.register(Contact)
