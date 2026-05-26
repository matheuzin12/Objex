from django.db import models


class Cidade(models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome da cidade"
    )

    uf = models.CharField(
        max_length=2,
        verbose_name="UF"
    )

    def __str__(self):
        return f"{self.nome} - {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Bairro(models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do bairro"
    )

    cidade = models.ForeignKey(
        Cidade,
        on_delete=models.CASCADE,
        verbose_name="Cidade do bairro"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"


class Pessoa(models.Model):

    OCUPACAO_CHOICES = (
        ('usuario', 'Usuário'),
        ('funcionario', 'Funcionário'),
        ('admin', 'Administrador'),
    )

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome da pessoa"
    )

    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF da pessoa"
    )

    telefone = models.CharField(
        max_length=20,
        verbose_name="Telefone da pessoa"
    )

    email = models.EmailField(
        verbose_name="Email da pessoa"
    )

    ocupacao = models.CharField(
        max_length=20,
        choices=OCUPACAO_CHOICES,
        verbose_name="Ocupação da pessoa"
    )

    data_cadastro = models.DateField(
        verbose_name="Data de cadastro"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class Instituicao(models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome da instituição"
    )

    tipo = models.CharField(
        max_length=100,
        verbose_name="Tipo da instituição"
    )

    telefone = models.CharField(
        max_length=20,
        verbose_name="Telefone da instituição"
    )

    email = models.EmailField(
        verbose_name="Email da instituição"
    )

    endereco = models.CharField(
        max_length=200,
        verbose_name="Endereço da instituição"
    )

    cidade = models.ForeignKey(
        Cidade,
        on_delete=models.CASCADE,
        verbose_name="Cidade da instituição"
    )

    bairro = models.ForeignKey(
        Bairro,
        on_delete=models.CASCADE,
        verbose_name="Bairro da instituição"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"


class Setor(models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do setor"
    )

    descricao = models.TextField(
        verbose_name="Descrição do setor"
    )

    instituicao = models.ForeignKey(
        Instituicao,
        on_delete=models.CASCADE,
        verbose_name="Instituição do setor"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"


class Local(models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do local"
    )

    descricao = models.TextField(
        verbose_name="Descrição do local"
    )

    instituicao = models.ForeignKey(
        Instituicao,
        on_delete=models.CASCADE,
        verbose_name="Instituição do local"
    )

    setor = models.ForeignKey(
        Setor,
        on_delete=models.CASCADE,
        verbose_name="Setor do local"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"


class CategoriaObjeto(models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome da categoria"
    )

    descricao = models.TextField(
        verbose_name="Descrição da categoria"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria do Objeto"
        verbose_name_plural = "Categorias dos Objetos"


class TipoObjeto(models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do tipo"
    )

    descricao = models.TextField(
        verbose_name="Descrição do tipo"
    )

    categoria = models.ForeignKey(
        CategoriaObjeto,
        on_delete=models.CASCADE,
        verbose_name="Categoria do tipo"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Objeto"
        verbose_name_plural = "Tipos de Objetos"


class StatusObjeto(models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do status"
    )

    descricao = models.TextField(
        verbose_name="Descrição do status"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Status do Objeto"
        verbose_name_plural = "Status dos Objetos"


class Objeto(models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do objeto"
    )

    descricao = models.TextField(
        verbose_name="Descrição do objeto"
    )

    cor = models.CharField(
        max_length=50,
        verbose_name="Cor do objeto"
    )

    marca = models.CharField(
        max_length=100,
        verbose_name="Marca do objeto"
    )

    imagem = models.ImageField(
        upload_to='objetos/',
        verbose_name="Imagem do objeto"
    )

    data_registro = models.DateField(
        verbose_name="Data de registro"
    )

    categoria = models.ForeignKey(
        CategoriaObjeto,
        on_delete=models.CASCADE,
        verbose_name="Categoria do objeto"
    )

    tipo = models.ForeignKey(
        TipoObjeto,
        on_delete=models.CASCADE,
        verbose_name="Tipo do objeto"
    )

    status = models.ForeignKey(
        StatusObjeto,
        on_delete=models.CASCADE,
        verbose_name="Status do objeto"
    )

    local = models.ForeignKey(
        Local,
        on_delete=models.CASCADE,
        verbose_name="Local do objeto"
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa responsável"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Objeto"
        verbose_name_plural = "Objetos"


class RegistroPerda(models.Model):

    objeto = models.ForeignKey(
        Objeto,
        on_delete=models.CASCADE,
        verbose_name="Objeto perdido"
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    data_perda = models.DateField(
        verbose_name="Data da perda"
    )

    descricao = models.TextField(
        verbose_name="Descrição da perda"
    )

    def __str__(self):
        return f"{self.objeto} - {self.pessoa}"

    class Meta:
        verbose_name = "Registro de Perda"
        verbose_name_plural = "Registros de Perdas"


class RegistroEncontrado(models.Model):

    objeto = models.ForeignKey(
        Objeto,
        on_delete=models.CASCADE,
        verbose_name="Objeto encontrado"
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa responsável"
    )

    data_encontro = models.DateField(
        verbose_name="Data do encontro"
    )

    observacao = models.TextField(
        verbose_name="Observação"
    )

    def __str__(self):
        return f"{self.objeto} - {self.pessoa}"

    class Meta:
        verbose_name = "Registro Encontrado"
        verbose_name_plural = "Registros Encontrados"


class Comentario(models.Model):

    texto = models.TextField(
        verbose_name="Texto do comentário"
    )

    data = models.DateField(
        verbose_name="Data do comentário"
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    objeto = models.ForeignKey(
        Objeto,
        on_delete=models.CASCADE,
        verbose_name="Objeto"
    )

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"


class Evidencia(models.Model):

    imagem = models.ImageField(
        upload_to='evidencias/',
        verbose_name="Imagem da evidência"
    )

    descricao = models.TextField(
        verbose_name="Descrição da evidência"
    )

    objeto = models.ForeignKey(
        Objeto,
        on_delete=models.CASCADE,
        verbose_name="Objeto"
    )

    def __str__(self):
        return f"Evidência - {self.objeto}"

    class Meta:
        verbose_name = "Evidência"
        verbose_name_plural = "Evidências"


class Notificacao(models.Model):

    mensagem = models.TextField(
        verbose_name="Mensagem"
    )

    data_envio = models.DateField(
        verbose_name="Data de envio"
    )

    visualizada = models.BooleanField(
        verbose_name="Notificação visualizada"
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    def __str__(self):
        return self.mensagem

    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"


class SolicitacaoPosse(models.Model):

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    objeto = models.ForeignKey(
        Objeto,
        on_delete=models.CASCADE,
        verbose_name="Objeto"
    )

    descricao = models.TextField(
        verbose_name="Descrição da solicitação"
    )

    data_solicitacao = models.DateField(
        verbose_name="Data da solicitação"
    )

    aprovada = models.BooleanField(
        verbose_name="Solicitação aprovada"
    )

    def __str__(self):
        return f"{self.pessoa} - {self.objeto}"

    class Meta:
        verbose_name = "Solicitação de Posse"
        verbose_name_plural = "Solicitações de Posse"


class HistoricoMovimentacao(models.Model):

    objeto = models.ForeignKey(
        Objeto,
        on_delete=models.CASCADE,
        verbose_name="Objeto"
    )

    status_anterior = models.ForeignKey(
    StatusObjeto,
    on_delete=models.CASCADE,
    related_name='status_anterior',
    verbose_name="Status anterior"
    )

    status_novo = models.ForeignKey(
    StatusObjeto,
    on_delete=models.CASCADE,
    related_name='status_novo',
    verbose_name="Novo status"
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa responsável"
    )

    data = models.DateField(
        verbose_name="Data da movimentação"
    )

    descricao = models.TextField(
        verbose_name="Descrição da movimentação"
    )

    def __str__(self):
        return f"{self.objeto} - {self.data}"

    class Meta:
        verbose_name = "Histórico de Movimentação"
        verbose_name_plural = "Históricos de Movimentações"