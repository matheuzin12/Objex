from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})


class BairrosView(View):
    def get(self, request, *args, **kwargs):
        bairros = Bairro.objects.all()
        return render(request, 'bairro.html', {'bairros': bairros})


class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicao.html',
                      {'instituicoes': instituicoes})


class SetoresView(View):
    def get(self, request, *args, **kwargs):
        setores = Setor.objects.all()
        return render(request, 'setor.html',
                      {'setores': setores})


class LocaisView(View):
    def get(self, request, *args, **kwargs):
        locais = Local.objects.all()
        return render(request, 'local.html',
                      {'locais': locais})


class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html',
                      {'pessoas': pessoas})


class CategoriasObjetoView(View):
    def get(self, request, *args, **kwargs):
        categorias = CategoriaObjeto.objects.all()
        return render(request, 'categoriaobjeto.html',
                      {'categorias': categorias})


class TiposObjetoView(View):
    def get(self, request, *args, **kwargs):
        tipos = TipoObjeto.objects.all()
        return render(request, 'tipoobjeto.html',
                      {'tipos': tipos})


class StatusObjetoView(View):
    def get(self, request, *args, **kwargs):
        status_objetos = StatusObjeto.objects.all()
        return render(request, 'statusobjeto.html',
                      {'status_objetos': status_objetos})


class ObjetosView(View):
    def get(self, request, *args, **kwargs):
        objetos = Objeto.objects.all()
        return render(request, 'objeto.html',
                      {'objetos': objetos})


class RegistrosPerdaView(View):
    def get(self, request, *args, **kwargs):
        registros = RegistroPerda.objects.all()
        return render(request, 'registroperda.html',
                      {'registros': registros})


class RegistrosEncontradoView(View):
    def get(self, request, *args, **kwargs):
        registros = RegistroEncontrado.objects.all()
        return render(request, 'registroencontrado.html',
                      {'registros': registros})


class EvidenciasView(View):
    def get(self, request, *args, **kwargs):
        evidencias = Evidencia.objects.all()
        return render(request, 'evidencia.html',
                      {'evidencias': evidencias})


class ComentariosView(View):
    def get(self, request, *args, **kwargs):
        comentarios = Comentario.objects.all()
        return render(request, 'comentario.html',
                      {'comentarios': comentarios})


class HistoricosMovimentacaoView(View):
    def get(self, request, *args, **kwargs):
        historicos = HistoricoMovimentacao.objects.all()
        return render(request, 'historicomovimentacao.html',
                      {'historicos': historicos})