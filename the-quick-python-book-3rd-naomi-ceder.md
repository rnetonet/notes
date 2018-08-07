# The Quick Python Book 3rd - Naomi Ceder

## Sobre Python

### Pontos fortes

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

### Pontos fracos

* Não tão rápida quanto C
* Tem menos bibliotecas - em alguns nichos - do que linguagens como C, Java...
* Não há verificação de tipos em *compile time*
* Não tem bom suporte em mobile
* GIL atrapalha concorrência

### Python em 10 minutos ou menos

* Tipos numéricos

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

* Operações com inteiros:

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

* Operações com pontos flutuantes:

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

* Algums funções *built-in* e do módulo *math*:

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

* Todo arquivo Python é um módulo. Os atributos definidos no módulo podem ser acessados a partir de outro módulo através de `import`. Feito o *import*, você pode acessar os atributos através da sintaxe: `module.function(arguments)`.

* Booleans:

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

* Listas

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

* Modificando listas:

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

* Algumas operações e funções que podem lidar com listas:

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

* Tuplas - similar a listas, mas são imutáveis, não permitem alteração por indexação / slice

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

* Conversão entre listas e tuplas

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

* Strings

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

* Ao usar `print(objeto)` o objeto é convertido para *string*

```python
>>> print(3.14)
3.14
>>> print(10)
10
>>> print(True)
True
>>> 
```

* Dicionários:

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

* Conjuntos (*Sets*)

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

* Arquivos:

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

* Estruturas de controle de fluxo

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

* Operações de comparação lógica:

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

* `if / elif / else`

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

* `while`:

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