from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
class movieinfo(models.Model):
	movie_name = models.CharField(max_length=100)
	movie_link = models.CharField(max_length=100)
	movie_rating = models.CharField(max_length=10)
	movie_summary = models.CharField(max_length=10000)
	movie_image = models.CharField(max_length=100,default=0)
	def __unicode__(self):
		return u'%s %s %s %s %s' % (self.movie_name,self.movie_link,self.movie_rating,self.movie_summary,self.movie_image)

