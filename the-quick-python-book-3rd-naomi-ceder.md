---
theme: "white"
customTheme : "notes"
transition: "none"
highlightTheme: "tomorrow"
center: false
controls: false
---

# The Quick Python Book 3rd - Naomi Ceder

---

# Pontos Fortes x Pontos Fracos

Otário!

---

Pontos fortes

* Fácil de usar
* Expressiva:

```python
# Swap entre duas variáveis
a = 10
b = 20
a, b = b, a
```

* Legível
* Tem (bibliotecas) baterias incluídas
* Multi-plataforma

---

Pontos fracos

* Não tão rápida quanto C
* Tem menos bibliotecas - em alguns nichos - do que linguagens como C, Java...
* Não há verificação de tipos em *compile time*
* Não tem bom suporte em mobile
* GIL atrapalha concorrência

---

# Python em 10 minutos ou menos

---

Tipos numéricos

```python
# Inteiros
a = 3
b = -10

# O tamanho dos inteiros é limitado apenas pela memória disponível
c = 300102020101020120021 ^ 10

# Pontos Flutuantes
pi = 3.14

# Booleanos
t = True
z = False
```

---

Operações com inteiros:

```python
>>> # Operacoes
>>> x = 5 + 2 - 10 + 35
>>> x
32
>>> 
>>> # Divisao normal
... 5 / 2
2.5
>>> 
>>> # Divisao descaranto a parte decimal
... 5 // 2
2
>>> # Resto da divisao
... 5 % 2
1
>>> # Resultado e resto da divisao
... divmod(5, 2)
(2, 1)
>> # Exponenciação
>>> 2 ** 8
256
>>> 100 ** 100
100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> 
```

---

Operações com pontos flutuantes:

```python
>>> x = 4.23 * 7.15
>>> x
30.244500000000006
>>> 
>>> 15.67 - 19.8
-4.130000000000001
>>> 
>>> 3.45 ** 5.6
1027.5120705982902
>>> 
```

---

Algums funções *built-in* e do módulo *math*:

```python
>>> x = 3.49
>>> round(x) # built-in, sempre disponível, não precisa importar nada
3
>>> 
>>> import math
>>> math.ceil(x)
4
>>> 
>>> math.floor(x)
3
```

---

Todo arquivo Python é um módulo. 

Os atributos definidos no módulo podem ser acessados a partir de outro módulo através de `import`. 

Feito o *import*, você pode acessar os atributos através da sintaxe: `module.function(arguments)`.

---

Booleans:

```python
>>> x = True
>>> y = False
>>> 
>>> # Negando usando "not"
>>> not x
False
>>> 
>>> not y
True
>>> 
>>> # Booleans são nomes para os inteiros 0 e 1
>>> # True == 1, False == 0
... 
>>> x + x
2
>>> x + y
1
>>> y + y
0
>>> 
```

---

Listas

```python
>>> # Lista vazia
... l1 = []
>>> 
>>> # Podem conter qualque tipo
... l2 = [1, 3.4, "aloha", [7, 6, 5]]
>>> l2 = [1, 3.4, "aloha", [7, 6, 5]]
>>> 
>>> # Indexando da esquerda pra direita (começa em 0)
... l2[0]
1
>>> l2[1]
3.4
>>> 
>>> # Indexando da direita pra esquerda (começa em -1)
... l2[-1]
[7, 6, 5]
>>> l2[-2]
'aloha'
>>> 

>>> # Slices. A primeira posição é inclusiva, a segunda não. 
>>> # l2[0:2] = l2[0], l2[1]...
... l2[0:2]
[1, 3.4]
>>> l2[1:3]
[3.4, 'aloha']
>>> l2[3:4]
[[7, 6, 5]]
>>>

# Se omitir o primeiro índice, o slice começa do primeiro objeto
>>> l2[:3]
[1, 3.4, 'aloha']
>>> 

# Se omitir o segundo índice, o slice irá até o final
>>> l2[1:]
[3.4, 'aloha', [7, 6, 5]]
>>> l2[2:]
['aloha', [7, 6, 5]]
>>> 
```

---

Modificando listas:

```python
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> # Alterando um item
... x[0] = "um"
>>> x
['um', 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> # Alterando um slice. A lista cresce ou decresce automaticamente
... x[5:7] = [6.0, 6.5, 7.0]
>>> x
['um', 2, 3, 4, 5, 6.0, 6.5, 7.0, 8, 9]
>>> 
```

---

Algumas operações e funções que podem lidar com listas:

```python
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> # Tamanho - len()
... len(x)
9
>>> 
>>> # Inverter
... x.reverse()
>>> x
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
>>> # Ordenar
... x.sort()
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> # del um elemento
... del x[0]
>>> x
[2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> # + adiciona uma lista ao final de outra, criando uma nova lista
>>> # não modifica as listas envolvidas
>>> y = x + [10]
>>> y
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x
[2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> # * cria uma nova lista repetindo a lista esquerda
>>> # a lista original não é modificada
>>> z = x * 2
>>> z
[2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
```

---

Tuplas - similar a listas, mas são imutáveis, não permitem alteração por indexação / slice

```python
>>> a = ()
>>> a
()
>>> # Declarar uma tupla de apenas um item, requer uma vírgula
... b = (2,)
>>> b
(2,)
>>> 
>>> # Tuplas podem conter vários tipos também
... c = (1, "two", 3.14)
>>> c
(1, 'two', 3.14)
>>>
>>> # Suportam os operadores + e * pois eles criam _novas_ tuplas
... c
(1, 'two', 3.14)
>>> 
>>> d = c + (10,)
>>> d
(1, 'two', 3.14, 10)
>>> 
>>> e = d * 2
>>> e
(1, 'two', 3.14, 10, 1, 'two', 3.14, 10)
>>> 
>>> c
(1, 'two', 3.14)
>>> 
```

---

Conversão entre listas e tuplas

```python
>>> l = [1, 2, 3]
>>> t = (4, 5, 6)
>>> 
>>> # tuple(list) converte uma lista para uma tupla
... z = tuple(l)
>>> z
(1, 2, 3)
>>> 
>>> # list(tuple) converte uma tupla para uma lista
... x = list(t)
>>> x
[4, 5, 6]
```

---

Strings

```python
>>> # Diversas maneiras de declarar
... a = "aloha"
>>> b = 'bacon'
>>> c = """
... a 
... multiline
... string
... """
>>> d = '''
... he said "i dont believe"
... she said "ok!"
... '''

>>> # Podem conter caracteres especiais
... z = "a\nteste\n\tcaracteres"
>>> print(z)
a
teste
        caracteres
>>> 

>>> # Sao imutaveis, mas suportam varias operacoes disponiveis para listas.
... # Voce só não consegue modificá-las usando indexacação ou slices
... a = "aloha"
>>> a
'aloha'
>>> 
>>> b = a + "bacon"
>>> b
'alohabacon'
>>> 
>>> a
'aloha'
>>> 
>>> c = a * 3
>>> c
'alohaalohaaloha'
>>> 
>>> len(a)
5
```

---

Ao usar `print(objeto)` o objeto é convertido para *string*

```python
>>> print(3.14)
3.14
>>> print(10)
10
>>> print(True)
True
>>> 
```

---

Dicionários `dict()`:

```python
>>> # Dicionários são hashmaps de chave e valor
... d = {
...     "nome": "Joao",
...     "idade": 21
... }
>>> d
{'nome': 'Joao', 'idade': 21}
>>> 
>>> # len retorna o número de pares chave/valor no dicionário
... len(d)
2
>>> 
>>> # você pode acessar um dicionário indexando-o por uma chave
... d["nome"]
'Joao'
>>> 
>>> # você pode usar o método .get para pegar um valor ou obter um default se não existir
... d.get("sobrenome", "Silva")
'Silva'
>>> 
>>> # Você pode modificar um dicionário por indexação também
... d["nome"] = "Paulo"
>>> d
{'nome': 'Paulo', 'idade': 21}
>>> 
>>> # Chaves não podem ser mutáveis
... d[['s', 'p', 'a', 'm']] = 'bacon'
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: unhashable type: 'list'
>>> 
```

---

Conjuntos `set()`

```python
>>> # Sets / Conjuntos são agrupamentos não ordenados de objetos (de qualquer tipo) únicos
... x = set([1, 2, 3, 1, 3, 5]) # Note o 1 e o 3 repetidos, serão removidos no set criado
>>> x
{1, 2, 3, 5}
>>> 
>>> # Sets são usados em verificações de pertencimento
... 1 in x
True
>>> 2 in x
True
>>> 10 in x
False
>>> 
```

---

Arquivos:

```python
>>> # Arquivos em Python estão acessíveis através da função open()
>>> # No exemplo abaixo, abrimos um arquivo para escrita, 'w' write
>>> f = open('arquivo.txt', 'w')
>>> f.write('Aloha\n') # Lembre-se de colocar a quebra de linha no final
6
>>> f.write('Spam\n')
5
>>> f.close() # E de fechar o arquivo! Liberando-o pro SO
>>> 
>>> # Para abrir para leitura, é similar, mas usamos a diretiva 'r'
>>> f2 = open('arquivo.txt', 'r')
>>> linha1 = f2.readline()
>>> linha2 = f2.readline()
>>> print(linha1, linha2)
Aloha
 Spam

>>> f2.close()
>>> 
>>> # O módulo "os" permite realizar operações envolvendo diretórios
>>> import os

>>> # Pegando o diretório corrente
... os.getcwd()
'/tmp'
>>> 
>>> # Mudando de diretório
>>> os.chdir(os.path.join('/home', 'rnetonet'))
>>> os.getcwd()
'/home/rnetonet'
>>> 
>>> # Usando um caminho absoluto, ainda podemos acessar o arquivo
>>> # Pode omitir o 'r', leitura é o comportamento padrão
>>> f3 = open(os.path.join('/tmp', 'arquivo.txt')) 
>>> print(f3.readline())
Aloha

>>> print(f3.readline())
Spam

>>> f3.close()
>>> 
```

---

Estruturas de controle de fluxo

```python
>>> # Python tem diversas maneiras de expressar valores Booleanos:
... # Valores que se igualam a False
... False
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(None)
False

# Toda sequência vazia é considerada como False em Python
>>> bool([])
False
>>> bool({})
False
>>> bool(set())
False
>>>
>>> bool('')
False
>>> 

>>> # Tudo diferente desses valores (False, None, zero e sequências vazias) é considerado True
... True
True
>>> bool(1)
True
>>> bool(-1)
True
>>> bool("X")
True
>>> bool([9])
True
>>> 
```

---

Operações de comparação lógica:

```python
>>> # Igualdade, diferença, maior que, menor que...
... 10 == 10
True
>>> 
>>> 11 != 343
True
>>> 
>>> 15 > 10
True
>>> 
>>> 10 < 15
True
>>> 
>>> 18 <= 20
True
>>> 
>>> 25 >= 14
True
>>> 

>>> # Negação pode ser obtido através do not antes da comparação
>>> 10 == 10
True
>>> not 10 == 10
False
>>> 
>>> 100 == 999
False
>>> not 100 == 990
True
>>> 


>>> # Contido (in), não contido (not in)
>>> 1 in [1, 2, 3]
True
>>> 
>>> 10 not in [1, 2, 3]
True
>>> 
```

---

`if / elif / else`

```python
>>> x = 10
>>> y = 99
>>> 
>>> # Primeiro tenta-se o if
>>> if x > 20:
...     print('Primeiro caso')
... # Depois, todas clausulas elif. Essas claúsulas são opcionais e podem ter várias
... elif y > 100:
...     print('Segundo caso')
... # Se nenhuma der match, executa o else (que é opcional)
... else:
...     print('Nenhum deu match')
... 
Nenhum deu match
>>> 
```

---

`while`:

```python
>>> # Executa até a condição tornar-se falsa
>>> x = 10
>>> while x > 0:
...     print(x)
...     x = x - 1
... 
10
9
8
7
6
5
4
3
2
1
>>> 

>>> x = 3
>>> while x: # lembre-se que zero é considerado falso!
...     print(x)
...     x = x - 1
... 
3
2
1
>>> 

>>> # Você pode usar a instrução break para sair do loop
>>> x = 0
>>> while x <= 100:
...     if x == 10:
...         break
...     
...     print(x)
...     x = x + 1
... 
0
1
2
3
4
5
6
7
8
9
>>> 

>>> # Ou o continue para ir para o próximo ciclo
>>> x = 10
>>> while x:
...    if x == 5:
...        x = x - 1
...        continue
...    print(x)
...    x = x - 1
... 
10
9
8
7
6
4
3
2
1
>>> 
```

---

`for` - tá mais para um `foreach`

```python
>>> # for do python itera sobre sequências
... seq = [1, 2, 3, 'four', 5, 6.15]
>>> for i in seq:
...     print(i)
... 
1
2
3
four
5
6.15
>>> 

>>> # o for numérico pode ser feito produzindo um range(comeco, fim), fim não é incluído!
... for i in range(10, 20):
...     print(i)
... 
10
11
12
13
14
15
16
17
18
19
>>> 

>>> # se início for omitido, começa de 0
... for i in range(11):
...     print(i)
... 
0
1
2
3
4
5
6
7
8
9
10
>>> 

>>> # continue e break também funcionam com for
... seq = [1, 2, 3, 4, 'five', 'six', 7]
>>> for i in seq:
...     if i == 3: continue
...     if i == 'six': break
...     print(i)
... 
1
2
4
five
```

---

`def` - declarando funções e formas de receber parâmetros

```python
>>> # você define funções usando a declaração def
... 
>>> def soma(a, b):
...     return a + b
... 
>>> soma(2, 2)
4
>>> 

>>> # você pode atribuir valores padrão para os parâmetros
... # lembre-se, a partir do primeiro atributo com valor padrão, todos terão que ter
... 
>>> def mensagem(nome, tratamento='Sr', elogio='Sagaz'):
...     print(f'{tratamento} {nome} é {elogio}')
... 
>>> mensagem('Rui')
Sr Rui é Sagaz
>>> mensagem('Rui', tratamento='Dr')
Dr Rui é Sagaz
>>> mensagem('Rui', tratamento='Dr', elogio='Brilhante')
Dr Rui é Brilhante
>>> mensagem('Rui', elogio='Estupendo')
Sr Rui é Estupendo
>>> 

>>> # você pode passar uma lista variávels de parâmetros, usando '*', 
>>> # exemplo '*args': args será visto como uma tupla dos parâmetros passados
... def debug(*args):
...     for arg in args:
...             print(arg)
... 
>>> debug('a', 'b', 3, 15)
a
b
3
15
>>> 

>>> # você também pode passar uma conjunto variávels de parâmetros nomeados usando '**args'
>>> # '**args' 
>>> def mensagem(nome, **atributos):
...     print(nome)
...     for chave, valor in atributos.items():
...             print(f'{chave} = {valor}')
...
>>> mensagem('Rui', idade=30, sobrenome='Neto', time='Bahia')
Rui
idade = 30
sobrenome = Neto
time = Bahia
>>> 

>>> # uma função sem return, retorna None
>>> # 'pass' é uma declaração que não faz nada no Python
>>> def nada():
...     pass
... 
>>> print(nada())
None
>>> 

>>> # você pode, mas não deve, mudar a ordem se nomear os parâmetros
>>> def mensagem(nome, elogio):
...     print(f'{nome} e {elogio}')
... 
>>> mensagem(elogio='Inteligente', nome='John')
John e Inteligente
>>> 
```

---

`Exception` - Exceções

```python
>>> # O bloco minimo para tratar exceções é o try / except:
... try:
...     x = 10 / 0
... except ZeroDivisionError:
...     x = 0
... 
>>> x
0
>>> 

>>> # Você pode adicionar, também, uma claúsula 'else'
... # Essa claúsula só é executada se NÃO ocorrer nenhuma exceção
... try:
...     10 / 2
... except ZeroDivisionError:
...     x = 0
... else:
...     print(f'x = {x}')
... 
5.0
x = 0
>>> 

>>> # Além do 'else', também é possível adicionar uma claúsula 'finally'
... # A claúsula finally é executada de qualquer forma
... try:
...     x = 10 / 2
... except ZeroDivisionError:
...     x = 0
... else:
...     print('Sem exceções!')
... finally:
...     print(f'x = {x}')
... 
Sem exceções!
x = 5.0
>>> 

>>> # Para criar sua proria exceção, crie uma classe herdando de 'Exception'
... class ErroCustomizado(Exception):
...     pass
... 

>>> # Para lançar essa exceção, use 'raise'
... try:
...     raise ErroCustomizado("Ops!")
... except ErroCustomizado as e:
...     print(e)
... 
Ops!
```

---

`with` - Gerenciando contexto

```python
>>> # A declaração with permite abstrair as construções try / except / finally
... # Através da utilização de um gerenciador de contexto que já faz isso implicitamente
... # No exemplo abaixo, usando with e gerenciador de contexto, não precisamos dar 'close' no arquivo
... # Isso será feito automaticamente ao final do bloco
... with open('teste.txt', 'w') as fp:
...     fp.write('oi\n')
... 
3
>>> fp
<_io.TextIOWrapper name='teste.txt' mode='w' encoding='UTF-8'>
>>> 
```

---

Criando módulos

```python
# Todo arquivo Python é um módulo, podendo ser importado para utilização dos seus atributos
# Arquivo: wo.py
def words_occur(file_name):
    """Retorna uma tupla contendo respectivamente: quantidade de palavras, quantidade de palavras únicas"""
    # A linha acima é uma docstring!
    # É um comentário especial do Python, que permite documentar objetos. 
    # É possível acessar esse comentário através da função: help(words_occur)
    f = open(file_name)
    w_list = f.read().split()
    occur_list = {}
    for word in w_list:
        occur_list[word] = occur_list.get(word, 0) + 1
    
    return (len(w_list), len(occur_list))
```

---

Utilizando o módulo (supondo estar no mesmo diretório que `wo.py` ou que `wo.py` esteja no `sys.path`):

```python
# arquivo wo_test.py
import wo
print( wo.words_occur('sample.txt') )
```

---

Se `wo` for atualizado durante a execução de `wo_test`, essa modificação não será automaticamente assimilada.
Você precisará atualizar o módulo usando `imp.reload()`:

```python
import wo

# .... faz coisas....

# Ops, preciso atualizar wo
import imp
imp.reload(wo) # Note que não precisa de aspas, é o próprio objeto
```

---

Em projetos muito grandes, você pode criar estruturas de pacotes (`packages`).

Supondo uma estrutura:

```
jogo
└── fisica
    └── colisao
        ├── deteccao.py
```

E que você abra o interpretador dentro da pasta `jogo`, você pode importar `deteccao`:

```python
In [1]: import fisica.colisao.deteccao
In [2]: fisica.colisao.deteccao.detectar(1, 3)
1 3
```

---

Orientação a Objetos:

```python
class Forma:
    """Classe base para formas geométricas"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mover(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY

# Herança! 
class Quadrado(Forma):
    """Um quadrado que herda de Forma"""
    def __init__(self, x, y, lado=1):
        Forma.__init__(self, x, y)
        self.lado = lado

# Outra herança!
# Dessa vez adicionamos um método
class Circulo(Forma):
    pi = 3.14

    """Classe Circulo, herda de Forma e adiciona mais um metodo"""
    def __init__(self, x, y, r=1):
        Forma.__init__(self, x, y)
        self.raio = r
    
    def area(self):
        return self.raio * self.raio * self.pi

    # Método chamado para representação amigável "print(obj)"
    # Gera o output de print(circuloObjeto)
    def __str__(self):
        return f'Circulo de raio = {self.raio}, nas coordenadas ({self.x}, {self.y})'


if __name__ == '__main__':
    c1 = Circulo(18, 23)
    c2 = Circulo(5, 15, 20)

    print(c1)
    print(c2)

    print(f'Area c2: {c2.area()}')

    c2.mover(5, 6)
    print(c2)
```

---

Saída:

```bash
Circulo de raio = 1, nas coordenadas (18, 23)
Circulo de raio = 20, nas coordenadas (5, 15)
Area c2: 1256.0
Circulo de raio = 20, nas coordenadas (10, 21)
```

---

# Observações Orientação a Objetos

* Todos métodos de classes recebem como primeiro parâmetro `self`. Quando o método é chamado, `self` é setado para a instância que o chamou.

* A classe herdeira deve sempre chamar o `__init__()` de sua classe pai, dentro do seu `__init__()`.

* Observe que o parâmetro `self` é atribuído automaticamente pelo Python, com o valor da instância solicitante.

---

# Python - Essencial, em mais de 10 minutos

---

Python usa identação para identificar blocos de código:

```python
n = 9
r = 1

# 4 espaços!
while n > 0:
    r = r * n # equivalente: r *= n
    n = n - 1 # equivalente: n -= 1
```

---

Comentários em Python é tudo que vem após `#`:

```python
# Eu sou um comentário. Completamente ignorado pelo interpretador.
a = 10 # O código que precede executado. Mas o comentário, ignorado.
text = 'Mas, dentro de strings, é um # caractere como outro qualquer'
```

---

Variáveis em Python são criadas no momento que são declaradas. Não há necessidade de definir os tipos, que são inferidos:

```python
a = 10
c = 3.14
x = 'uma string'
```

---

# Obs:

Em algumas linguagens, os tipos primitivos são "baldes" que armazenam de fato os valores. 

**Mas**, em Python, variáveis são como **etiquetas** que apontam para os objetos dentro do *namespace*. 

Podem existir múltiplas etiquetas para um mesmo objeto. Caso esse objeto seja modificado, todas etiquetas refletirão isso.

---

Etiquetas! 

```python
# Etiqueta 'numero' refere-se ao objeto inteiro 10
numero = 10

# 'copia' passará a apontar também para o objeto inteiro 10
# cuidado! 'copia' não aponta para 'numero'.
# no momento da atribuição, 'numero' foi resolvido para o objeto inteiro 10
copia = numero

# Altera a etiqueta/variável 'numero' que passa a apontar o objeto inteiro 20
numero = 20

# 'copia', apesar da modificação em 'numero', permanece inalterada
print(copia)  # 10!
print(numero) # 20!
```

---

Essa informação só faz diferença **mesmo** para objetos mutáveis:

```python
# Ambas apontam para o mesmo objeto
# Novamente: l_copia não referencia l, mas sim o objeto lista.
l = [1, 2, 3]
l_copia = l

# Modifica o objeto lista, através de l
l[0] = 10
l[1] = 20
l[2] = 30

# Como o objeto é Mutável, l_copia também é afetado
print(l) # 10, 20, 30
print(l_copia) # 10, 20, 30
```

---

Variáveis em Python podem durante a execução diferentes tipos de objeto. **Mas evite!**:

```python
a = 10
print(a)

a = 3.14
print(a)

a = 'aloha'
print(a)
```

---

Você pode deletar uma variável com `del`:

```python
a = 100
print(a)

del a

print(a) # Exceção! a não foi declarada!
```

---

Por fim, variáveis devem começar com letras ou underline e não podem conter espaços. 

Python diferencia maiúsculas de minúsculas.

---

Expressões aritméticas e similares:

```python
# Expressões retornam valores
In [1]: 2 + 2
Out[1]: 4

# A divisão entre inteiros retorna um float. 
# Para truncar a parte fracional, use o '//'.
In [2]: 3 / 4
Out[2]: 0.75

# Outros objetos podem ser usados em expressões, não apenas números
In [4]: 'a' + 'b'
Out[4]: 'ab'

# Parênteses alteram a precedência
In [5]: 7 * (2 + 3)
Out[5]: 35

In [6]: 7 * 2 + 3
Out[6]: 17
```

---

Strings:

```python
# Declare com aspas simples ou duplas
>>> a = "spam"
>>> b = 'bacon'
>>> a
'spam'
>>> b
'bacon'

# Você aspas simples dentro de aspas duplas e vice-versa
>>> c = "you're"
>>> d = '"citacao"'
>>> c
"you're"
>>> d
'"citacao"'

# Você pode escapar usando '\', para inserir caracteres especiais
>>> x = "\t abc \n def"
>>> x
'\t abc \n def'
>>> print(x)
         abc 
 def

# Strings multilinha
>>> z = """
... um
... texto
... multilinha
... """
>>> 
>>> y = '''
... outro
... texto
... multilinha
... '''
>>> 
>>> x
'\t abc \n def'
>>> print(z)

um
texto
multilinha

>>> print(y)

outro
texto
multilinha
```

---

Números:

```python
>>> # Inteiro
... i = 10
>>> j = -15
>>> 
>>> # Floats
... c = 3.14
>>> d = 9.99
>>> 
>>> # Operações com int sempre retornam int, exceto a divisão, que retorna float
... 10 / 2
5.0
>>> 
>>> # Para truncar, use //
... 10 // 2
5
>>> 
>>> # Operações com float sempre retornam float
... 2.15 / 1.5
1.4333333333333333
>>> 
>>> # Você pode converter entre os tipos usando as funções int e float
... int(3.14)
3
>>> 
>>> float(2)
2.0
>>> 
>>> # Booleans se comportam como números, exceto na hora de serem representados como string
... # True = 1, False = 0
... True + True
2
>>> True == 1
True
>>> 
>>> False == 0
True
>>> 
```

---

Algumas funções *built-in* relacionadas a números:

```python
>>> # Valor absoluto
... abs(3.5)
3.5
>>> abs(-2)
2
>>> 
>>> # Quociente e resto
... divmod(10, 3)
(3, 1)
>>> 
>>> # Converte para float
... float(3)
3.0
>>> float('4.5')
4.5
>>> 
>>> # Converte para uma representação (string) hexadecimal do número
... hex(2)
'0x2'
>>> # Representação Octal
... oct(2)
'0o2'
>>> # Representação Binária
... bin(2)
'0b10'
>>> 
>>> 
>>> # Converte para inteiro
... int(3.5)
3
>>> int('4')
4
>>> 
>>> # Exponenciona
... pow(2, 3)
8
>>> 2 ** 3
8
>>> 
>>> # Arredonda
... round(3.5)
4
>>> round(3.4)
3
>>> round(3.6)
4
```

---

`None`

```python
# None é o "null" do Python
# Em valores lógicos, é um valor False
# Pode ser usado como placeholder
>>> nome = None
>>> bool(nome)
False

>>> # Depois a variável é de fato preenchida
>>> nome = "Teste"

>>> # Como None é um Singleton (só há uma instância)
... # Pode ser comparado com 'is'
... idade is None
True
```

---

Para ler dados do usuário, use `input('Mensagem: ')`

```python
# Use input(msg) para receber uma string do usuário
>>> nome = input('Seu nome: ')
Seu nome: Rui
>>> 

# Você deve converter, quando necessário, para o tipo adequado
>>> idade = int(input('Sua idade: '))
Sua idade: 30
```

---

Recomendações PEP8:


|Situação  |Sugestão  |Exemplo  |
|---------|---------|---------|
|Nome de módulos     |Tudo minúsculo e curto. Underscore apenas se necessário.         |`imp, sys`         |
|Nome de funções     |Tudo minúsculo. Use underscores se ficar mais legível.         |`sum(), my_func()`         |
|Nome de variáveis     |Tudo minúsculo. Use underscores se ficar mais legível.         |`my_var`         |
|Nome de Classes     |CapitalizeCadaPalavra         |`MyClass()`         |
|Constantes     |TODA_MAISCULA_COM_UNDERSCORE         |`TAX_RATE=`         |
|Identação     |4 espaçõs por nível         |         |
|Comparando True ou False     |Não comparte com True ou False, teste o valor da variável         |`if x, if not y`         |

---

# Listas, tuplas e conjuntos

---

Listas são como  arrays. Só que bem mais poderosos:

* Listas podem crescer ou diminuir
* Não há necessidade de declarar tipos
* Tipos de objetos diferentes podem constar na mesma lista

```python
>>> # Declarando uma lista
... lista = [1, 3.14, 'a', ['a', 'b']]
>>> lista
[1, 3.14, 'a', ['a', 'b']]
>>> 
>>> # Verificando o tamanho da lista
... len( lista )
4
>>> 
>>> # Para obter elementos individualmente, você pode indexar
... # Índices começam de zero
... lista[0]
1
>>> 
>>> # Você também pode indexar usando números negativos
... # -1 = último elemento
... # -2 = penúltimo.... e assim por diante
... lista[-1]
['a', 'b']
>>> lista[-2]
'a'
>>> 
>>> # Python permite indexar vários elementos de uma única vez
... # Sintaxe: [inicio:fim], sendo que fim não é inclusivo.
... lista[0:2] # Retornará os índices 0 e 1. Lembre-se, 2 não é incluído.
[1, 3.14]
>>> 
>>> lista[0:-1] # Todos
[1, 3.14, 'a']
>>> 
>>> lista[0:3] # 0, 1, 2
[1, 3.14, 'a']
>>> 
>>> lista[-2:-1]
['a']
>>> 
>>> # Cuidado, retorna uma lista vazia:
... lista[-1:2]
[]
>>> 
>>> # Você pode omitir as partes do slice
... # Se omitir o começo, default é 0
... lista[:2]
[1, 3.14]
>>> 
>>> # Se omitir o final, o default é len(lista), ou seja incluirá o último índice
... lista[2:]
['a', ['a', 'b']]
>>> 
>>> # Se omitir ambos, default [0:len(lista)]
... lista[:] # Essa sintaxe muitas vezes é utilizada para fazer uma cópia de uma lista
[1, 3.14, 'a', ['a', 'b']]
>>> 
>>> # Acessando um elemento específico
... lista[0]
1
>>> lista[1]
3.14
>>> 
>>> # Modificando uma lista
... lista[1] = 7.32
>>> 
>>> lista
[1, 7.32, 'a', ['a', 'b']]
>>> 
>>> # Modificando usando slices
... lista[1:3] = [10, 20, 30]
>>> lista
[1, 10, 20, 30, ['a', 'b']]
>>> 
>>> # Não precisa ser o mesmo tamanho não
... lista[1:3] = [10, 20, 30, 40, 50, 60, 70]
>>> lista
[1, 10, 20, 30, 40, 50, 60, 70, 30, ['a', 'b']]
>>> 
>>> # Removendo elementos da lista
... lista[1:3] = []
>>> lista
[1, 30, 40, 50, 60, 70, 30, ['a', 'b']]
>>> lista[1:3] = []
>>> lista
[1, 50, 60, 70, 30, ['a', 'b']]
>>> 
>>> # Adicionando elementos a lista
... lista.append('spam')
>>> lista
[1, 50, 60, 70, 30, ['a', 'b'], 'spam']
>>> 

>>> lista = [1, 3.14, 'f', ['a', 10]]
>>> 
>>> # Para mesclar listas, use extend()
... lista.extend([99, 100, 101])
>>> lista
[1, 3.14, 'f', ['a', 10], 99, 100, 101]
>>> 

>>> # Para inserir antes de uma posição específica, use insert(posicao, objeto)
... # objeto será incluído logo antes de "posicao"
... lista = [1, 2, 3]
>>> lista.insert(1, 'a')
>>> lista
[1, 'a', 2, 3]

>>> # Também suport índices negativos
... lista.insert(-1, 'b')
>>> lista
[1, 'a', 2, 'b', 3]
>>>
```

---

Para deletar um elemento de uma lista, use `del`:

```python
>>> lista
[1, 'a', 2, 'b', 3]
>>> 
>>> del lista[1]
>>> 
>>> lista
[1, 2, 'b', 3]
>>> 
```

---

Para remover um elemento através do valor, não do índice, use `remove(valor)`:

```python
>>> lista
[1, 2, 'b', 3]
>>> 
>>> lista.remove('b')
>>> 
>>> lista
[1, 2, 3]
>>> 

>>> # Se o valor não for encontrado, produz exceção. Cuidado.
... lista.remove('x')
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: list.remove(x): x not in list
>>> 
```

---

# Ordenando listas

---

O método `.reverse()` das listas, inverte a ordem *in-place*.

```python
>>> lista
[1, 2, 3]
>>> 
>>> lista.reverse()
>>> 
>>> lista
[3, 2, 1]
>>> 
```