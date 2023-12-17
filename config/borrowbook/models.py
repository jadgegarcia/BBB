from time import strftime

from django.db import models

from account.models import User

from book.models import Book, BigBadBook

# Create your models here.
from django.db import models

# Create your models here.


class BorrowBook(models.Model):
    borrow_book_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"Book: {self.book_id.__str__()}, Due Date: {self.due_date}"
