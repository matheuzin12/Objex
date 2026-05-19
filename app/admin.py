from django.contrib import admin
from .models import *


admin.site.register(Pessoa)
admin.site.register(Usuario)
admin.site.register(Funcionario)
admin.site.register(Instituicao)
admin.site.register(Local)
admin.site.register(CategoriaObjeto)
admin.site.register(StatusObjeto)
admin.site.register(Objeto)
admin.site.register(RegistroPerda)
admin.site.register(RegistroEncontrado)
admin.site.register(Comentario)
admin.site.register(Evidencia)
admin.site.register(HistoricoMovimentacao)