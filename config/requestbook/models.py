from django.db import models
from account.models import User

# Create your models here.
class RequestBook(models.Model):
    request_book_id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)
    book_date = models.CharField(max_length=100)
    request_date = models.CharField(max_length=100)
    status = models.CharField(max_length=10, null=False, default="Pending")

    def __str__(self):
        return "Name: " + self.username.__str__() + ", Book: " + self.book_title.__str__() + ", Status: " + self.status