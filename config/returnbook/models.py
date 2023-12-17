from django.db import models
from account.models import User
from borrowbook.models import BorrowBook
# Create your models here.
class ReturnBook(models.Model):
    return_book_id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_book_id = models.ForeignKey(BorrowBook, on_delete=models.CASCADE)
    returnDate = models.DateField()
    condition = models.CharField(max_length=20)
    isOverdue = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_id.__str__() + " : " + self.borrow_book_id.__str__()

