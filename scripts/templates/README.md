<!--
IMPORTANT:
  This file is generated from the template at 'scripts/templates/README.md'.
  Please update the template instead of this file.
-->

# adc_download
[![pipeline status](https://gitlab.com/JulioContrerasH/adc-download/badges/master/pipeline.svg)](https://gitlab.com/JulioContrerasH/adc-download/pipelines)
[![coverage report](https://gitlab.com/JulioContrerasH/adc-download/badges/master/coverage.svg)](https://gitlab.com/JulioContrerasH/adc-download/commits/master)
[![documentation](https://img.shields.io/readthedocs/adc-download.svg?style=flat)](https://adc-download.readthedocs.io/en/latest/index.html)
[![pypi version](https://img.shields.io/pypi/v/adc-download.svg)](https://pypi.org/project/adc-download/)

download images

## Requirements
adc_download requires Python 3.6 or above.

<details>
<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.6
pyenv install 3.6.8

# make it available globally
pyenv global system 3.6.8
```
</details>

## Installation
With `pip`:
```bash
python3.6 -m pip install adc-download
```

With [`pipx`](https://github.com/cs01/pipx):
```bash
python3.6 -m pip install --user pipx

pipx install --python python3.6 adc-download
```

## Usage (as a library)
TODO

## Usage (command-line)
```
{{ command_line_help }}
```

{% if commands %}Commands:
{% for command in commands %}
- [`{{ command.name }}`](#{{ command.name }}){% endfor %}

{% for command in commands %}
### `{{ command.name }}`
```
{{ command.help }}
```

{% include "command_" + command.name.replace("-", "_") + "_extra.md" ignore missing %}
{% endfor %}{% endif %}