## Build Package

```bash
python3 -m build
```

## Upload to Test PyPi

```bash
twine upload --repository testpypi dist/*
```

## Test

### Create Virtual Env

```bash
rm -rf testenv
python3.9 -m venv testenv
source testenv/bin/activate
```

### Install bcolors from Test PyPi

```bash
python3.9 -m pip install --index-url https://test.pypi.org/simple/ --no-deps bcolors
```

### Test 

Start Python Console:

```bash
python3
```

Verify the Version:

```python
from importlib import metadata
metadata.version("bcolors")
```

Verify the functionality

```python
import bcolors as b
print(b.OK + "Color Statement" + b.END)
print(b.ERR + "Color Statement" + b.END)
```

## Upload to Prod PyPi

```bash
twine upload dist/*
```