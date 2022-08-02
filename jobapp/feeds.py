from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Job
from django.urls import reverse


class LatestJobPostsFeed(Feed):
    title = "Bloggystacker Job Notifications"
    link = "/feeds/"
    description = "Latest post@bloggystacker"

    def items(self):
        return Job.objects.filter(status=1)

    def item_title(self, item):
        return item.postname

    def item_description(self, item):
        return truncatewords(item.shortinfo, 50)
