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

```python
{% raw %}
{% url "detail" person.id %}
{% endraw %}
```

```python
{% raw %}
{% url "hr:person_detail" person.id %}
{% endraw %}
```

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

- Django map URLs to views through the `urls.py` file and the `urlpatterns` list, where each item is composed by a `path(url_part, view, name=...)`.

Example:

```python
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]
```

The URL can contain `capture` blocks in the format `<type:name>`.
Those blocks, when captured, are passed as keyword arguments `name=captured_value` to the view.

- Each `path` can have an unique `name` which makes refer to those urls easier using the template tag `url` in the templates.

- But, imagine you have many apps in your project. And each one defines an `name='index'` `path`.
Which one gets refered where your template use `{% url 'index' %}` ?

To avoid this situation, you should add an attribute to every `urls.py` you define named `app_name`, with a string representing your app´s name.

```python
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]
```

So, in our examples, the canonical names of these urls are: `blog:post_list` and `blog:post_detail`.

- If you need a really complex URL configuration and `path` patterns don´t solve your problem, you can use regular expressions and the `re_path` method.

- To enable the app urls into your project, `include()` into the project `urls.py` file. Example:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

- You can create canonical URLs of an object defining the method `get_absolute_url(self)` in its model:

```python
class Post(models.Model):
    ...

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )

    ...
```

Then, in your template you can put things like:

```django
<a href="{{ post.get_absolute_url }}">{{ post }}</a>
```

- Django looks for templates in every app inside a folder named `templates`.

Example:

```
app_1/
    templates/
app_2/
    templates/
app_3/
    templates/
```

- Imagine if you have an `index.html` in every `templates` folder and calls `render(request, "index.html")`:

```
app_1/
    templates/
        index.html
app_2/
    templates/
        index.html
app_3/
    templates/
        index.html
```

Which one gets rendered ?

To avoid that, create one more folder inside each `templates` folder with the same name as the parent app:

```
app_1/
    templates/
        app_1/
            index.html
app_2/
    templates/
        app_2/
            index.html
app_3/
    templates/
        app_3/
            index.html
```

Now, you should call `render` with a sort of namespace: `render(request, "app_3/index.html")`.

- Django template system has three building blocks:

1. `Template tags` that control the rendering of the template: `{% tag %}`
2. `Template variables` `{{ variable }}` get replaced by the `variable` passed in the `context` dict.
3. `Template filters`: allows to modify the way variable are displayed: `{{ variable|filter }}`

- To enable the `static` template tag, enable it with:

```django
{% load static %}
```

Then, to refer to create a path to a static file:

```django
...
  <link href="{% static "static/css/blog.css" %}" rel="stylesheet">
...
```

Similarly to `templates`, Django looks for `static` files in each installed app. In each app, it checks if the file is contained in a folder called `static`:

```
app_1/
    static/
        app_1/
            css/
                style.css
            js/
                animation.js
app_2/
    static/
        app_2/
            css/
                style.css
            js/
                animation.js
```

So, to load the `app_2` `css`, you would do:

```django
...
  <link href="{% static "static/css/style.css" %}" rel="stylesheet">
...
```

- Django templates support inheritance throught build `blocks`. When a template  defines a block, it can be extended and filled by a more especific template. Blocks are defined with the `{% block name %}{% endblock %}` tag. The more specifica template dosen´t need to fill all parents block:

```django
<title>{% block title %}{% endblock %}</title>

...
  <div id="content">
    {% block content %}
    {% endblock %}
  </div>
```

- The other templates can extend this template using the `extends` template tag and redefining the blocks:

```django
{% extends "blog/base.html" %}

{% block title %}My Blog{% endblock %}

{% block content %}
  <h1>My Blog</h1>
  {% for post in posts %}
    <h2>
      <a href="{{ post.get_absolute_url }}">
        {{ post.title }}
      </a>
    </h2>
    <p class="date">
      Published {{ post.publish }} by {{ post.author }}
    </p>
    {{ post.body|truncatewords:30|linebreaks }}
  {% endfor %}
{% endblock %}
```

- Django comes with a built-in pagination solution in the app `django.core.paginator`. To enable pagination your code should:

Import the class and the main exceptions generated:

```python
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
```

In your view, instatiate the `Paginator` passing the object list and the number of objects per page:

```python
paginator = Paginator(posts, 2)
```

Capture the current page passed in the URL as a GET parameter:

```python
page = request.GET.get("page")
```

The filtered list will be returned by the `paginator` object. You just need to pass the desired page number:

```python
    # Some page was passed ? If so, render it
    try:
        posts = paginator.page(page)
    # No page given, render the first
    except PageNotAnInteger:
        posts = paginator.page(1)
    # The page passed is invalid, render the last in the paginator object
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
```

In the template with pagination you can use this pretty generic code. Will work in almost any page with pagination:

```django
<div class="pagination">
  <span class="step-links">
    {% if pagination.has_previous %}
      <a href="?page={{ pagination.previous_page_number }}">Previous</a>
    {% endif %}
    <span class="current">
      Page {{ pagination.number }} of {{ pagination.paginator.num_pages }}.
    </span>
      {% if pagination.has_next %}
        <a href="?page={{ pagination.next_page_number }}">Next</a>
      {% endif %}
  </span>
</div>
```

`pagination` is a `Paginator` instance, in the view above, `posts`.

Being generic, this html snippet for pagination can be saved in a folder for generic snippets and included in other templates.

To include this snippet in other templates, use the `include` template tag.

```django
...
{% include "blog/inc/pagination.html" with pagination=posts %}
...
```

The `with` clauses passed to the included template a context, where `pagination` will be equal to the variable `posts` in the current context.

Mind that included templates have access to all the context of the template including it. We could have changed the pagination snippet to use `posts` instead of `pagination` and it would work.

- Views can be implemented as classes. Called Class Views. Major advantages include better code organization and the creation or usage of mixins for enhanced functionality.

- Django provide multiples generic views in the `django.views.generic` package. In our blog example, the `post_list` view can be implemented as a class view:

```python
from django.views.generic import ListView

...

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"
```

The class attributes define how the class-view will behave.
Above:

`queryset` defines an specific queryset. If you want to list all objects of some model, use, instead, the class attribute: `model = ModelClass`

`context_object_name` name of the variable to be passed to the template with the queryset result. The default name, is none is specified, is `object_list`.

`paginate_by` param to instatiate the paginator

`template_name` the template to use in `render`

You will need to adjust your `urls.py` to refer the class:

```python
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name="post_list"),
```

Last, you need to change the template because the `paginator` object returned by the generic `ListView` is named `page_obj`:

```django
{% include "blog/inc/pagination.html" with pagination=page_obj %}
```

- Django forms provide a elegant way to request, process, validate and bind information into models.

- Django provide two base classes to build forms:

`Form`: Standard HTML forms, not tied to models.

`ModelForm`: Forms tied to model instances.

- Forms are usually saved in a `forms.py` file for each app.

- A simple standard `Form` example to send share a blog post by email:

```python
from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
```

- Each `Field` has a default widget tied to it. You can change the widget passing a keyword parameter `widget=`, like in `comments`.

- The parametes used in the `Fields` initializes are taken into account during validation, example:

`required=False`: the field can be left empty.
By default, every field should be filled.

`max_length=...`: limites the field size.

The type of the field also implies some validation. `EmailField` validates the mail addresses entered.

- `form.is_valid()` validates the form data. Returns `True` if everything is ok.

- `form` errors can be accessed through the `form.errors` attribute.

- if `form` `is_valid()`, then it´s `form.cleaned_data` attribute contains a dict with the fields and values.

- note: if `form` **not** `is_valid()`, `cleaned_data` will only contain the fields that validated.

- Django makes sending e-mails pretty easy. A simple `send_mail(subject, message, sender, list_of_recipients)` function is provided in the `django.core.mail` package.

```python
from django.core.mail import send_mail
send_mail('Django mail', 'This e-mail was sent with Django.', 'your_account@gmail.com', ['your_account@gmail.com'], fail_silently=False)
```

- You can mount a full url using the same protocol and base of the current request using `request.build_absolute_uri(url)`.

Example:

```python
# post is a model object
post_url = request.build_absolute_uri(post.get_absolute_url())
```

- To initialize a form with the data sent in the `request`:

```python
if request.method == "POST":
        form = EmailPostForm(request.POST)
```

- You can render the form using the helper methods `form.as_p` or `form.as_ul` or `form.as_table`

```django
<h1>Share {{post.title}} by e-mail:</h1>
<form action="." method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Send e-mail">
</form>
```

- Remember to include the `{% crsf_token %}` template tag. Its mandatory and avoids CSRF attacks.

- If the form is not fully filled or filled with wrong data, the method `form.is_valid()` raises an exception and forces the page to be re-rendered, exhibiting the errors found in each field.

- `ForeignKey` can define the inverse relation name:

```python
class Post(models.Model):
    ...

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, relation_name="comments")
    ...
```

You can accessa a comment post by `comment.post` and all comments of a post using `post.comments.all()`.

If not defined, the relation name is the name of the class suffixed with a `_set`:

```python
class Post(models.Model):
    ...

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ...
```

In this case, you would access the of a `Comment` in the same way: `comment.post`, but to access all the `Comments` of a `Post`, you would do:
`post.comment_set.all()`.

Note that `post.comments` (or `post.comment_set`) are querysets, so you can use `.all()`...`.filter()`...

- Remember, Django forms can inherit from a `Form`, standard form class, or from `ModelForm` that is a `Form` that inspects and bases itself in a `Model`.

To define a `ModelForm`:

```python
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")
```

- You can explicit which attributes of the model will be "fillable" in the form defining a `fields` tuple.
Or, explicitly define which fields to `exclude` defining a `exclude` tuple.

- To create the model instance linked to the `ModelForm` you cave to call its `save()` method:

```python
comment_form = CommentForm(request.POST)
if comment_form.is_valid():
    new_comment = comment_form.save()
```

- If you want to change the model object before saving it to the database, call `save(commit=False)`:

```python
current_post = Post.objects.get(pk=post_id) # passed in URL

comment_form = CommentForm(request.POST)
if comment_form.is_valid():
    new_comment = comment_form.save(commit=False)
    new_comment.post = current_post
    new_comment.save()
```

- You can create a block and define a var to be used over all the scope in templates using the `with` block:

```django
{% with comments.count as total_comments %}
    {{ total_comments }} comment{{ total_comments|pluralize }}
{% endwith %}
```

- The `pluralize` filter returns "s" if the value passed is different of 1.

- Django `for` template tag has a `empty` clause, when the `for` dosent have any iteration:

```django
{% for comment in comments %}
    <p>{{ comment }}</p>
    <p>{{ comment.body }}</p>
    <p>{{ comment.created }}</p>
    <hr>
{% empty %}
    <p>Oh! No comments yet.</p>
{% endfor %}
```

- You could use the template filter `join` to render a lista as a single string:

```django
<p class="tags">Tags: {{ post.tags.all|join:", " }}</p>
```

