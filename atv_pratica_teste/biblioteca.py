class Livro:
    def __init__(self, isbn, titulo, autor, quantidade_total):
        if quantidade_total < 0:
            raise ValueError("A quantidade total não pode ser negativa.")

        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.quantidade_total = quantidade_total
        self.quantidade_disponivel = quantidade_total

    def esta_disponivel(self):
        return self.quantidade_disponivel > 0

    def emprestar(self):
        if not self.esta_disponivel():
            raise ValueError("Livro indisponível.")

        self.quantidade_disponivel -= 1

    def devolver(self):
        if self.quantidade_disponivel >= self.quantidade_total:
            raise ValueError("Todos os exemplares já estão disponíveis.")

        self.quantidade_disponivel += 1


class Usuario:
    def __init__(self, id_usuario, nome, limite_emprestimos=3):
        if limite_emprestimos <= 0:
            raise ValueError("O limite de empréstimos deve ser maior que zero.")

        self.id_usuario = id_usuario
        self.nome = nome
        self.limite_emprestimos = limite_emprestimos
        self.emprestimos_ativos = 0

    def pode_emprestar(self):
        return self.emprestimos_ativos < self.limite_emprestimos

    def registrar_emprestimo(self):
        if not self.pode_emprestar():
            raise ValueError("Usuário atingiu o limite de empréstimos.")

        self.emprestimos_ativos += 1

    def registrar_devolucao(self):
        if self.emprestimos_ativos <= 0:
            raise ValueError("Usuário não possui empréstimos ativos.")

        self.emprestimos_ativos -= 1


class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.ativo = True

    def finalizar(self):
        if not self.ativo:
            raise ValueError("Empréstimo já finalizado.")

        self.ativo = False


class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.emprestimos = []

    def cadastrar_livro(self, livro):
        self.livros[livro.isbn] = livro

    def cadastrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario

    def realizar_emprestimo(self, id_usuario, isbn):
        usuario = self.usuarios.get(id_usuario)
        livro = self.livros.get(isbn)

        if usuario is None:
            return "Usuário não encontrado."

        if livro is None:
            return "Livro não encontrado."

        if not livro.esta_disponivel():
            return "Livro indisponível."

        if not usuario.pode_emprestar():
            return "Usuário atingiu o limite de empréstimos."

        livro.emprestar()
        usuario.registrar_emprestimo()

        emprestimo = Emprestimo(usuario, livro)
        self.emprestimos.append(emprestimo)

        return "Empréstimo realizado com sucesso."

    def devolver_livro(self, id_usuario, isbn):
        for emprestimo in self.emprestimos:
            mesmo_usuario = emprestimo.usuario.id_usuario == id_usuario
            mesmo_livro = emprestimo.livro.isbn == isbn

            if mesmo_usuario and mesmo_livro and emprestimo.ativo:
                emprestimo.finalizar()
                emprestimo.livro.devolver()
                emprestimo.usuario.registrar_devolucao()

                return "Livro devolvido com sucesso."

        return "Empréstimo ativo não encontrado."