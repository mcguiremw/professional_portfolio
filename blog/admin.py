from django.contrib import admin
import models as m

# How to separate this by section of site not app itself, not a high priority
# Blog posts
admin.site.register(m.Post)
# Resume
admin.site.register(m.WorkExperience)
admin.site.register(m.EducationExperience)
admin.site.register(m.VolunteerExperience)
# Bio
admin.site.register(m.PersonalInterest)
admin.site.register(m.ProfessionalInterest)
admin.site.register(m.ShortBio)
