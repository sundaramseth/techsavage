from django.contrib.sitemaps import Sitemap
from .models import Job


class JobSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.5

    def items(self):
        return Job.objects.all()

    def lastmod(self, obj):
        return obj.post_update
