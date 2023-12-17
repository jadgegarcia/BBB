from datetime import date

from django.db import models

from account.models import User
from book.models import Book

# Create your models here.


class DonationBook(models.Model):
    donation_book_id = models.BigAutoField(primary_key=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    donation_date = models.DateField(default=date.today)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "Donor: " + self.customer_id.__str__() + ", Book: " + self.book_id.__str__()

