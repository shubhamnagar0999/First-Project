from django.db import models
from django.db.models.fields.files import ImageField
from froala_editor.fields import FroalaField




#category 
class Catergory(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'category/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title

#post
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = FroalaField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Catergory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')

    def __str__(self) :
        return self.title