from django.db import models
from accounts.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

    
class Category(models.Model):
    name = models.CharField(max_length=255)
    #course = models.ManyToManyField('Course', related_name='categories', blank=True)
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    
class Course(models.Model):
    course_name = models.CharField(max_length=250)
    course_code = models.CharField(max_length=250)
    instructor = models.ForeignKey(
        CustomUser, blank=True,null=True, related_name='coursess', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='courses')
    students = models.ManyToManyField(
        CustomUser, blank=True, related_name='course')
    #slug = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField(blank=True)
    rate = models.IntegerField()
    data_added = models.DateTimeField()
    existence = models.BooleanField()  
    duration = models.IntegerField()
    min_students = models.IntegerField(blank=True, default=1)
    max_students = models.IntegerField()
    
    def __str__(self):
        return self.course_name

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
        return self.Course.instructor == user
    
    
class Practice(models.Model):
    teacher = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='practice')
    Course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='practice')
    submited_date = models.DateTimeField(default=timezone.now)
    Question = models.TextField(blank=True, null=True , default='')
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.teacher.username}"  
    
    
class Homework(models.Model):
    student = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='homeworks')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='homeworks')
    submited_date = models.DateTimeField(default=timezone.now)
    answer = models.TextField(blank=True, null=True , default='')
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.username}"

    def is_owner(self, user):
        return self.student == user

    def can_see(self, user):
        return (user.has_role('CustomUser') and self.is_owner(user.CustomUser)) \
		or (user.has_role('CustomUser') and self.is_course_owner(user.CustomUser))




