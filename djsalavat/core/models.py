from django.db import models

class Contributor(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name
    
class SalavatCollection(models.Model):
    number = models.IntegerField(default=0)
    date_contributed = models.DateTimeField(auto_now_add=True)
    contributor = models.ForeignKey('Contributor', related_name='slavats', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.number} of salavats contributed by: {self.contributor} on {self.date_contributed}"