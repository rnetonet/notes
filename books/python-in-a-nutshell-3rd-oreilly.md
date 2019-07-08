# Python in a Nutshell, 3rd Edition

### Interpretador

- Python tem um interpretador, `python`, que realiza interpretação e compilação (módulos importados).
- Em versões mais recentes, na plataforma Windows, há o launcher `py.exe`, que é incluído ao PATH.
- O interpretador é afetado por algumas variáveis de ambientes. As principais:
    - `PYTHONHOME` - Local de instalação do Python que deve conter um diretório `lib`, com as bibliotecas padrão do Python. Se não setada, heurísticas são aplicadas para encontrar o diretório.
    - `PYTHONPATH` - Lista de pasta em que o interpretador irá buscar por módulos. Separadas por vírgulas em ambientes UNIX e pontos-virgúla em ambientes Windows. Estende o valor de `sys.path`.
    - `PYTHONSTARTUP` - Nome ou caminho de um script a ser executado antes de uma sessão **interativa** do interpretador.
    - `PYTHONDONTWRITEBYTECODE` - Evita que o interpretador salve bytecodes em disco.

- Opções de linha de comando do interpretador:
    - `-B` - não gera bytecode
    - `-c "..."` - executa a linha de comando passada nas aspas e encerra
    - `-i` - abre uma sessão interativa ao final do script, mesmo que haja erro. A sessão tem acesso às variáveis globais definidas pelo script.
    - `-m module` - especifica um módulo, procurado em `PYTHONPATH`, para ser executado como script/main.
    - `-t` ou `-tt`, respectivamente, emitem warning/erro para indentação errada.
    - `-v` - mostra imports e cleanup de forma verbosa

- O interpretador suporta caminhos de arquivo separados por `/`, mesmo no Windows. Neste, também existe suporte para `\`.

- Apenas módulos importados são compilados e armazenados (cache). Em Python 2, salvos como `.pyc`, em Python 3, dentro de `__pycache__`, no mesmo *path* que o arquivo `.py` do módulo.

- Em ambientes UNIX, é possível tornar um script Python executável dando-o permissão de leitura e execução, `r+x`, e incluindo uma linha *shebang* em seu início: 

```python
#!/usr/bin/env python
```

### A linguagem Python

- Programas Python são feitos de linhas lógicas, que podem ter uma ou mais linhas físicas.

- *Blank lines* são ignoradas por Python

- Comentários `# texto`, podem ocorrer em uma linha própria ou no final de outras linhas. Tudo após o `#` é ignorado por Python.

- Não precisar terminar comandos com `;`. O final da linha física faz esse papel.

- Se o comando for muito grande, Python permite quebrá-lo usando: `\` no final de cada linha, exceto a última:

```python
print("Meu nome é " + \
"John!")
```

- Linhas físicas dentro de chaves `{}`, colchetes `[]` ou parênteses `()`. Nesses casos, a indentação é relevante apenas para primeira linha:

```python
In [1]: print( "a",  
   ...: "b", 
   ...: "c")                                                                                                                                                 
a b c

In [3]: [1, 
   ...: 2, 
   ...: 3, 
   ...: 4, 
   ...: 5]                                                                                                                                                   
Out[3]: [1, 2, 3, 4, 5]

In [4]:                                                                                                                                                      

In [4]: {"a": 1, 
   ...: "b": 2, 
   ...: "c": 3, 
   ...: "d": 4, 
   ...: "e": 5}                                                                                                                                              
Out[4]: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

- Python usa indentação para delimitar blocos. Cada bloco é uma sequência de linhas lógicas indentadas com a mesma quantidade de espaços.

- Versão 2 do Python susbstitui tabs por 8 espaços.

- Não use tabs. Use sempre 4 espaços, é o padrão.

- Em v2, use a opção `-tt` para evitar misturar tabs e espaços. v3, não permite isso.

- Em v3, o encoding dos arquivos `.py` é por padrão, `utf-8`. Em v2, é `ascii`. Em ambos pode-se definir explicitamente, através de um comentário especial:

```python
# coding: iso-8859-1
...
```

- Recomenda-se sempre usar `utf-8`.

- Identificadores são tokens que dão nomes a variáveis, módulos, funções, classes, etc. Devem começar com uma letra ou `_` e não podem ter espaços. 

- A versão 3 suporta unicode em identificadores, mas evite.

- Maiúsculas e minúsculas são **diferenciadas**.

- Sinais gráficos como: `#, @, $, !, etc` não são permitidos em identificadores.

- Algumas convenções utilizadas para identificadores em Python:
    - Apenas nomes de classes começam com letra **Maiúscula**, todos outros com minúscula.

    - Identificadores iniciados com um underscore, `_identificador`, são semanticamente **privados**. Já identificadores iniciados com **dois** underscores `__identificador` são semanticamente **fortemente privados**. Isso ocorre pois Python não impõe tal proteção, realizando apenas uma simples obfuscação dos nomes para torná-las *privados*.

    - Identificadores que iniciam e terminam com dois underscores, `__iden__`, são nomes especiais da linguagem.

- Em sessões interativas do interpretador, o identificar dor `_`, *single underscore*, guarda o valor do último comando interpretado.

