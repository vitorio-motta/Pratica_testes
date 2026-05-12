from biblioteca import Biblioteca, Livro, Usuario


def executar_exemplo():
    biblioteca = Biblioteca()

    livro = Livro(
        isbn="978-85-7522-726-4",
        titulo="Introdução à Programação com Python",
        autor="Nilo Ney Coutinho Menezes",
        quantidade_total=2
    )

    usuario = Usuario(
        id_usuario="U001",
        nome="Ana Souza",
        limite_emprestimos=2
    )

    biblioteca.cadastrar_livro(livro)
    biblioteca.cadastrar_usuario(usuario)

    print("Estado inicial:")
    print("Livro:", livro.titulo)
    print("Quantidade disponível:", livro.quantidade_disponivel)
    print("Empréstimos ativos do usuário:", usuario.emprestimos_ativos)

    print("\nRealizando empréstimo:")
    resultado_emprestimo = biblioteca.realizar_emprestimo("U001", "978-85-7522-726-4")
    print(resultado_emprestimo)

    print("\nEstado após empréstimo:")
    print("Quantidade disponível:", livro.quantidade_disponivel)
    print("Empréstimos ativos do usuário:", usuario.emprestimos_ativos)

    print("\nRealizando devolução:")
    resultado_devolucao = biblioteca.devolver_livro("U001", "978-85-7522-726-4")
    print(resultado_devolucao)

    print("\nEstado após devolução:")
    print("Quantidade disponível:", livro.quantidade_disponivel)
    print("Empréstimos ativos do usuário:", usuario.emprestimos_ativos)


if __name__ == "__main__":
    executar_exemplo()