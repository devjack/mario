# Mario
> Mario is a simple cli package management tool for endpoint documentation. It works well with [endpointer](https://github.com/devjack/endpointer).


## Installation

```
pip install mariocli
```


### Install from source.
For source installations:
```
pip install -e .
```

For development installs, build installs and other environments requiring
additional dependencies such as `pylint`, run:
```
pip install -e ".[dev]"
```

## Using mario

These commands may help get you started:
```
mario about
mario --help
mario validate
```

### Building & Distributing

(TODO: CI this w/ Travis)
```
rm -rf ./dist
python setup.py bdist_wheel
twine upload dist/*
```
