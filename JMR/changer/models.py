from django.db import models

# Create your models here.


class Post(models.Model):
    url_address = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.url_address


class Answer(models.Model):
    url_address = Post.url_address
    url_address_string = str(url_address)
    each_one_field = url_address_string.split("/")
    new_address = each_one_field[0]

    def __str__(self):
        return self.url_address, self.new_address
