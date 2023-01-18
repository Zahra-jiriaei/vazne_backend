from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models

class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent = None)
        return qs
    def filter_by_instance(self, instance):
        Content_Type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(Content_Type = Content_Type , object_id = obj_id ),filter(parent = None)
        return qs

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , default = 1 , on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType , on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type' , 'object_id')
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = CommentManager()
    
    class Meta():
        ordering = ['timestamp']
    
    def __unicode__(self):
        return str(self.user.username)
    
    def __str__(self):
        return str(self.user.username)
        
    def get_absolute_url(self):
        return reverse("comments:thread", kwargs={"id": self.id})