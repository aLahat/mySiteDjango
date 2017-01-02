from django.db import models

def rename(instance,filename):
	print( '/'.join(['images', str(instance.pk), filename]))

	return '/'.join(['images', str(instance.pk), filename])

class Post(models.Model):
	title = models.CharField(max_length=140)
	topic = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()
#	image1 = models.ImageField(upload_to=rename,
#				   default = 'images/none.jpg')
	def __str__(self):
		return self.title
