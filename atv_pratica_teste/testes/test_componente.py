import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from biblioteca import Livro, Usuario, Biblioteca

# cadastrar um livro e um usuário e realizar um empréstimo;
def test_realizar_emprestimo():
    biblioteca = Biblioteca()
    livro = Livro("12345", "Título do Livro", "Autor do Livro", 5)
    user = Usuario("001", "João", 3)
    
    biblioteca.cadastrar_livro(livro)
    biblioteca.cadastrar_usuario(user)
    
    resultado = biblioteca.realizar_emprestimo("001", "12345")
    assert resultado == "Empréstimo realizado com sucesso."

test_realizar_emprestimo()

#verificar se, após o empréstimo, a quantidade disponível do livro diminui;

def test_verificar_quantidade():   
    biblioteca = Biblioteca()
    livro = Livro("12345", "Título do Livro", "Autor do Livro", 5)
    user = Usuario("001", "João", 3)
    
    biblioteca.cadastrar_livro(livro)
    biblioteca.cadastrar_usuario(user)
    
    biblioteca.realizar_emprestimo("001", "12345")

    assert livro.quantidade_disponivel == 4

print("Testes de componentes aprovados.")




