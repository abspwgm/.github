# Contributing

Default for every repository in the `abspwgm` organization. A repository with its
own `CONTRIBUTING.md` overrides this one.

## The short version

1. Open an issue first for anything larger than a typo, so the shape of the
   change is agreed before you write it.
2. Branch from `main`. `main` is protected: no force push, no deletion, linear
   history, and every change arrives as a squash-merged pull request.
3. Write the failing test first. Every project here defines the tier it belongs
   in; pick the cheapest one that can prove the behaviour.
4. Update the document that the change makes wrong, in the same pull request.
5. Push. CI runs the fast tier in under a minute and the merge tier after it.
   A red build does not merge, and a failure is fixed forward rather than rerun.

## What the standard expects of you

These are not house preferences; they are clauses of
[absolute-standard](https://github.com/abspwgm/absolute-standard/blob/main/STANDARD.md),
and the conformance check enforces them.

| Clause | What it means for a pull request |
|---|---|
| 1.1 | A behaviour — including a bug fix — begins as a failing test. The test names the behaviour, not the implementation. |
| 1.2 | A decision lives in a document, and the document changes in the same PR. A PR that leaves a document claiming otherwise is incomplete. |
| 1.3 | Anything that can drift is guarded by a check. "We will remember" is not a control. |
| 1.5 | The public contract — test keys, CLI flags, environment variables, image tags, published paths — is explicit. Renaming one is a breaking change that updates every caller in the same commit. |
| 2.2 | Every gate runs the same way locally, with one documented command and no CI credentials. |
| 2.7 | Static analysis is strict and fatal. Warnings are errors; formatting is verified, not requested. |

## Running the gates locally

Each repository documents its own commands in its README — that is clause 2.2,
and a gate that only exists inside a workflow file does not count. If you cannot
find the command, that is a bug in the README; please report it.

## Commits and pull requests

Write the commit message for someone reading it in a year with no memory of the
issue: what was wrong, what changed, and why this way rather than the obvious
alternative. One squashed commit per change, so it can be reverted cleanly.

Pull requests need one approving review from a code owner, given after the last
push, with every review conversation resolved.

## Dependencies

Pin what you add — actions by commit SHA, images by digest or exact tag, packages
by version. Nothing in these projects installs "whatever is newest at build
time"; that is clause 3, and it is there because a mod loader once did exactly
that.

## Conduct and security

The [Code of Conduct](CODE_OF_CONDUCT.md) applies everywhere in the organization.
Security problems never go in a public issue — see [SECURITY.md](SECURITY.md).
