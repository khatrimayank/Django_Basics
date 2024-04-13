from django.db import models

# Create your models here.

class GeeksModel(models.Model):

	title=models.CharField(max_length=100)

	description=models.TextField()

	length=models.IntegerField(default=0)

	def __str__(self):
		return self.title

# model named Post
class PostModel(models.Model):
	Male = 'M'
	FeMale = 'F'
	GENDER_CHOICES = (
	(Male, 'Male'),
	(FeMale, 'Female'),
	)

	# define a username field with bound max length it can have
	username = models.CharField( max_length = 20, blank = False,
								null = False)
	
	# This is used to write a post
	text = models.TextField(blank = False, null = False)
	
	# Values for gender are restricted by giving choices
	gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, 
							default = Male)
	
	time = models.DateTimeField(auto_now_add = True)

		