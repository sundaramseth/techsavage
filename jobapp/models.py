from django.db import models
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

STATUS = (
    (0,"Draft"),

    (1,"Publish")
)

class Job(models.Model):
    postname = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.CharField(max_length=20,blank=True, null=True)
    post_date = models.DateTimeField(null=True)
    post_update = models.DateTimeField(auto_now= True)
    shortinfo = models.CharField(max_length=500)
    job_description =RichTextUploadingField(blank=True, null=True,
                                      config_name='special',
                                      external_plugin_resources=[(
                                          'youtube',
                                          '/static/ckeditor/ckeditor/plugins/youtube/',
                                          'plugin.js',
                                          )],
                                      )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.postname

    def save(self, *args, **kwargs):
        self.slug = slugify(self.postname)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('job_detail',
                       args=[str(self.slug)])
