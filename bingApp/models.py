from django.db import models

class Employee(models.Model):
    VISA_STATUS =[('USC','US Citizen'), ('GC', 'Green Card'), ('H1B','H1B Visa'), ('H4','H4-EAD'),
                  ('L2','L2-EAD'),('TN','Canadian Visa'), ('OTH', 'OTHERS')]
    CLIENT_NAME = [('HEXA', 'Hexaware'), ('JPMC', 'JP Chase'), ('BOA', 'Bank of America'), ('FAN', 'Fannie Mae'), ('FED', 'Freddie Mac')
                   , ('IQV', 'IQVIA'), ('XLCAT', 'XL-Catlin'), ('AMRI', 'AmeriHealth'), ('EY', 'E&Y'), ('OTHS', 'Others')]
    STATUS_NAME = [('SUB', 'SUBMITTED'), ('L1SEL', 'L1-SELECTED'), ('REJ', 'REJECTED'), ('L1SCH', 'L1-SCHEDULED'),
                   ('L2SCH', 'L2-SCHEDULED'), ('L2SEL', 'L2-SELECTED'), ('OFFER', 'OFFERED'), ('STRT', 'STARTED'), 
                   ('L3SCH', 'L3-SCHEDULED'), ('L1REJ', 'L1-REJECTED'), ('L3SEL', 'L3-SELECTED'), ('L2REJ', 'L2-REJECTED')]
    SUBMITTED = [('ALEX', 'AL'), ('VIKI', 'VK'), ('SRIVENKAT', 'SRI'), ('OTHERS', 'OTHRS')]

    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.CharField(max_length=20)
    Location = models.CharField(max_length=50)
    Visa = models.CharField(max_length=30, choices=VISA_STATUS)
    Customer = models.CharField(max_length=100, choices=CLIENT_NAME)
    Poc_Name = models.CharField(max_length=100)
    Req_Name = models.CharField(max_length=50)
    Req_Number= models.CharField(max_length=15)
    Req_Location= models.CharField(max_length=50)
    Pay_Rate = models.FloatField(default=0)
    Bill_Rate = models.FloatField(default=0)
    Margin = models.FloatField(default=0)
    Submitted_Date = models.DateField()
    Status = models.CharField(max_length=20, choices=STATUS_NAME)
    Submitted_By = models.CharField(max_length=20, choices=SUBMITTED)
    Message = models.TextField(max_length=500)

    def __str__(self):
        return self.Name

# Create your models here.
