from django.db import models


# Crie a classe Profile.
# A classe Profile deve herdar os models do Django.
# A classe Profile deve ter as propriedades: name, github, linkedin, e bio.
class Profile(models.Model):
    # A propriedade name deve ser um campo de caracteres com um tamanho máximo de 100 caracteres.
    name = models.CharField(max_length=50)
    # As propriedades github, linkedin devem ser campos de URL.
    github = models.URLField()
    linkedin = models.URLField()
    # A propriedade bio deve ser um campo de texto sem tamanho máximo definido.
    bio = models.TextFieldField()

    # O método __str__ da classe Profile deve retornar a propriedade name do perfil criado.
    def __str__(self):
        return f"{self.name}"


# As propriedades devem ser:
# name: Campo de caracteres, com tamanho máximo de 50 caracteres.
# github: Campo de URL.
# linkedin: Campo de URL.
# bio: Campo de texto, sem tamanho máximo definido.
# As propriedades name, github, linkedin, e bio não devem aceitar informações vazias ou maiores que 500 caracteres.
