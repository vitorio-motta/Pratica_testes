import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from biblioteca import Livro

#verificar se um livro inicia com a quantidade disponível correta;
def test_livro_inicializacao():
    livro = Livro("12345", "Título do Livro", "Autor do Livro", 5)
    assert livro.quantidade_disponivel == 5

test_livro_inicializacao()

#verificar se o método esta_disponivel() retorna corretamente True ou False
def test_esta_disponivel():
    livro = Livro("12345", "Título do Livro", "Autor do Livro", 5)
    assert livro.esta_disponivel() == True
    livro.quantidade_disponivel = 0
    assert livro.esta_disponivel() == False

test_esta_disponivel()

#verificar se o método emprestar() reduz a quantidade disponível
def test_emprestar():
    livro = Livro("12345", "Título do Livro", "Autor do Livro", 5)
    livro.emprestar()
    assert livro.quantidade_disponivel == 3
    livro.quantidade_disponivel = 0

test_emprestar()