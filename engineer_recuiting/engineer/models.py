from django.db import models
from django.contrib.auth.models import User
# Create your models here.


DGREE_TYPES=(
    ('H','Highschool'),
    ('B','Banchler'),
    ('M','Master'),
    ('P','PHD'),
)
STATUS_TYPE=(
    ('W','waiting for approve'),
    ('N','normal user'),
    ('B','baned')
)
class EngineerProfile(models.Model):
    user=models.OneToOneField(User)
    phone=models.CharField(max_length=15)
    dob=models.DateField()
    ssn=models.CharField(max_length=20)
    status=models.CharField(max_length=3,choices=STATUS_TYPE,default='W')
    review_score=models.IntegerField(default=-1)
    description=models.CharField(max_length='200')
class SkillCertification(models.Model):
    owner=models.ForeignKey(User,related_name='skill_certifications')
    img=models.ImageField(upload_to='/SkillImg/')
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
class CertificationOfDegree(models.Model):
    university=models.CharField(max_length=20)
    degree=models.CharField(max_length=1,choices=DGREE_TYPES)
    owner=models.ForeignKey(User,related_name='degree_certifications')
    img = models.FileField(upload_to = '/DegreeImg/')