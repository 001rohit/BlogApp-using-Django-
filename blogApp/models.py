from django.db import models

# Create your models here.
class blogApp(models.Model):
    title = models.CharField(max_length=50,blank=False)
    desc = models.TextField()
    img = models.ImageField(upload_to='myBlog')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title