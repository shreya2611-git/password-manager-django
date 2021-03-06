from django.db import models

from ..accounts.models import User
from ..core.models import GroupUserPermission
# Create your models here.

class UserKey(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    public_key = models.TextField()
    private_key = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

class GroupUserKey(models.Model):
    key = models.ForeignKey(UserKey)
    group_user = models.ForeignKey(GroupUserPermission)
    public_key = models.TextField()
    private_key = models.TextField()
    creation = models.DateTimeField(auto_now=True)
