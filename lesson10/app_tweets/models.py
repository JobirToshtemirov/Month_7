from django.db import models
from rest_framework.authtoken.admin import User


class TweetModel(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tweet = models.CharField(max_length=140)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tweet

    class Meta:
        verbose_name_plural = 'Tweets'
        verbose_name = 'Tweet'


class FollowerModel(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.from_user

    class Meta:
        verbose_name = "Follower"
        verbose_name_plural = "Followers"
        unique_together = ('user', 'code')
