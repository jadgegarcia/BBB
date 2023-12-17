from django.db import models

# Create your models here.


class Book(models.Model):
    isbn = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.title


class BigBadBook(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.isbn.__str__()
