# Security policy

This is the default policy for every repository in the `abspwgm` organization. A
repository that needs to say more keeps its own `SECURITY.md`, and that one wins.

## Reporting a vulnerability

Please do not open a public issue for a security problem.

Use **Report a vulnerability** on the Security tab of the affected repository.
That opens a private advisory only the maintainers can see. If the repository is
private, or the Security tab is not available to you, report it against
[this repository](https://github.com/abspwgm/.github/security/advisories/new)
and say which project it concerns.

Include the commit, image tag or version, what you did, and what happened. You
will get a reply within 7 days. Fixes ship in a new tag, and the advisory is
published once a fixed version is available.

Do not include real user data, credentials, or personal information in a report.
A minimal reproduction is enough.

## Scope

In scope: our scripts, Dockerfiles, workflows, published images, applications,
and websites.

Out of scope: vulnerabilities in a game server itself, in a mod, or in a
third-party service we integrate with. Report those to the game's publisher, the
mod's author, or the vendor. We never redistribute a game server or a mod; they
are downloaded by your container at run time.

## Supported versions

The newest release tag of each project, and the `latest` tag of each image.
Older tags do not receive fixes; update with `docker compose pull`. A project
that is pre-release supports its default branch only.

## How these projects are secured

The posture is defined once, in the Absolute engineering standard: clause 6 and
its `security/BASELINE.md` set a seven-layer baseline from L1 source to L7
operations, and its `conformance/check.py` compares each repository's declared
policy against it. An exception is allowed only where it is written down with a
reason.

Secrets are never committed. Local configuration uses an untracked `.env` beside
a committed `.env.example` that documents the required keys without values. A
credential that reaches a commit is rotated first and reported second.

## Branch protection

Every repository carries the same two rulesets — no force push, no deletion,
linear history, changes through a reviewed pull request, required status checks —
defined in `governance/` in the `absolute-game-servers` repository and applied
by script, so the protection is reviewable and changes to it go through a pull
request like any code. That repository is private; the rules it enforces are
summarised above and in [docs/NEW-REPOSITORY.md](docs/NEW-REPOSITORY.md).
