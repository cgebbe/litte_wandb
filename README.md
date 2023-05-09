# litte_wandb

Extracts the [automatic logging](https://docs.wandb.ai/guides/track/log#automatically-logged-data) part from the weights and biases library.

## Desired output

- system info
- pip- or conda-environment
- git repo including patches
- stdin, stdout, stderr ?!
- system metrics (?) This is not a snapshot, but rather 

## Relevant code

- https://github.com/wandb/wandb/blob/7a7dd30e94e3c27e0af9058248320fe30967157e/wandb/sdk/internal/system/system_info.py#L82
  -  this one file does everything!
- https://github.com/wandb/wandb/blob/7a7dd30e94e3c27e0af9058248320fe30967157e/wandb/sdk/wandb_init.py#L719
- https://github.com/wandb/wandb/blob/7a7dd30e94e3c27e0af9058248320fe30967157e/wandb/sdk/wandb_run.py#L514
