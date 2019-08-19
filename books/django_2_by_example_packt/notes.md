# Django 2 By Example - Packt - Antonio Mele

- A **project** is a Django installation with some settings.

- A **project** is a site. Which can have multiple **applications** running.

- An **application** is a group of models, views, templates and URLS.

- **Applications** leverage the framework to provide functionalities and may be reused in different sites.

- `Projects` and `Applications` are Python packages.

- To enable an app, register it in `settings.INSTALLED_APPS`. The string will look like: `app_name.apps.AppNameConfig`

- If your app provides some view, it should implement an `urls.py` file. Which should include an `urlpatterns` list.

- You should name each URLPattern defined in `urls.py`. So you can refer them from the templates through the `url` templatetag.

- If you want to namespace it, create a variable, just above `urlpatters` defining the `app_name`. You don´t need to change the names in urlpatterns, but in the `url` templatetag they should be prefixed with the defined `app_name`.

`{% url "detail" person.id %}`, becomes `{% url "hr:person_detail" person.id %}`.

- To make the app URLs visible, create a path in the project `urls.py` and use `include("app_name.urls")` to refer to the app urls.

- Views should return a `HttpResponse` or raise an Exception (`django.http.Http404` for example)

- Use `django.shortcuts.render(request, template, context)` to render a template into an `HttpResponse`.

- To refer to templates, create a `templates` folder inside the `app` folder. Then, create an `app_name` folder inside the  recently created `templates` folder. Put the HTML files inside `templates/app_name/`. When rendering the template, refer to them using `app_name/template.html`.
This subfolder acts like a namespace to the template files, avoiding name clashes.

- Models are the canonical truth of the data model adopted. Every change should be made to the model class.

- Models are synced to the database through the commands `makemigrations` and `migrate`

- Django comes with a very good `admin` portal. To access it, first you need to create a `superuser`:

```python
python manage.py createsuperuser
```

- To make a model accessible in the admin, change the app `admin.py` file and register the model:

`admin.site.register(Model)`

- You can customize the admin creating a subclass of `admin.ModelAdmin`. Then, you bind it with the model and register using the decorator `@admin.register(Model)`. Example:

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('author', )
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
```

- Some util Django shortcuts:

`django.utils.timezone` -> A datetime timezone aware: `timezone.now()`.
`django.shortcuts.get_object_or_404` -> Gets an object without raising model-related-exceptions or raise an `Http404` exception.
`django.shortcuts.get_list_or_404` -> Gets a list of objects or raise an `Http404` exception, if nothing is found.

- Models get, by inheritance, a very powerful API to select, create, update and delete registers.

- The select process is made through the `objects` attribute of the model. This attribute, called `queryset`, provides a `.get` that get exactly one object based on the keywords filters passed.

If none object is found, it raises: `Model.DoesNotExist` exception.
If more than one is found, it raises: `Model.MultipleObjectsReturned`.

- `Model.objects` is the default `queryset` of the models. The `queryset` allows you to create new objects, select, update, delete...etc.

- To create a new object of a Model, you can create the object in memory, instatiating the object, and then `save()`, persisting:

```python
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>>
>>> user = User.objects.get(username='admin')
>>> user
<User: admin>
>>> post = Post(title='Another post', slug='another-post', body='Another post content', author=user)
>>> post.id
>>> post
<Post: Another post>
>>>
>>> post.save()
>>> post.id
3
>>>
```

Or call `objects.create` to create and persist at the same time:

```python
>>> another_post = Post.objects.create(title='AnotherAnother post', slug='another-another-post', body='
... Another Another post content', author=user)
>>> another_post
<Post: AnotherAnother post>
>>> another_post.id
4
>>>
```

- To update an object, change the atribute then call `save()` again. `save()` is smart and if the object already exists, will perform an update.

- Using the `queryset`:

Get all objects from a table:

```python
Model.objects.all()
```

But mind that the query was not executed. Django querysets are lazy, so, they just performe the operation when really necessary:

```python
>>> posts = Post.objects.all() # not executed yet
>>>
>>> print( posts ) # executed!
<QuerySet [<Post: AnotherAnother post>, <Post: A very another post>, <Post: teste>, <Post: Um novo post>]>
>>>
```

- To apply a filter to all objects and return the filtered list, use `Model.objects.filter`.

- You can make field lookups during `filter` or `get`: `field__attr=`

```python
>>> Post.objects.filter(publish__year=2019)
<QuerySet [<Post: AnotherAnother post>, <Post: A very another post>, <Post: teste>, <Post: Um novo post>]>
>>>
```

- You can pass multiples conditions:

```python
>>> Post.objects.filter(publish__year=2019, author__username='admin')
<QuerySet [<Post: AnotherAnother post>, <Post: A very another post>, <Post: teste>, <Post: Um novo post>]>
>>>
```

Which is equivalent to chaining `filter` calls:

```python
>>> Post.objects.filter(publish__year=2019).filter(author__username='admin')
<QuerySet [<Post: AnotherAnother post>, <Post: A very another post>, <Post: teste>, <Post: Um novo post>]>
>>>
```

- You can exclude some objects from the returned list using the `.filter` method:

```python
>>> Post.objects.filter(publish__year=2019).filter(author__username='admin').exclude(title__startswith=
... "Another")
<QuerySet [<Post: A very another post>, <Post: teste>, <Post: Um novo post>]>
>>>
```

- Use `.order_by` to order the results:

```python
>>> Post.objects.filter(publish__year=2019).filter(author__username='admin').exclude(title__startswith=
... "Another").order_by("title")
<QuerySet [<Post: A very another post>, <Post: Um novo post>, <Post: teste>]>
>>>
>>> # Prefix with - to make "desc"
>>> Post.objects.filter(publish__year=2019).filter(author__username='admin').exclude(title__startswith=
... "Another").order_by("-title")
<QuerySet [<Post: teste>, <Post: Um novo post>, <Post: A very another post>]>
>>>
```

- Delete an object with `.delete`, but mind the cascade behavior with the defined `ForeignKey`.

```python
>>> p = Post.objects.get(id=4)
>>> p.delete()
(1, {'blog.Post': 1})
```

- **Querysets** are **lazy**. They are evaluated only when:

1. Iterated over
2. Sliced
3. Serialized (pickle or cache)
4. `repr()` or `len()` applied
5. `list()` applied
6. When are used in an `if` or passed to `bool()`

- `Model.objects` is the default manager provided by Django and returns all objects from the table.
It is magically provided by Django to every model, **except when the Model defines some custom manager**.

- To define a custom Manager, inherti from `models.Manager` and implement a `get_queryset()`:

```python
class PostPublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    ...
    objects = models.Manager()
    published = PostPublishedManager()
```

If you provide a custom manager, you need to explictly declara an `objects` also. Django, in those cases, won´t create one magically.

The custom manager can be used then:

```python
>>> from blog.models import Post
>>>
>>> Post.published.all()
<QuerySet [<Post: teste>]>
>>>
```

Being a queryset, additional filters can be applied:

```python
>>> Post.published.filter(title__startswith="teste")
<QuerySet [<Post: teste>]>
>>> Post.published.filter(title__startswith="Another")
<QuerySet []>
>>>
```

- Django `views` receive a request and return a `HttpResponse`, or raise an exception.

- All `views` need to receive a `request` parameter

- A simple view example:

```python
# Create your views here.
def post_list(request):
    posts = Post.published.all()
    context = {
        "posts": posts
    }
    return render(request, "blog/post/list.html", context)

```

- Django provides the `django.shortcuts.render` function render a template and return a `HttpResponse`.
It takes the `request` object, the `template path` and a `dict` with the `context` to be made avaiable to the template.

- Besides the `context` dict passed to `render()`, it also has access to the attributes set in the `request` by context processors.

- `Views` receive as arguments parts captured during the `path` processing by Django. The parts to be captured are defined using the `<type:argument_name>` format (ex: `<id:age>`).

-