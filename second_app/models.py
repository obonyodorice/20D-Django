from django.db import models

class BorrowedBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    borrower_name = models.CharField(max_length=100)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author} (Borrowed by {self.borrower_name})"

