* View mixins should go on *the left* in the inheritance list.

* `settings.AUTH_USER_MODEL` returns a string and can be used in model declarations.
  `get_user_model()` returns the `User` model class object.

* Templates can access the view object that rendered it (and their attributes) through the `view` object:

```html
<!-- "attribute" can change, "view" is the default object name -->
<h1> {{ view.attribute }} </h1>
```
