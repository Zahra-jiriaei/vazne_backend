from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser
from uuid import uuid4
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

"""if CustomUser.role==0:
    Student=CustomUser
else:
    Instructor=CustomUser
    """
"""
def course_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)
"""
"""class Instructor(models.Model):
    if CustomUser.role==1:
        instructor = models.ForeignKey(
            CustomUser, blank=True, related_name='courses', on_delete=models.CASCADE)
    def __str__(self):
        return self.instructor
        
class Student(models.Model):
    if CustomUser.role==0:
        Student = models.ForeignKey(
            CustomUser, blank=True, related_name='courses', on_delete=models.CASCADE)
    def __str__(self):
        return self.Student"""

class Category(models.Model):
    name = models.CharField(max_length=255)
    #course = models.ManyToManyField('Course', related_name='categories', blank=True)
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name



"""   
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
"""
    
class Course(models.Model):
    course_name = models.CharField(max_length=250)
    course_code = models.CharField(max_length=250)
    instructor = models.ForeignKey(
        CustomUser, blank=True,null=True, related_name='coursess', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='courses')
    students = models.ManyToManyField(
        CustomUser, blank=True,null=True, related_name='courses')
    #slug = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField(blank=True)
    rate=models.IntegerField()
    data_added = models.DateTimeField()
    existence = models.BooleanField()  
    duration = models.IntegerField()
    min_students = models.IntegerField(blank=True, default=1)
    max_students = models.IntegerField()


    """
    class Meta:
        ordering = ['-data_added']
    """

    """def __str__(self):
        return self.title"""

    def is_enrolled(self, user):
        return self.students.filter(id=user.id).exists()

    def is_owner(self, user):
        return self.instructor == user

    def is_course_user(self, user):
        return (user.has_role('student') and self.is_enrolled(user.student)) \
		or (user.has_role('instructor') and self.is_owner(user.instructor))

    def update_rate(self):
        rates = self.rates.all()
        self.rate_no = len(rates)
        self.rate = round(sum([rate_obj.rate for rate_obj in rates]) / self.rate_no, 1)
        self.save()

    def update_capacity(self):
        self.capacity = self.max_students - len(self.students.all())
        self.save()
        
    def can_enroll(self, student):
        return True
    
class Comment(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='comment')
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.course.course_name} {self.text}"

    def is_owner(self, user):
        return self.user == user

    def is_course_owner(self, user):
        return self.course.instructor==user
    
