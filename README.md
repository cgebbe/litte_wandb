# litte_wandb

Extracts the [automatic logging](https://docs.wandb.ai/guides/track/log#automatically-logged-data) part from the weights and biases library.

## How it works

Simply call `little_wandb.dump_info(output_dirpath)` to track the following information:

- system info (hostname, user, time, OS, python executable, CLI arguments)
- pip- or conda-environment (think pip freeze)
- git information including diff patches to current local commit *and recent upstream commit*
- copy of currently executing file

See [example notebook](example_notebook.ipynb) and [example output](example_output/).

## Improvement ideas

- Feature: environment variables !!! Shall we also add such an option upstream?
- Problem: If called from a jupyter notebook, it will not copy the executing file.
  - root cause: wandb determines the program via `__main__.__file__` which raises an AttributeError in Jupyter
  - solution: fix upstream `_get_program` in wandb/sdk/wandb_settings.py
- Problem: If the current commit is not yet pushed to upstream, there is not git diff to upstream
- Problem: The diff patch does not include (new) untracked files
  - solution: fix upstream `_save_patches` in wandb/sdk/internal/system/system_info.py (`git diff --no-index`?!)
- Feature: Track GPU type
- Feature: editable installs are not easily tracked. Either raise error or get git information for editably installed libs?

