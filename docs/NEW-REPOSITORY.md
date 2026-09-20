# Starting a new repository in this organization

What a new repository gets, in the order that avoids locking yourself out of
it. The steps are short; the order is the part that matters, and most of the
notes below are mistakes that were actually made rather than hypotheticals.

Governance definitions and the scripts live in `governance/` and `scripts/` in
**`absolute-game-servers`**. That repository is private, so clone it first.

## 1. Create it private

```sh
gh repo create abspwgm/<name> --private --description "<one line>"
```

**Private first, always.** A repository becomes public only once its end-to-end
tier is green — [the standard][std], clause 8.1. Publishing source is a claim
that it works, and the end-to-end tier is the only evidence for that claim.
Nothing forces you to publish later; red forbids it, green merely permits it.

## 2. Scaffold it before protecting it

Copy the shape from [`absolute-server-template`][tpl] for a game image, or from
`absolute-unifi` for a repository that is not one:

| Path | Why |
|---|---|
| `.absolute/policy.yml` | How this project meets each clause (7.1) |
| `.github/workflows/conformance.yml` | Calls the standard's reusable check (7.2) |
| `.github/workflows/<fast-tier>.yml` | A signal in under a minute (2.1) |
| `.github/CODEOWNERS` | `* @abspowergaming` |
| `SECURITY.md` | Private reporting, and what the repo never contains (L7) |
| `LICENSE`, `README.md`, `.gitattributes` | |
| `tests/` | The fast tier has to actually run something |

### Pin the standard and declare the same version

The single most common failure. `conformance.yml` pins a commit of
the standard, and `.absolute/policy.yml` declares `standard_version`.
**`check.py` compares them exactly**, so a scaffold copied from the template
inherits the template's older pin and fails on its first run:

```
FAIL  [7.3] policy pins standard 1.2.0, this standard is 1.0.0
```

Pin a commit carrying the version you are declaring. A new repository should
adopt the current standard rather than inherit whatever the template pinned.

### Run the check before you push

```sh
python3 conformance/check.py --repo .
```

Answer honestly. A clause you do not yet meet is an **exception with a reason
and an expiry** (7.4), never a requirement quietly marked met. A scaffold that
cannot do the thing yet should say so — that is what the exception mechanism is
for, and an expired one fails the check, which is how a temporary decision stays
temporary.

## 3. Push `main` first, then protect it

```sh
git push -u origin main
```

Do this **before** the next step. The ruleset forbids direct pushes to the
default branch, so once it is applied your initial commit has to arrive through
a pull request — and on an empty repository there is no base branch to open one
against.

## 4. Apply the rulesets

```sh
cd absolute-game-servers
python3 scripts/apply_rulesets.py --dry-run
python3 scripts/apply_rulesets.py
python3 scripts/apply_rulesets.py --check     # every repository covered?
```

Repositories are discovered from the organization, so a new one needs no edit
to any list. Everything after this point goes through a pull request: no force
push, no deletion, linear history, squash merge, review threads resolved.

## 5. Declare required checks, and label it

Add the checks the repository actually runs to `governance/required-checks.json`:

```json
"absolute-<name>": ["Conformance", "Lint (shellcheck)"]
```

Only checks that run on **every** pull request belong here. A required check
that a path filter skips blocks every pull request in that repository forever.
A repository with no entry still gets branch protection — it just gets no
required status checks.

```sh
python3 scripts/apply_labels.py
```

30 labels and 6 milestones, the same set everywhere.

## 6. Publish it when it has earned it

Bring the end-to-end tier green, then flip visibility. `scripts/check_visibility.py`
runs daily and fails a repository that is public while its E2E is not green, so
this is checked rather than remembered.

If it becomes public, check that nothing public still links to it *as a private
repository*, and nothing in it links back out to one — clause 8.2. Generated
links are guarded by their generator; hand-written prose, install snippets and
buttons are where stale links actually survive.

[std]: https://github.com/abspwgm/.github
[tpl]: https://github.com/abspwgm/absolute-server-template
