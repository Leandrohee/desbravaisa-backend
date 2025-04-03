from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from django.utils import timezone

class Pessoas(models.Model):
    cod_pessoa = models.AutoField(primary_key=True)
    age = models.IntegerField(
        validators=[MinValueValidator(0, message="Age cannot be negative")]
    )
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3, message="Name must have at least 3 characters")]
    )
    male = models.BooleanField()
    married = models.BooleanField(default=False)
    birth = models.DateTimeField(default=timezone.now)

    #This fn is the identifier method of the class
    def __str__(self):
        return self.name
    
    #Set schema and table name
    class Meta:
        db_table = '"pessoas"."pessoas"'
