from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Perfil(models.Model):
    utilizador = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='profile_images/default.jpg', upload_to='profile_images')
    discord_id = models.CharField(max_length=30, blank=True, verbose_name="Discord")
    pontuacao = models.PositiveSmallIntegerField(default=0, verbose_name="Pontuação")

    class Meta:
        verbose_name_plural = "Perfis"


    def __str__(self):
        return f'{self.utilizador.username} Perfil'

    # Override the save method of the model
    def save(self, *args, **kwargs):
        super(Perfil, self).save(*args, **kwargs)
        img = Image.open(self.imagem.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.imagem.path) # Save it again and override the larger image


