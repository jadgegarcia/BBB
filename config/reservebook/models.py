from django.db import models
from account.models import User
from book.models import Book
# Create your models here.

class ReserveBook(models.Model):
    reserve_book_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_date = models.DateField()

    def __str__(self):
        return f"Reserve Book Id: {self.reserve_book_id}, User: {self.username}"