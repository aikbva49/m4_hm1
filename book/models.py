from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=50, verbose_name='напишите название книги') 
    description = models.TextField(verbose_name='напишите аннотацию', blank=True) 
    image = models.ImageField(upload_to='books/', verbose_name='загрузите обложку в формате jpg или png', blank=True) 
    book_file = models.FileField(upload_to='books/', verbose_name='загрузите pdf-файл книги')
    
    GENRE_CHOICES = (
        ('Детектив', 'Детектив'),
        ('Хоррор', 'Хоррор'),
        ('Классика', 'Классика'),
   
    )
    
    quantity_pages = models.PositiveIntegerField(verbose_name='кол-во страниц', default=100, null=True) 
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default='Классиказн') 
    created_at = models.DateTimeField(auto_now_add=True) 
    author = models.CharField(max_length=100, verbose_name='напишите автора', default='Автор неизвестен') 
    price = models.PositiveIntegerField(verbose_name='укажите цену', default=0) 
    email_publisher = models.EmailField(verbose_name='почта издательства', null=True) 

    def __str__(self):
        return self.title
