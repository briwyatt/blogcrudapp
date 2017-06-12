from django.db import models
from django.core.urlresolvers import reverse


class Blog(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=20000)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:blog_edit', kwargs={'pk': self.pk})