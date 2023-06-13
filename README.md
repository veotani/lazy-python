# Lazy Python

This documentation provides an example of how to import submodules lazily in Python utilizing the [lazy_loader](https://github.com/scientific-python/lazy_loader) library.

## Objective

Our primary aim is to achieve lazy evaluation of a module's attributes while preserving the IDE hints. This feature can't be implemented by merely defining attributes in the `__getattr__` method, hence our approach to use `lazy_loader`.

## Setup and Execution

### Dependencies

Before executing the code, you need to install the `lazy_loader` library. You can install it using pip:

```bash
pip install lazy_loader
```

### Running the Code

After installation, navigate to the project's root directory and execute `main.py`:

```bash
python main.py
```

## How It Works

The `resources` module provides two submodules: `eager` and `lazy`. The attributes of the `eager` submodule are evaluated upon import, while those of the `lazy` submodule are evaluated upon use.

To achieve this, we define stubs and pass them into `lazy_loader` within the `__init__.py` file of the module. These stubs are defined in a `*.pyi` file - in this case, `__init__.pyi`.

When importing from these modules, IDE hints will only display what is defined in the `*.pyi` file. Despite this, all imported entities will be evaluated lazily.

For attributes where lazy evaluation isn't necessary, there are two approaches:

1. Define the imports within the `__init__.py` file.
2. Leave the imports in the `__init__.[py|pyi]` files untouched.

The first method may lack IDE hints, whereas the second one requires no modification of the way you import the attribute or module.

## Expected Results

If everything is configured correctly, the output should resemble the following:

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

This output verifies the success of both eager and lazy resource evaluations.
