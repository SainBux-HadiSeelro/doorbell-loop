# self-reviewing-repo

## Purpose

This repo demonstrates an **event-driven code-review loop** using OpenCode (Opencode) GitHub Actions. The goal is to have an automatic, unrequested code review fire whenever a pull request opens — flagging a deliberately planted bug without any manual invocation.

Repo structure:
- `main` branch: clean, working code with passing tests
- `fix-attempt` branch: same code with a subtle bug planted in `inventory.py`
- Opening a PR from `fix-attempt` → `main` triggers the `.github/workflows/opencode.yml` Action
- The Action invokes `opencode review-pr`, which examines the PR and reports the bug

## Planted Bug

A subtle **off-by-one error** in the loop bound of `remove_expired_items(items, today)` at `inventory.py:11`. The loop iterates `len(items) - 1` times instead of `len(items)`, causing the **last item in the list to be silently skipped**. The bug:

- Produces no syntax error or crash
- Only manifests depending on which item is last in the list
- Causes expired items at the end of the list to remain undetected

(See `PLANTED_BUG.md` for a complete description and real-world impact.)

## Manual Steps (you'll do next)

OpenCode requires your GitHub authentication — do not push or run installs yourself:

1. **Push this repo to GitHub** (you'll authenticate via your GitHub account)
2. Run: `opencode github install` — this registers the Opencode GitHub Action in the repo
3. Open a Pull Request from the `fix-attempt` branch into `main`
4. Watch the automatic Opencode review appear on the PR, flagging the planted off-by-one bug

## What "Done" Means

- The PR review has been triggered automatically (no manual `opencode review` call needed)
- The review flags the off-by-one bug in `inventory.py`
- The baseline on `main` remains clean with correct behavior
- You've verified the loop: push → Action → PR review → bug detected

---

**Note:** This repo is designed to test the OpenCode event-driven review loop. The bug is intentionally subtle so that a casual code read might miss it — the automatic Action is what catches it.