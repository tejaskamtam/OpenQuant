# Development Notes


## Packaging
Guide: https://youtu.be/JkeNVaiUq_c

### Dependencies
`twine`

### Installing Locally
```sh
pip install .
```
Then import in python terminal editor to test.
Remove using `pip uninstall quantpyml`

### Building
First delete dist then edit version in toml. Then build wheel and dist:
```sh
python -m build
```

### Uploading to Repositories
#### Test PyPi:
```sh
twine upload -r testpypi dist/*
```
Test install: `pip install -i https://test.pypi.org/simple/ quantpyml`

#### PyPi
```sh
twine upload dist/*
```
Test install: `pip install quantpyml`




