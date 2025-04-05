# -------------------------------- CREATING A TABLE NAMED PESSOAS -------------------------------- #

from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from django.utils import timezone

class Pessoas(models.Model):

    #Is the first item that counts: "Male"
    SEX_OPTIONS = [
        ("Male", "male"),
        ("Female", "female"),
        ("Other", "other"),
    ]


    cod_pessoa = models.AutoField(primary_key=True)
    age = models.IntegerField(
        null=False,                                                                 #null = null *This config is default*
        blank=False,                                                                #blank = ""
        validators=[MinValueValidator(0, message="Age cannot be negative")]
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        validators=[MinLengthValidator(3, message="Name must have at least 3 characters")]
    )
    sex = models.CharField(choices=SEX_OPTIONS, default='')
    married = models.BooleanField(default=False)
    birth = models.DateTimeField(null=False, blank=False)
    info = models.TextField(null=True,blank=True)

    #This fn is the identifier method of the class
    def __str__(self):
        return self.name
    
    #Set schema and table name related to this model
    class Meta:
        db_table = '"pessoas"."pessoas"'
