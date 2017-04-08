from django.db import models
from django.conf import settings

def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)] #8글자 랜덤 초이스
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    # monkey/abdcefgh.png
    return '{}/{}.{}'.format(instance.owner.username, pid, extension)

class Photo(models.Model):
    image = models.ImageField(upload_to = user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    thumbnail_image = models.ImageField(blank = True)
    comment = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now_add = True)
