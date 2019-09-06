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

- Inside the `for` templatetag you can also test if it is the last element (`forloop.last`):

```django
{% for tag in post.tags.all %}
    <a href="{% url "blog:post_list_by_tag" tag.slug %}">
      {{ tag.name }}
    </a>
    {% if not forloop.last %}, {% endif %}
{% endfor %}
```

- You can create your own custom template tags. In Django, there are two kinds of template tags.

`simple_tag`, that receive a value, process it and return an object.

`inclusion_tag`, that receive a value, process and return a rendered template.

All custom template tags should live inside Django applications.

To create, create a folder `templatetags` inside your app and create a `__init__.py` file in it.

No create the modules that will contain the templatetags, example: `blog_tags.py`

```
blog/
    __init__.py
    models.py
    ...
    templatetags/
        __init__.py
        blog_tags.py
```

The name of the module (`blog_tags`) will be used in the `load` inside the template `{% load blog_tags %}`, for example.

- The code for a simple template tag that returns the total of posts in the blog:

```python
from django import template
from ..models import Post

# required!
register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()
```

- Every `template_tags` module should include a `register = template.Library()` variable to be valid.

- The `simple_tag` decorator registers the function as a template tag. The function name is used as the name of the template tag.
If you want to use other name, pass a `name` parameter to the decorator:

```python
@register.simple_tag(name='my_tag')
def my_super_template_tag():
    ...
```

- To use the template tag, `load` it in the template file:

```django
{% load blog_tags %}
```

Now, you can use:

```django
  <div class="alert alert-primary">
    This blog has {% total_posts %} posts
  </div>
```

- Template tags are very powerfull. They permit you to access models from the representation layer in a shareable and encapsulated way.

- `inclusion_tag` declare the template to be rendered in the decorator and the function should return a dict, used as context for rendering the template.

```django
@register.inclusion_tag("blog/post/latest_posts.html")
def latest_posts(count=5):
    latest_posts = Post.published.order_by("-created")[:count]
    return {"latest_posts": latest_posts}
```

In this example, the template tag accepts a parameter named `count` (which defaults to `5`), but can be passed in the template tag as a positional parameter:

```python
@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by("-created")[:count]
    return {"latest_posts": latest_posts}
```

And rendered in the layout:

```django
...
{% show_latest_posts 2 %}
...
```

- You can return objects from `simple_tags` to be used. In this template tag, we get the n most commented posts:

```python
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count("comments")).order_by('-total_comments')[:count]
```

We use the `annotate` to count how many comments each `Post` has. Django provides others annotations, as `Avg`, `Sum`, `Max`.

See: https://docs.djangoproject.com/en/2.0/topics/db/aggregation/

No that this template tag returns an object, a queryset.

Now use it in the template (if a template tag returns an object, you can "rename", "create an alias", for it using `as`):

```django
{% get_most_commented_posts as most_commented_posts %}
```

Mind that template tags that return objects have to be linked to a variable, like above.

You can´t iterate directly over a template tag:

**Won´t work!**

```django
{% for commented_post in get_most_commented_posts %}
    <li><a href="{{ commented_post.get_absolute_url }}">{{ commented_post.title }} ({{ commented_post.total_comments }} comment{{ commented_post.total_comments|pluralize }})</a></li>
{% endfor %}
```

Instead:

```django
{% get_most_commented_posts as most_commented_posts %}
<ul>
{% for commented_post in most_commented_posts %}
    <li><a href="{{ commented_post.get_absolute_url }}">{{ commented_post.title }} ({{ commented_post.total_comments }} comment{{ commented_post.total_comments|pluralize }})</a></li>
{% endfor %}
</ul>
```

- Besides the template tags, Django provides also template filters, that permits you to modify a variable and return the modified content.

- Template filters are Python functions that receive one or two arguments, the variable being changed and a parameter.

- Filters are used in the following forms:

```django
{{ variable|my_filter }}
```

Or, when a param is passed:

```django
{{ variable|my_filter:"upper" }}
```

- You can chain filters:

```django
{{ variable|first_filter|second_filter:"X"|third_filter }}
```

The result of a filter is passed to the next.

- Filters are registered in a very similar way to other template tags.

Inside the `templatetags` folder, in a module with a `register = template.Library()`, and are registered by the decorator `@register.filter`:

```python
@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
```

`simple_filter` also accepts a `name` argument, to register the filter with other name than the function one.

- Django escapes all strings generated by filters. To avoid this behavior, we use the `mark_safe` that marks the string as *safe*, so Django does not escape it.

- Django is database agnostic, but it provides some advanced features for PostgreSQL, like full text index search, in the app `django.contrib.postgres`.

- To enable these functionality, you need to activate the app, listing it in `settings.INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.postgres",
    ...
]
```

- After enabling the app, you will get new kinds of lookups:

```python
from blog.models import Post
Post.objects.filter(body__search='django')
```

Which searchs in a vector based way (*full text search*).

- You can use `SearchVector` to `annotate` a `QuerySet` and search in multiple fields at the same time:

```python
from django.contrib.postgres.search import SearchVector
from blog.models import Post

Post.objects.annotate(
    search=SearchVector('title', 'body'),
).filter(search='django')
```

```python
.annotate(
    search=SearchVector('title', 'body')
)
```

Creates a new computed field named `search`. Then, we filter using it:

```python
.filter(search="django")
```

PostgreSQL will look for the word `"django"` in the title and body fields at the same time, using full index text search.

- If you want to order the results of a full text index search by rank (frequency and proximity), use the classes: `SearchQuery` and `SearchRank`:

```python
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
...
search_vector = SearchVector("title", "body")

search_query = form.cleaned_data["query"]
search_query = SearchQuery(query)

results = (
    Post.objects.annotate(
        search=search_vector, rank=SearchRank(search_vector, search_query)
    )
    .filter(search=search_query)
    .order_by("-rank")
)
...
```

- You can attribute `weight` for the columns of the `SearchVector`:

```python
search_vector = SearchVector("title", weight="A") + SearchVector("body", weight="B")
```

And filter for a minimum rank:

```python
results = (
    Post.objects.annotate(
        search=search_vector, rank=SearchRank(search_vector, search_query)
    )
    .filter(search=search_query)
    .filter(rank_gte=0.3) # Minimum rank
    .order_by("-rank")
)
```

The weights can be defined as letters and each letter has a fixed value:

`A`: `1.0`

`B`: `0.4`

`C`: `0.2`

`D`: `0.1`

The bigger, the more relevant.

- The PostgreSQL app also supports search based on trigram similarity. Trigram are sequences of three chars.
It compares strings based on the number of trigrams that are equal. This turns out to be very effective way to compare words among many languages.

- To use TrigramSimilarity you have to install an extension in your database:

```sql
CREATE EXTENSION pg_trgm;
```

- And to search using Trigram, first import the Annotation:

```python
from django.contrib.postgres.search import TrigramSimilarity
```

And change you query:

```python
results = Post.objects.annotate(
    similarity=TrigramSimilarity('title', query),
).filter(similarity__gt=0.3).order_by('-similarity')
```

`TriganSimilarity` calculates a similarity for each row comparing the column (`"title"`) to the `query` specified.

- If you want to use other search platforms like Solr or Elasticsearch, **use http://haystacksearch.org/**.

- Django looks for template, static files, etc, in the order of the `settings.INSTALLED_APPS` list.
If you want to prioritize an especific app, put it first.

- The Django authentication framework (`django.contrib.auth`) is included by default in every project you create.

- The authentication framework also enables a middleware:

`AuthenticationMiddleware`: associates the user instance for every request, based on session information.

```python

# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Middleware register themselves to be called in every request or response event, augmenting it or doing some auxiliary action.

- The Django `auth` framework creates three models:

`User`: an user basic model, containing `username`, `password`, `email`, `first_name`, `last_name`, `is_active`

`Group`: group model to categoriza users.

`Permission`: flags to allow users or groups to perform some action.

- The module `django.contrib.auth` provides two functions important functions:

`authenticate(request, username=..., password=...)` to check if a pair `username/password` is valid.
If it is, the `User` in question is returned, if not, `None` is returned.

`user(request, user)`: binds the user to the request object.

- `django.contrib.auth` include some class based views in the `django.contrib.auth.views` module, being the most important:

`LoginView`: handle login

`LogoutView`: handle logout

And, when the user knows the current password, to change password:

`PasswordChangeView`: form to perform a password change.

`PasswordChangeDoneView`: success view shown when the password change is performed successfully.

If the user does not remembers, reset can be performed:

`PasswordResetView`: Generates a link and sends to the user to reset the password.

`PasswordResetDoneView`: view saying the link to reset was sent

`PasswordResetConfirmView`: Screen that allows the user to set the new password (link sent by `PasswordResetView`)

`PasswordResetCompleteView`: view after the change is done successfully

- Leverage those views to gain time.

- Example of `LoginView` and `LogoutView` usage:

```python
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
```

- By default, `django.contrib.auth` framework looks for its templates in folder called `registration`.

So, if you want to overwrite it, create a `registration` folder inside your app folder and create htmls files in it.

Remember that you have put your application first in the `INSTALLED_APPS` list, so templates will be looked first in it, then in `django.contrib.auth` app.

- You can force a view to be accessible only if the user is authenticated decorating it with `@login_required` from `django.contrib.auth.decoratos`:

```python
from django.contrib.auth.decorators import login_required

@login_required()
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})
```

- To configure the urls used by the `django.contrib.auth.views` class based views, define in your `settings.py`:

```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_URL = 'logout'
```

- Every `request` in Django has an `user` attribute. If the user is not authenticated, `.user` is an `AnonymousUser` instance. You can check if an user is authenticated using the read only attribute `request.user.is_authenticated`.

- You can include all `django.contrib.auth` urls instead of declaring your own:

```python
from django.urls import path, include
# ...

urlpatterns = [
    # ...
    path('', include('django.contrib.auth.urls')),
]
```

`django.contrib.auth.urls` defined paths:

```python
from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
```

- Every field in a form can have a `clean_fieldname(self)` method to validate/transform it.
Those methods can return the input value (accessible from `cleaned_data`) if valid.
Or transform it, returning it, and overwriting it in the `cleaned_data` dict.
And, if not valid, it can raise a `forms.ValidationError("Message")`, that will be bind to the field.

```python
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password_confirmation(self):
        cd = self.cleaned_data
        if cd["password_confirmation"] != cd["password"]:
            raise forms.ValidationError("Passwords do not match")
        return cd["password_confirmation"]
```

- Your forms can also include a more general `clean(self)` method that is run after all `clean_field...` methods.
This method is useful to validate fiels in group.

- The `User` model provides a `set_password` methods that handles encryptation. Don´t attribute the password directly.

- Files created by the developer are served in the `static` scope. User uploaded files are saved in `media`.

To configure, add to `settings`:

```python
MEDIA_URL = '/media/' # URL path to access the files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') # Folder where the files will live
```

By default, Django does not serve those files, you need to configure your `urls.py`:

```python
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, settings.MEDIA_ROOT)
```

- You can use the `messages` app, already included in every Django app, to show one time messages to users:

Register a message:

```python
...
if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, "Credentials saved with success")
        else:
            messages.error(request, "Error updating your profile")
...
```

Listing (normaly in the `base.html` template) the messages:

```django
{% for message in messages %}
<div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
    {{ message|safe }}
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
    </button>
</div>
{% endfor %}
```

- Authentication is handled by the `settings.AUTHENTICATION_BACKENDS` backends.

Default is the `ModelBackend`, that checks username x password using the `User` model:

```python
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
```

- Every time you call `authenticate()` from `django.contrib.auth` it tris to auth the user against each of the backends in `settings.AUTHENTICATION_BACKENDS` until some has success or the list ends.

- To create your own authentication backend you need to provide a class with two methods:

`authenticate`: that receives the user credentials and tries to authenticate it.
If success, returns the user, if not, `None`.

`get_user`: receives an user ID and returns its instance

- A simple custom authentication class:

```python
from django.contrib.auth.models import User


class EmailBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            return None

```

- You can check an user password using its `check_password()` method:

```python
...
if user.check_password(password):
    return user
...
```

To activate it, add to `settings.AUTHENTICATION_BACKENDS`:

```python
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "account.authentication.EmailAuthBackend",
]
```

- Indexes make database queries faster. Django creates indexes in three ways:

Fields with `unique=True` automatically have an index.

You can require Django to create an index for a field using `db_index=True` in its declaration:

```python
class Image(models.Model):
    ...
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    ...
```

Create index for fields that are very used in lookups.

If you want compound indexes, create using `Meta.index_together` option.

- To define `ManyToMany` relations, use `models.ManyToManyField(Entity)`.

It creates a intermediary join table with the primary key of each `Entity`.

It can be defined in any of the two entities. Normally, it is defined in the one that contains the other.

- The `ManyToManyField` creates a `Manager` in the attribute, so you can add, remove, filter, .all....

- `ImageField` take a parameter `upload_to` that defines the subfolder, inside `MEDIA_ROOT`, to save the file.

- To persist an `ImageField` in disk you can call explictly `.image.save()`:

```python
image.image.save(
    image_name,
    ContentFile(response.read()),  # from django.core.files.base import ContentFile
    save=False                     # do not save the model
)
```

- `ImageField` have an `.url` attribute to use in the `<img src=...`.

- You can make some view accessible only by POST or GET methods using `django.views.decorators.http` decorators:

Example:

```python
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get("id")
    action = request.POST.get("action")
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == "like":
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({"status": "ok"})
        except:
            pass

    return JsonResponse({"status": "ko"})
```

There is also `require_GET` and `require_http_methods(["GET", "POST", "PUT"])`, that receives a list.

- Default, the many to many manager `add(instance)` method does not duplicate (it does not raises an exception if you try also).
And a `.remove(instance)` where `instance` does not exist, does not raises an exception too.

- If you want to allow duplicates in your many to many, declare your own "man in the middle table":

Example:

```python
class PostIcon(models.Model):
    post = models.ForeignKey(Post)
    icon = models.ForeignKey(Icon)
```

And use `through=`

```python
class Post(models.Model):
    icons = models.ManyToManyField(Icon, through=PostIcon)
```

And then create it one by one:

```python
for icon in icons:
    PostIcon(post=post, icon=icon).save()
```

- You should protect your POST requests from CSRF attacks using the `{% csrf_token %}`.
But you need to protect AJAX requests too, to do that read the cookie and append the value to all AJAX requests:

Django hosts the token in the `csrftoken` cookie:

```html
<!-- Lib to read cookie content -->
<script src="https://cdn.jsdelivr.net/npm/js-cookie@2/src/js.cookie.min.js"></script>

<script>
  // Append the token to all AJAX requests made by jQuery
  var csrftoken = Cookies.get('csrftoken');
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
  $(document).ready(function(){
    {% block domready %}
    {% endblock %}
  });
</script>
```

- Some HTTP methods are considered safe and should not be augmented with CSRF tokens: GET, HEAD, OPTIONS, TRACE.
Those methods should not realize significant changes inside your system.

- The `with` tags is useful to avoid evaluating a queryset multiple times in the template, example:

```django
{% with total_likes=image.users_like.count users_like=image.users_like.all %}
<div class="image-info">
  <div>
    <span class="count">
      <span class="total">{{ total_likes }}</span>
      like{{ total_likes|pluralize }}
    </span>
    <a href="#" data-id="{{ image.id }}" data-action="{% if
    request.user in users_like %}un{% endif %}like"
    class="like button">
      {% if request.user not in users_like %}
        Like
      {% else %}
        Unlike
      {% endif %}
    </a>
  </div>
  {{ image.description|linebreaks }}
</div>
{% endwith %}
```

- Use the `with` tag for a more performatic system.

- All Django models support monkey patching throught `add_to_class` method.

- You can define your own middle-table for many to many relations:

the middle model:

```python
class Contact(models.Model):
    user_from = models.ForeignKey("auth.User", related_name="rel_from_set", on_delete=models.CASCADE)
    user_to = models.ForeignKey("auth.User", related_name="rel_to_set", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("-created", )

    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"
```

Add you can add to the user:

```python
User.add_to_class(
    "following",
    models.ManyToManyField("self", through=Contact, related_name="followers", symmetrical=False)
)
```

Creating the manager. Note that `add`, `remove`, etc, will be disabled, because your are using a custom middle table.

The `symmetrical=False` indicates that the relationship can go only one way, if i follow you, you don´t need to follow me.

- You can dinamically add a `get_absolute_url()` for some models using the `settings.ABSOLUTE_URL_OVERRIDES`:

```python
from django.urls import reverse_lazy

# Dynamically add a get_absolute_url() to the listed models
ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda u: reverse_lazy("user_detail", args=[u.username])
}
```

- Polymorphic ForeignKeys can be created using the `django.contrib.contenttypes` app.

It´s installed by default in every Django project. It includes a model, `ContentType`, that represents each model of each application.

Django creates an instance of ContentType for every model created, automatically.

The model contain three attributes:

`app_label`: the app name

`model`: the name of the model class

`name`: model verbose_name

You can query these instances:

```python
>>> ContentType.objects.filter(app_label="images")
<QuerySet [<ContentType: image>]>
>>>
```

You can get the original class using the `model_class()` method:

```python
>>> ct_image = ContentType.objects.filter(app_label="images").first()
>>>
>>> Image = ct_image.model_class()
>>> Image
<class 'images.models.Image'>
>>>
>>> Image.objects.count()
4
>>>
```

Its possible to go the other way too: get the contentype from the model class:

```python
>>> from images.models import Image
>>> from django.contrib.contenttypes.models import ContentType
>>>
>>> ContentType.objects.get_for_model(Image)
<ContentType: image>
>>>
```

- To define a Generic relation in your model, you need three attributes:

`target_ct`: A ForeignKey to a `ContentType` instance that is beings pointed.
`target_id`: Id of the instance of the Model pointed in `target_ct`
`target`: A `GenericForeignKey` model, provided by `django.contrib.contenttypes.model`, that links the previous two attributes.

```python
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
...
class Action(models.Model):
    user = models.ForeignKey('auth.User',
                             related_name='actions',
                             db_index=True,
                             on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType,
                                  blank=True,
                                  null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True,
                                            db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
...
```


- You can list all the ids of a relation using `values_list("id", flat=True)`:

```python
    following_ids = request.user.following.values_list("id", flat=True)
    if following_ids:
        actions = Action.objects.filter(user_id__in=following_ids)
```

- Django querysets provide the `select_related()` for improving the performance of ForeignKey and OneToOne relations.
It creates a JOIN, speeding up the query and the access to the related models:

```python
actions = actions.select_related('user', 'user__profile')[:10]
```

`select_related("rel1", "rel2")` takes the attribute names of the relations to be improved.
If none is provided, all `ForeignKey` and `OneToOne` fields are joined.

Always, if possible, limit it to the relations that will be really used.

- `select_related()` is useful to `ForeignKey` and `OneToOne` relations, where it´s possible to make a `JOIN`.

- For `ManyToMany` or reverse lookups, we need to use `prefetch_related()`.
This method performs a separated query and joins, using Python, the result to the original.

```python
actions = actions.select_related('user', 'user__profile').prefetch_related("target")[:10]
```

`prefetch_related()` works for `ManyToMany`, `ManyToOne` and `GenericForeignKey` fields.

- But if you apply some `filter()` or `exclude()`, the `prefetch_related()` loses its capabilites, because the originary query is changed.

- To achieve the better performance you need to use the new `Prefetch()` annotation:

```python
categories_qs = Category.objects.prefetch_related(
    Prefetch(
        'subcategories',
        queryset=Category.objects.filter(is_active=True),
        to_attr='active_subcategories'
    )
)

categories = []

for category in categories_qs:
    subcategories = [sub.name for sub in category.active_subcategories]
```

- Django offers `signals` to monitor changes in models. The main signals are:

`pre_save`, `post_save`, `pre_delete`, `delete` and `m2d_changed`

- Define your signal handlers in a module named `signals.py` in your application.

```python
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Image


@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()
```

- Just creating the file won´t cut it, you need to import it in your app configuration class, inside the `ready()` method.
This method is called when the application registry is fully populated:

```python
from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = "images"

    def ready(self):
        import images.signals
```

