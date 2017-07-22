from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.postgres.fields import ArrayField

_TIME_FORMAT = "%B %Y"


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextField(default='article entry here')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Objective(models.Model):
    obj = RichTextField(default='objective here')


class Experience(models.Model):
    from_date = models.DateField(blank=False)
    to_date = models.DateField(blank=True, null=True)
    location = models.CharField(blank=False, max_length=50, default='LOC_CITY, LS')
    description = RichTextField(default='description here')
    attachments = CKEditorUploadingWidget()

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)


class ProfessionalExperience(Experience):
    exp = models.OneToOneField(
        Experience,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True,
    )
    employer = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50, default="ROCK STAR")

    def __str__(self):
        return """
            Work Experience ID: {self.exp}\n
            Employer: {self.employer}\n
            Job Title: {self.job_title}\n
            """.format(self=self)


class EducationExperience(Experience):
    exp = models.OneToOneField(
        Experience,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True,
    )
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=80)
    major = models.CharField(max_length=50)
    minor = models.CharField(max_length=50, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return str(self.major)


class VolunteerExperience(Experience):
    exp = models.OneToOneField(
        Experience,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True
    )
    org = models.CharField(max_length=80)
    summary = models.CharField(max_length=80)
    reason = models.TextField()

    def __str__(self):
        return org

# The interest models may be expanded to give more detail in bootstrap wells
# along the gutters of the site.  Will be in a feature request at some point.


class PersonalInterest(models.Model):
    interest = models.CharField(max_length=50)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.interest


class ProfessionalInterest(models.Model):
    interest = models.CharField(max_length=50)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.interest


class ShortBio(models.Model):
    bio = RichTextField(default='bio here')

    def __str__(self):
        return self.bio
