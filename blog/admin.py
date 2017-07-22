from django.contrib import admin
from django import forms
import models

# How to separate this by section of site not app itself, not a high priority
# Blog posts
admin.site.register(models.Post)
# Resume
admin.site.register(models.Objective)
admin.site.register(models.ProfessionalExperience)
admin.site.register(models.EducationExperience)
admin.site.register(models.VolunteerExperience)
# Bio
admin.site.register(models.PersonalInterest)
admin.site.register(models.ProfessionalInterest)
admin.site.register(models.ShortBio)
