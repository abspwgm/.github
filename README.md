# .github

The organization's identity and its default community health files.

GitHub gives a repository with this name two powers: `profile/README.md` becomes
the [organization's public profile](https://github.com/abspwgm), and the files
below are used by **every** repository in the organization — public and private
alike — that does not carry its own copy. That inheritance is why they live here
once instead of being copy-pasted into each repo and drifting apart.

| Path | Applies to |
|---|---|
| `profile/README.md` | The organization profile page |
| `SECURITY.md` | Every repo without its own security policy |
| `CONTRIBUTING.md` | Every repo without its own contributing guide |
| `CODE_OF_CONDUCT.md` | Every repo — Contributor Covenant 2.1, unmodified apart from the reporting contact |
| `SUPPORT.md` | Every repo |
| `.github/ISSUE_TEMPLATE/` | The issue forms and the "contact links" panel |
| `.github/PULL_REQUEST_TEMPLATE.md` | Every repo without its own PR template |

A repository that needs to say something different keeps its own file; the local
one wins, and there is no merging.

This repository must stay **public** for any of that to work, including for the
private repositories that inherit from it. Nothing in it may contain anything
that is not already public.

## Brand assets

`brand/` is vendored from `absolute-power-brand`, which is the source of truth
and is private. Do not edit it by hand:

```sh
python3 scripts/sync_brand.py            # vendor from the brand repo's main
python3 scripts/sync_brand.py --check    # re-hash only; what CI runs
```

`brand/SOURCE.json` pins the upstream commit and a SHA-256 per file, the same
mechanism and format `absolute-game-servers` uses, rather than a second way of
doing the same thing.

The organization avatar and the social preview card are uploaded by hand in
organization settings — GitHub exposes no API for either. The PNGs come from the
`render-org-assets` workflow in `absolute-power-brand`, which renders the SVGs
with the real brand faces installed; a browser render of the SVG will silently
substitute a fallback face and get the wordmark wrong.

## Governance

Branch protection is not configured here. It lives in
[`absolute-game-servers/governance/`](https://github.com/abspwgm/absolute-game-servers/tree/main/governance)
and is applied by script to every repository.
