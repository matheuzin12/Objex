from django.contrib import admin
from django.urls import include, path
from app.views import *
urlpatterns = [
path('admin/', admin.site.urls),
path('', IndexView.as_view(), name='Index'),
path('cidade/', CidadesView.as_view()),
path('bairro/', BairrosView.as_view()),
path('instituicao/', InstituicoesView.as_view()),
path('setor/', SetoresView.as_view()),
path('local/', LocaisView.as_view()),
path('pessoa/', PessoasView.as_view()),
path('categoriaobjeto/', CategoriasObjetoView.as_view()),
path('tipoobjeto/', TiposObjetoView.as_view()),
path('statusobjeto/', StatusObjetoView.as_view()),
path('objeto/', ObjetosView.as_view()),
path('registroperda/', RegistrosPerdaView.as_view()),
path('registroencontrado/', RegistrosEncontradoView.as_view()),
path('evidencia/', EvidenciasView.as_view()),
path('comentario/', ComentariosView.as_view()),
path('historicomovimentacao/', HistoricosMovimentacaoView.as_view()),
]