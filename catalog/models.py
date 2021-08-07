from django.db import models
import uuid
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=150, help_text='Enter Genre')

    def __str__():
        return self.name


class Book(models.Model):
    #Fields
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null = True)
    summary = models.TextField(max_length=1000, help_text='Enter a Brief description')
    genre = models.ManyToManyField(Genre, help_text='Select genre for this book')

    #Meta

    #methods
    def __str__():
        return self.title

    def get_absolute_url():
        return reverse('book-detials', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique id')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__():
        return f'{self.id} {seld.book.title}'


class Author(models.Model):
    name = models.CharField(max_length=200, help_text='Enter author name')

    class Meta:
        ordering=['name']

    def __str__():
        return self.name

    def get_absolute_url():
        return reverse('author-details', args = [str(self.id)])
