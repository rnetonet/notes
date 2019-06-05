# Django for Beginners - William S. Vincent

## Criando um ambiente virtual Python

Ambientes virtuais evitam colisão entre versões de bibliotecas. **Use!**

Para utilizar *virtual environments* precisamos instalar o `pipenv` através do `pip3`:

```bash
pip3 install -U pipenv
```

Para criar um primeiro projeto:

```bash
mkdir django
cd django

# Cria o ambiente virtual e instala a última versão do Django
pipenv install django

# Ativa o ambiente virtual
pipenv shell

# Cria um primeiro projeto de test
django-admin startproject test_project .
```

> **Observação**: O `.` no final da linha de comando, força o Django a criar as estruturas na pasta atual. 
Do contrário, Django criará uma pasta `test_project`, dentro dela um arquivo `manage.py` e outra pasta `test_project`. O `.` evita essa redundância.

Confirme que tudo está funcionando chamando o servidor próprio do Django:

```python
python manage.py runserver
```

## Hello World app

Crie um diretório:

```bash
$ mkdir helloworld
```

Crie o ambiente virtual:

```bash
$ cd helloworld
$ pipenv install django
$ pipenv shell
```

Crie o projeto Django:

```bash
$ django-admin startproject helloworld .
```

Você obterá a seguinte estrutura:

```bash
$ tree helloworld/
helloworld/
├── helloworld
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── Pipfile
└── Pipfile.lock
```

Os arquivos têm funções próprias.

`settings.py` - guarda toda as configurações do projeto
`urls.py`     - mapeia as URLs recebidas às `views` a serem executadas

`manage.py`   - script do Django que permite executar uma série de ações ao nível do projeto.

Django vem com um servidor web próprio. Para executá-lo:

```bash
$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

January 26, 2019 - 22:21:18
Django version 2.1.5, using settings 'helloworld.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Django empacota funcionalidades através de apps. Um mesmo projeto pode ter vários apps.

Vamos criar um primeiro app, chamado `pages`:

```bash
$ python manage.py startapp pages
```

Uma pasta `pages` será criada, com a seguinte estrutura:

```bash
$ tree pages/
pages/
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

O que cada arquivo faz:

- `admin.py` - arquivo de configuração para o app `admin`
- `apps.py` - arquivo de configuração para o app propriamente dito
- `migrations/` - armazena os arquivos de alteração da base dados (migrações)
- `models.py` - onde os modelos são definidos. Django traduz automaticamente para tabelas.
- `tests.py` - testes específicos do app
- `views.py` - funções / views que recebem a requisição, tratam, interagem com o banco e renderizam a resposta

Contudo, para que Django identifique o novo app, é preciso listá-lo nas configurações (`settings.py`):

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pages'
]
```

Em Django as configurações de URLs (`urls.py`) indicam para qual `view` as requisições devem ser redirecionadas.

As `views`, por sua vez, tratam a requisição, opcionalmente consultam/manipulam o banco de dados, para então renderizar a resposta.

Criando uma `view` em `pages.views` que retorna `Hello World`:

```python
# pages/views.py
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("Hello World")
```

> **Nota:** Todas views recebem pelo menos o objeto `request` como parâmetro.

Crie um arquivo em `pages/urls.py` com a seguinte configuração de URLs apontando para a view:

```python
# pages/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # se URL == /, chame views.helloword, nomeie esse mapeamento como 'home'
    path('', views.helloworld, name='home')
]
```

Por fim, você precisa referencia as configurações de urls do app (`pages/urls.py`) no projeto (`helloword/urls.py`):

```python
# helloworld/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')) # ***
]
```

> Toda requisição que case com `pages/` será tratada pelos padrões definidos em `pages/urls.py`.

## Criando um app `pages`

Crie um novo projeto `pages_project` com um app denominado `pages`:

```bash
$ mkdir pages_project
$ cd pages_project/

pages_project$ pipenv install django
pages_project$ pipenv shell

pages_project$ django-admin startproject pages_project .
pages_project$ django-admin startapp pages
```

Habilite o app, listando em `pages_project/settings.py`:

```python
# ...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pages'
]
# ...
```

Toda página necessitará de três coisas: `Template`, `View` e `URL`.

Para criar sua primeira view, crie uma página chamada `templates` dentro do app `pages`.
Dentro dessa pasta, crie uma outra pasta chamada `pages`, por fim, ponha o arquivo HTML nesssa página.

A repetição é necessária pois o Django quer ter muita muita certeza de que está renderizando o template correto.

A estrutura ficará:

```bash
pages_project$ tree pages/templates/
pages/templates/
└── pages
    └── home.html
```

Outra alternativa, é cria um diretório `templates` na pasta do projeto `pages_project` e alterar o `settings.py` para buscar lá também:

Você deverá mover a pasta `templates` de `pages` para `pages_project`, e subir o nível do arquivo `home.html`, para que fique dentro de `templates`.

Ficará assim:

```bash
pages_project$ tree pages_project/
pages_project/
├── __init__.py
├── settings.py
├── templates
│   └── home.html
```

E para que o Django considere essa pasta `templates` (por padrão só considera as mencionadas em `settings.INSTALLED_APPS`), 
é preciso alterar o arquivo `settings.py`.

Note que uma das primeiras linhas do arquivo `settings.py` é:

```python
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```

Note que o `settings` define uma variável, `BASE_DIR`, para servir de base para referenciar pastas, apps, etc, que componham nosso projeto.

Altere agora na seção de templates:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Busque templates no diretório BASE_DIR (pages_project) + '/templates/'
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Agora altere o conteúdo de `home.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    Homepage!
</body>
</html>
```

## Class Based Views

Django vem com uma série de Views baseadas em classes com comportamento padrão: renderize um template, detalhe um objeto de determinado modelo, etc.

Utilizando a `TemplateView` (renderizar um template), altere o arquivo `pages.views`:

```python
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
```

Agora, para criar a URL apontando para essa `view`, altere o `urls.py` do projeto, para referenciar o arquivo `urls.py` do app `pages`, a ser criado.

```python
# pages_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls'))
]
```

Crie o arquivo `urls.py` do app `pages`:

```python
# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home')
]
```

> Class Based Views requerem a chamada de método `as_view()` quando mencionadas no arquivo `urls.py`

