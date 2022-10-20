from django.db import models


class FeedbackModel(models.Model):
    client_id = models.AutoField(primary_key=True)

    client_name = models.CharField(max_length=120)
    client_phone_number = models.CharField(max_length=20)
    task_brief = models.CharField(max_length=240)

    logo = models.BooleanField()
    presentation = models.BooleanField()
    social_networks = models.BooleanField()
    identity = models.BooleanField()
    infographics = models.BooleanField()
    offline_adds = models.BooleanField()

    task_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded at")
    task_accomplishment = models.BooleanField(default=False)

    def __str__(self):
        return self.client_name
