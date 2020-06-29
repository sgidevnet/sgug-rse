# Django Macros

Macros accepting positional and keyword arguments, and repeated block
tags in the django template system.  Sometimes include tags just do
not get the job done.  Either you have repeated code that you want to
keep all in the same single template, or your code needs to
dynamically generate and substitute in certain values, in a way that
the include syntax inhibits.  Whatever the case, if you are finding
that the built in include tag just is not working for your use case,
then perhaps django-macros is for you.

## Exemple

At the beginning of your file include:

```
{% load macros %}
```

When you have a section of your template you want to repeat, but don't
want to have inherited or any other block tag-like functionality, define
a macro as follows:

```
{% macro some_macro_name arg1 arg2 kwarg="default" %}
    {{ arg1 }} was the first argument.
    {{ arg2 }} was the second argument.

    {% if kwarg %}This is a {{ kwarg }}. {% endif %}
{% endmacro %}
```

Then when you want to use the macro, simply do:

```
{% use_macro some_macro_name "foo" "bar" kwarg="nondefault value" %}
```

which renders to:

```
foo was the first argument.
bar was the second argument.
This is a nondefault value.
```

# License

MIT
