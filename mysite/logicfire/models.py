from django.db import models

class Lesson(models.Model):  # ← SHU YERDA BO‘LISHI KERAK
    title = models.CharField(max_length=200)
    content = models.TextField()
