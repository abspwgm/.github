# brand/ — vendored, not authored

Every file under `logos/` is a copy of an asset in
[`absolute-power-brand`](https://github.com/abspwgm/absolute-power-brand), which
is the single source of truth for colour, type and marks. **Do not edit them
here.** Change the asset upstream, then:

```sh
python3 scripts/sync_brand.py            # from the brand repo's main
python3 scripts/sync_brand.py --check    # re-hash only; no network, no writes
```

`SOURCE.json` records the upstream commit and a SHA-256 per file. `--check` runs
in CI. It cannot prove the copy is *current* — that needs the private repo — but
it does prove nobody edited it in place, which is the drift that actually
happens.

The guidelines themselves are not vendored. This repository is public and the
brand strategy is internal, so `docs/BRAND_GUIDELINES.md` stays upstream and is
cited by path.

## The rasters

The organization avatar and the social preview card are uploaded by hand in
organization settings; GitHub exposes no API for either. The PNGs are built by
the `render-org-assets` workflow in `absolute-power-brand`, which installs the
real brand faces before rendering. Do not export these SVGs from a browser: the
wordmarks are live text, and without Rajdhani the render silently substitutes a
fallback face and gets the letterforms wrong.
