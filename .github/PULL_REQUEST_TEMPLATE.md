## What changed and why

<!-- What was wrong, what this does about it, and why this way rather than the
     obvious alternative. Written for someone reading it in a year. -->

Closes #

## The test that proves it

<!-- Clause 1.1: name the test and the tier it runs in. For a bug fix, the test
     that failed before this change and passes after it. -->

- Test:
- Tier:

## Checklist

- [ ] A failing test came first, and the whole suite is green (1.1)
- [ ] Every document this makes wrong is updated in this PR (1.2)
- [ ] Anything that could drift is guarded by a check, not by a note (1.3)
- [ ] No change to the public contract — or every caller is updated here (1.5)
- [ ] The gates run locally with the documented command (2.2)
- [ ] Analysis and formatting are clean with warnings fatal (2.7)
- [ ] New dependencies are pinned; no secrets, keys or real data in the diff

## Risk and rollback

<!-- What breaks if this is wrong, and how to undo it. "Revert the commit" is a
     fine answer; say so. Note any migration, data change or manual step. -->
