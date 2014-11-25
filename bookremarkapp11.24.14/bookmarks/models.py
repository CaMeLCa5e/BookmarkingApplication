import datetime
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save


#import pdb; pdb.set_trace()


class UserProfile(models.Model):
  user          = models.OneToOneField(User)
  internal_id   = models.CharField(max_length=25, null = True, blank = True)
  verified      = models.BooleanField(default=False)
  approval_date = models.DateTimeField(null = True, blank = True)
  def __unicode__(self):
    return "(internal_id:'{0}', verified:'{1}', approval_date:'{2}')".format(self.internal_id, self.verified, self.approval_date)


class Link(models.Model):
  name          = models.CharField(max_length=50)
  link          = models.URLField()
  date_created  = models.DateTimeField(auto_now_add=True)   
  date_modified = models.DateTimeField(auto_now=True)
  tags          = models.TextField(null = True, blank = True)
  def __unicode__(self):
    return "(name:'{0}', link:'{1}', tags:'{2}')".format(self.name, self.link, self.tags)


class LinkList(models.Model):
  name          = models.CharField(max_length=50)
  date_created  = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)
  links         = models.ManyToManyField(Link)
  def __unicode__(self):
    return "(name:'{0}', links:{1})".format(self.name, self.links.all())


