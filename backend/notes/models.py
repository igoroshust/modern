from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания (когда событие попало в систему)
    
    class Meta:        
        # Параметр получения последней записи (для .latest() и .earliest())
        get_latest_by = 'created_at'
    
    def __str__(self):
        return self.title  # отображение в админке
    
