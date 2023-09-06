from django.db import models

class portfolioModels(models.Model):
    first_name = models.CharField(max_length=225)
    email_address = models.EmailField()
    subject = models.CharField(max_length=255)
    msg = models.TextField()

    class Meta:
        db_table = 'portfolio_Table'
    

