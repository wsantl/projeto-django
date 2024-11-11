from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)  # A data em que o post foi criado
    autor_email = models.EmailField()  # O email do autor do post
    publicado = models.BooleanField(default=False)  # Para indicar se o post foi publicado ou não

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_publicacao']  # Ordenar posts pela data de publicação (mais recentes primeiro)
