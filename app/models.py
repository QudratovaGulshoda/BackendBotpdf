from django.db import models

# Create your models here.
class BotUser(models.Model):
    first_name = models.CharField(max_length=150,null=True,blank=True,verbose_name="First name",help_text="Enter name")
    username = models.CharField(max_length=150,null=True,blank=True,verbose_name="Username",help_text="Enter username",unique=True)
    telegram_id = models.CharField(max_length=20,unique=True,verbose_name="Telegram ID",help_text="Enter telegram ID")
    status = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.telegram_id
    class Meta:
        db_table = 'BotUser'
        managed = True
        verbose_name = 'BotUser'
        verbose_name_plural = 'BotUsers'