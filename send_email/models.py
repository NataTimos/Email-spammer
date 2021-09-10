from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    # def __str__(self) -> str:
    #     return super().__str__()

    def __str__(self):
        return self.name
