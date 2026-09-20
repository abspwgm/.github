# Absolute

Dedicated game servers you can run yourself, collection tooling for trading-card
games, and the engineering standard both are held to.

Every project here is built the same way, because the standard is a repository
rather than a habit: a behaviour begins as a failing test, a decision lives in a
document that changes in the same pull request, and anything that can drift is
guarded by a check instead of by discipline.

## Game servers

Docker images for dedicated servers that update themselves, back up your world,
and **hold** instead of breaking on patch day. The registry tracks 62 games: 1
live, 2 at parity, 50 planned, 9 blocked on an upstream that does not ship a
dedicated server.

[**The fleet board**](https://abspwgm.github.io/absolute-game-servers/) is the
live view: every game, its status, and how to run the ones that are ready.

| | |
|---|---|
| [absolute-valheim-server](https://github.com/abspwgm/absolute-valheim-server) | Valheim, vanilla and BepInEx, with an end-to-end disaster-recovery harness |
| [absolute-palworld-server](https://github.com/abspwgm/absolute-palworld-server) | Palworld |
| [absolute-server-template](https://github.com/abspwgm/absolute-server-template) | The template every image above is cut from |

Rust, Satisfactory and 7 Days to Die are being built and are not published yet.
A server image becomes public once its end-to-end suite is green — something has
to start it, play against it and restore it before we hand it to anyone. Until
then there is nothing to show that we would trust ourselves.

## How it is built

| | |
|---|---|
| the Absolute engineering standard | The engineering standard: process, quality signals, a seven-layer security baseline, and a conformance check that enforces both |

Every clause in the standard is the scar of a real failure on the Valheim image —
a mod loader that installed whatever was newest, a remote console shipped with
`changeme`, a nightly job that drained a CI budget. The point of writing them
down is that the next project does not have to earn them again.

## Getting in touch

[**Discord**](https://discord.gg/ufC2RFxxkx) — questions, help getting a server running, and finding
people to play with.

Bugs and requests go in the affected repository's issues. Security problems go
through **Report a vulnerability** on that repository's Security tab, never a
public issue — see [the security policy](https://github.com/abspwgm/.github/blob/main/SECURITY.md).
