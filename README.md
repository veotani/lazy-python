# Lazy Imports Experiments

An example how to import python submodules lazily using [lazy_loader](https://github.com/scientific-python/lazy_loader).

## Running

Before running make sure you've installed `lazy_loader`:

```
pip install lazy_loader
```

Then go to the root directory of this project and run `python main.py`.

## Explanation

Module `resources` provides two submodules: `eager` and `lazy`. Attributes of `eager` are evaluated when they are
imported. Attributes of `lazy` only load when they are used.

To achieve it we should define stubs like we did here in `resources/__init__.pyi`. However, you shouldn't import
anything in the `resources/__init__.py` because it won't be used. If you append `from . import eager` there, you won't
be able to import `from resources import eager` in `main.py`. You also can't just import `import resources` and access
`resources.eager` as it leads to `AttributeError`.

## Expected Output

If everything is set correctly here is the output you should get:

```
Resources loading started
Eager resource evaluation started
Eager resource evaluation finished
Resources loading finished
Accessing lazy resource value
Lazy resource evaluation started
Lazy resource evaluation finished
Accessed lazy resource value
Accessing eager value
Accessed eager value
```
