from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/')
    born_date = models.DateTimeField()

    def __str__(self):
        return self.name


class BookModel(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=250)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.title
