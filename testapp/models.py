from django.db import models

class Student(models.Model):
    Book_Name = models.CharField(max_length=60)
    Book_Price = models.IntegerField()
    Book_code = models.IntegerField()
    
    
    

    def __str__(self):
        return self.Book_Name
