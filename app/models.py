from django.db import models


class Pessoa(models.Model):
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

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class Usuario(models.Model):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa do usuário"
    )

    data_cadastro = models.DateField(
        verbose_name="Data de cadastro"
    )

    def __str__(self):
        return self.pessoa.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


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

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"


class Funcionario(models.Model):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa do funcionário"
    )

    cargo = models.CharField(
        max_length=100,
        verbose_name="Cargo do funcionário"
    )

    instituicao = models.ForeignKey(
        Instituicao,
        on_delete=models.CASCADE,
        verbose_name="Instituição do funcionário"
    )

    def __str__(self):
        return self.pessoa.nome

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"


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

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        verbose_name="Usuário do objeto"
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

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )

    data_perda = models.DateField(
        verbose_name="Data da perda"
    )

    descricao = models.TextField(
        verbose_name="Descrição da perda"
    )

    def __str__(self):
        return f"{self.objeto} - {self.usuario}"

    class Meta:
        verbose_name = "Registro de Perda"
        verbose_name_plural = "Registros de Perdas"


class RegistroEncontrado(models.Model):
    objeto = models.ForeignKey(
        Objeto,
        on_delete=models.CASCADE,
        verbose_name="Objeto encontrado"
    )

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE,
        verbose_name="Funcionário"
    )

    data_encontro = models.DateField(
        verbose_name="Data do encontro"
    )

    observacao = models.TextField(
        verbose_name="Observação"
    )

    def __str__(self):
        return f"{self.objeto} - {self.funcionario}"

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

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
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

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE,
        verbose_name="Funcionário"
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