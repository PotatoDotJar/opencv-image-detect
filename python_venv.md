# Python virtual environments using venv
Sourced from https://gist.github.com/GinoAvanzini/f0ed9c1a74ffce3f832c9fa68f19daba

Virtual environments are a useful way of separating dependencies and establishing a working environment for Python projects. The most common way of achieving this is through the use of `virtualenv` or `pipenv`. But since Python 3.3, a subset of `virtualenv` has been integrated into the standard library under the `venv` [module](https://docs.python.org/3/library/venv.html). Though not as featureful as the former two, `venv` is a simple way of getting a functional virtual environment setup.

This gist was inspired by Corey Schafer's [video](https://www.youtube.com/watch?v=Kg1Yvry_Ydk) on `venv`.

The commands are intended to be used on any Arch-based Linux distribution. For others distros, `python3` and `pip3` might be the way to go.

## Using venv

Since `venv` is a built-in module of any stock Python installation we don't need to install anything (apart from `python-pip` if it's not yet installed).

To create a virtual environment in the _virtual_env_ folder:

```
python -m venv virtual_env
```

In order for the virtual environment to have access to globally installed Python packages the flag `--system-site-packages` should be used.

To activate the virtual environment
```
source virtual_env/bin/activate
```
This will add some text to your command prompt indicating that the environment is activated. The output of ```pip list``` should be different than the one we see without the virtual environment.

Typing ```which python``` will retrieve the path of the Python interpreter which the venv will use. The version of Python used in the virtual environment will be the same as the one that was installed in the system when the venv was created. If you REALLY need to use different Python versions you must use other solutions, like `virtualenv`.

To deactivate the virtual environment just type
```
deactivate
```

## Installing packages

Packages can be installed with ```pip```. These will exist only within the virtual environment and will not be accesible otherwise.

```
pip install package_name
```

## Export package list

We can generate a list of required packages so anybody can create an environment which uses the same requirements and dependencies (and the same versions).

```
pip freeze > requirements.txt
```

If the venv has access to globally installed packages and we only want to add locally installed packages to requirements.txt add the `--local` flag.

With the virtual environment activated we can install the packages in the requirements.txt file:

```
pip install -r requirements.txt
```