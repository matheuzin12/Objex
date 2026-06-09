from django.contrib import admin
from .models import *


# ==========================
# INLINES
# ==========================

class LocalInline(admin.TabularInline):
    model = Local
    extra = 1


class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1


class EvidenciaInline(admin.TabularInline):
    model = Evidencia
    extra = 1


class HistoricoMovimentacaoInline(admin.TabularInline):
    model = HistoricoMovimentacao
    extra = 1


class ObjetoInline(admin.TabularInline):
    model = Objeto
    extra = 1


class ObjetoPessoaInline(admin.TabularInline):
    model = Objeto
    extra = 1


# ==========================
# ADMINS COM INLINES
# ==========================

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [LocalInline]


@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioInline,
        EvidenciaInline,
        HistoricoMovimentacaoInline,
    ]


@admin.register(CategoriaObjeto)
class CategoriaObjetoAdmin(admin.ModelAdmin):
    inlines = [ObjetoInline]


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [ObjetoPessoaInline]


# ==========================
# MODELOS SEM INLINES
# ==========================

admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(RegistroEncontrado)
admin.site.register(RegistroPerda)
admin.site.register(Setor)
admin.site.register(StatusObjeto)
admin.site.register(TipoObjeto)
admin.site.register(Local)
admin.site.register(Comentario)
admin.site.register(Evidencia)
admin.site.register(HistoricoMovimentacao)