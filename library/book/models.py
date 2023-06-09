from django.db import models

# Create your models here.

class Book(models.Model):
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title} by {self.author}'

    @property
    def likes_count(self):
        return self.likes.count()



class Like(models.Model):
    user = models.ForeignKey('account.UserAccount', on_delete=models.CASCADE, related_name='likes')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} likes {self.book}'

    class Meta:
        unique_together = ('user', 'book')
