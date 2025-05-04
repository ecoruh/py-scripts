# py-scripts

Python scripts monorepo. It uses virtualenv + pip-tools.

## Create & activate your repo’s virtualenv

```bash
# At the monorepo root:
pyenv shell 3.13.3          # ensure you’re using your pyenv’d Python
python -m venv .venv        # create a venv in “.venv”
source .venv/bin/activate   # activate it
```

You’ll now install all dependencies into this one env.

## Install pip-tools

```bash
pip install pip-tools
```

pip-tools gives you `pip-compile` (to pin) and `pip-sync` (to install).

## Define your common dependencies

At the repo root, create requirements.in containing libs every script might need:

```text
# requirements.in (root)
pytest
pylint
# …etc.
```

Run:

```bash
pip-compile requirements.in # produces requirements.txt with
                            # exact pins
pip-sync                    # installs every package in
                            # requirements.txt
```

## Per-script dependency lists

Under `scripts/`, each script folder gets its own requirements.in:

```text
monorepo/
├── requirements.in   # common deps
├── requirements.txt  # pinned common deps
├── scripts/
│   ├── script_a/
│   │   ├── script.py
│   │   └── requirements.in   # script-specific deps
│   └── script_b/
│       ├── script.py
│       └── requirements.in
```

In scripts/script_a/requirements.in:

```text
-r ../../requirements.in    # inherit all common deps
flaky-lib                  # add only what script_a needs
```

Then at the root run:

```bash
pip-compile scripts/script_a/requirements.in  \
    --output-file scripts/script_a/requirements.txt

pip-compile scripts/script_b/requirements.in  \
    --output-file scripts/script_b/requirements.txt
```

## Install (sync) everything

Back in the root:

```text
pip-sync                            \
  requirements.txt                  \
  scripts/script_a/requirements.txt \
  scripts/script_b/requirements.txt
```

This installs the union of all pinned `deps` into your single `venv`. No duplication, no drift.

## Workflow for adding/removing deps

1. Edit the appropriate requirements.in (root or script folder).
2. Re-run `pip-compile` ….
3. `pip-sync` from the root to update the venv.

## Bulk compile

From root:

```bash
chmod +x ./comp-reqs.sh
./comp-reqs.sh
```

## Bulk sync

From root:

```bash
chmod +x ./sync-reqs.sh
./sync-reqs.sh
```
