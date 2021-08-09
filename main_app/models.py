from django.db import models


class User(models.Model):
    user_name = models.CharField(('Username'), max_length=100)
    user_image = models.CharField(('Image'), max_length=200, blank=True)
    user_age = models.CharField(('Age'), max_length=3)
    user_description = models.TextField(('Description'), max_length=255)


def __str__(self):
    return f'{self.name}'
# user = [
#     User('Lolo', 'image', 18, 'lorem ipsum'),
#     User('Sachi', 'image', 21, 'lorem ipsum'),
#     User('Raven', 'image', 22, 'lorem ipsum')
# ]
