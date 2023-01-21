from django.db import models


def upload_path(instance, filename):
    return '/'.join(['photos', str(instance.photo_name), filename])


# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Image(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to=upload_path, max_length=100)
    photo_name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.photo_name

    def save_photo(self):
        self.save()

    @classmethod
    def search_by_album(cls, search_term):
        photo = cls.objects.filter(album__name__icontains=search_term)
        return photo

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    class Meta:
        ordering = ['date']
