from django.db import models


class Layout(models.Model):
    html = models.TextField()


class Header(models.Model):
    unique_id = models.IntegerField(default=0)
    image = models.TextField()
    title = models.CharField(max_length=500)


class ContentData(models.Model):
    unique_id = models.IntegerField(default=0)
    layout_id = models.ForeignKey(Layout, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.TextField()
    title = models.TextField()

    def __str__(self):
        return self.layout_id.html
