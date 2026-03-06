# alloyfyi

Metal alloys and materials science API client — [alloyfyi.com](https://alloyfyi.com)

## Install

```bash
pip install alloyfyi
```

## Quick Start

```python
from alloyfyi.api import AlloyFYI

with AlloyFYI() as api:
    results = api.search("steel")
    print(results)
```

## License

MIT
