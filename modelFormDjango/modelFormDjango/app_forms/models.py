from django.db import models

SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class Client(models.Model):
    name = models.CharField(max_length=30)
    dt_birth = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def formatted_date(self):
        return self.dt_birth.strftime('%d%m%Y')
