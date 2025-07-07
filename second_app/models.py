# from django.db import models

# class BorrowedBook(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     isbn = models.CharField(max_length=13, unique=True, help_text="International Standard Book Number")
#     borrower_name = models.CharField(max_length=100)
#     borrow_date = models.DateField(auto_now_add=True)
#     return_date = models.DateField(null=True, blank=True)
#     is_returned = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.title} by {self.author} (Borrowed by {self.borrower_name})"

#     class Meta:
#         verbose_name = "Borrowed Library Book"
#         verbose_name_plural = "Borrowed Library Books"
#         ordering = ['-borrow_date'] 