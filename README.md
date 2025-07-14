# Dummy notebookutils / mssparkutils for Python

This package is an unofficial fork of [https://pypi.org/project/dummy-notebookutils/](https://pypi.org/project/dummy-notebookutils/), which is a pure dummy interfaces package which mirrors [MsSparkUtils' APIs](https://learn.microsoft.com/en-us/azure/synapse-analytics/spark/microsoft-spark-utilities?pivots=programming-language-r) of [Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/) for python users,customer of Azure Synapse Analytics can download this package from PyPi to generate the build.

The original package disappeared from GitHub and so I had no change to create PRs to fix a typing issue, so I recreated the project from scratch and updating it to the latest version of `notebookutils` (1.1.11) at the time of writing.

## Getting started

Install `dummy_notebookutils`

```sh
pip install dummy-notebookutils-reborn
```

## Usage

Add the following code below your other imports:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import notebookutils

    from notebookutils import mssparkutils
```

> [!WARNING]
> again, the package only mirrors APIs of synapse mssparkutils without actual functionality. The main goal is to help customer generating the local build. You always need upload your built package to synapse workspace for end to end testing.
