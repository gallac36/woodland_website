from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce.models import HTMLField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='event_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(('image'), blank=True, null=True, upload_to='uploaded_images', default='forest-of-spruce.jpg')

    day = models.DateField(u'Day of the event', help_text=u'Day of the event', default=datetime.now())




    class Meta:
        ordering = ['day']

    def __str__(self):
        return self.title

   # def get_absolute_url(self):
   #     return reverse('event:detail', kwargs={'slug': self.slug})
