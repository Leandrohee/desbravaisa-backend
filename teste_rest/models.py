from django.db import models

class Pessoas(models.Model):
    cod_pessoa = models.AutoField(primary_key=True)
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    male = models.BooleanField()
    married = models.BooleanField(default=False)
    birth = models.DateTimeField()

    #This fn is the identifier method of the class
    def __str__(self):
        return self.name
    
    #Set schema and table name
    class Meta:
        db_table = '"pessoas"."pessoas"'
