# Vendored standard

This directory is a copy of the machine-readable half of the Absolute
engineering standard at commit `fb8ff70ecd01e6e6f23291d442d69f310ded08f6`,
standard version **1.0.0**, matching the `standard_version` declared in
`../policy.yml`.

The copy was taken from `absolute-server-template`, which already carries this
version verbatim, rather than from the standard itself, so that the two public
repositories run byte-identical checkers and a refresh moves them together.

It is vendored because the standard lives in a private repository, and a public
repository cannot call a reusable workflow from a private one. This repository
has to be public — GitHub only honours an organisation profile page and default
community health files from a public `.github` repository, including for the
private repositories that inherit them — so calling the standard is not an
option here. Only what `check.py` actually reads is present; the prose
(`STANDARD.md`, `BASELINE.md`) is not.

| Path | What it is |
|---|---|
| `VERSION` | The standard version `check.py` compares against `../policy.yml` (7.3) |
| `conformance/check.py` | The conformance check |
| `security/baseline.policy.yml` | The seven-layer security floor (clause 6) |
| `security/base-images.yml` | The approved base image library |

`security/base-images.yml` is unused here — this repository builds no image and
records `base_image_from_approved_library` as not applicable — but `check.py`
reads it whenever a policy declares `build.base_images`, so it is vendored with
the rest rather than left out to be missed later.

## The differences from the original

Two, both already present in the copy this was taken from, and both there to
keep the private repository's name out of a public one:

- The secret-scanner escape hatch is spelled `absolute-conformance:allow-secret`
  rather than the name the standard uses. No file in this repository uses the
  marker.
- The `--standard` argument's help text says "checkout of the standard" rather
  than naming the private repository.

Nothing else differs: `VERSION`, `security/baseline.policy.yml` and
`security/base-images.yml` are byte-identical to the standard at that commit,
and `check.py` differs only in the two lines above.

## Keeping it current

`check.py` compares `VERSION` against `../policy.yml` exactly, so these move
together or the check fails. Refreshing to a newer standard means copying these
four files again from that version and bumping `standard_version` in the same
pull request.
