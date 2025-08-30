# alg

Here is an implementation of regex for:
* a+
* b+

## NeuralNetworks module

The `NeuralNetworks` package has been reorganized for clarity. It now
contains the following subdirectories:

| Folder | Purpose |
| ------ | ------- |
| `data` | Sample datasets and images used for demonstrations. |
| `models` | Stand‑alone model definitions and architecture examples. |
| `scripts` | Training and inference scripts as well as small experiments. |
| `utils` | Reusable helper functions such as dataset generators. |
| `tests` | Simple test scripts and experimental snippets. |

Each folder is a Python package thanks to the included `__init__.py`
files, which enables relative imports between components.
