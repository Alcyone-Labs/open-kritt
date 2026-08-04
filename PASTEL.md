# Pastel private open-kritt fork — bootstrap

**Location:** `/Users/nemb/projects/pastel-org/open-kritt`  
**Remotes:**
- `origin` → `git@github.com:Alcyone-Labs/open-kritt.git` (Pastel private fork — **only push target**)
- `upstream` → `https://github.com/Kritt-ai/open-kritt.git` (**fetch only** — push URL disabled)

**Program:** BLG-601 / `punkdb/docs/security-audits/kritt-harness-adapters.md`  
**Policy:** No OpenAI/Anthropic for Punk security scans. Harnesses: CyberStrike → Hermes → OpenCode → Pi.

---

## Git workflow (so pull/push stay healthy)

`main` **tracks `origin/main`**, never `upstream/main`.

```bash
cd ~/projects/pastel-org/open-kritt

# Daily Pastel work
git pull                  # = pull from origin
git push                  # = push to origin (Alcyone-Labs)

# Sync Kritt upstream (read-only) onto our fork
git fetch upstream
git rebase upstream/main  # or: git merge upstream/main
git push --force-with-lease origin main   # only after a rebase rewrote history

# Never
git push upstream …       # blocked (push URL = DISABLE_DO_NOT_PUSH)
```

If `git status` shows `main...upstream/main [ahead N, behind M]`, tracking is wrong:

```bash
git branch -u origin/main
git status -sb            # should show main...origin/main
```

Re-disable upstream push if someone re-enabled it:

```bash
git remote set-url --push upstream DISABLE_DO_NOT_PUSH
```

**Last healthy sync:** 2026-08-04 — rebased 3 Pastel commits onto upstream (+35), force-with-lease to `origin`.

---

## Operational default: Track A (what works today)

**Do not wait on kritt-managed Ollama credentials.** Deep waves run on the host via the Punk runner; CLIs use their own auth.

| Piece | Where |
|-------|--------|
| Runner | `punkdb/scripts/security-harness-run.mjs` → `pnpm security:harness` |
| Gate | `punkdb` → `pnpm security:gate` |
| CyberStrike Ollama | `cyberstrike auth` → `~/.local/share/cyberstrike/auth.json` |
| Hermes Ollama | Hermes profile / `hermes model` (ollama-cloud) |
| Findings | `punkdb/docs/security-audits/findings/` |

### Run a wave

```bash
cd ~/projects/pastel-org/punkdb

# Deterministic floor
pnpm security:gate

# Dry-run (prints command only)
pnpm security:harness -- --dry-run --harness cyberstrike \
  --workdir packages/cojson \
  --prompt-file docs/security-audits/prompts/l1-crypto-boundary.md

# Live CyberStrike L1 (writes under findings/ when the agent complies)
pnpm security:harness -- --harness cyberstrike \
  --workdir . \
  --model ollama-cloud/deepseek-v4-flash:0731 \
  --prompt-file docs/security-audits/prompts/2026-08-04-cyberstrike-l1-wave.md \
  --out /tmp/cs-wave.json

# Hermes confirm / Punk-aware follow-up
pnpm security:harness -- --harness hermes \
  --prompt-file docs/security-audits/prompts/2026-08-04-hermes-l1-wave.md \
  --model deepseek-v4-flash:0731 \
  --provider ollama-cloud \
  --out /tmp/hermes-wave.json
```

Note: `pnpm security:harness -- <args>` — the bare `--` is stripped by the runner.

### Credentials checklist (Track A)

```bash
cyberstrike auth list    # need Ollama Cloud
which cyberstrike hermes
hermes status            # provider/model as configured
```

No `open-kritt/.env` Ollama key required for Track A.

---

## Track B (deferred) — full kritt stack

Scaffold only until we need workflows/de-dup UI:

- [x] Clone + `origin` fork remote
- [x] `PastelCliHarness` + `ollama` provider **name** in constants
- [ ] First-class Ollama secret in `provider_credentials.py` / Accounts (not needed for Track A)
- [ ] Compose hardened + runner images with CLIs
- [ ] First multi-depth ranked scan via kritt UI

Push Pastel commits to the fork when ready:

```bash
cd ~/projects/pastel-org/open-kritt
git push -u origin main    # never push upstream
```

## Safety

1. Local targets only unless Nick authorizes otherwise.  
2. Hunters never fix/push. Findings → quarantine → BLG `#security`.  
3. Do not push to `upstream`.

## License

AGPL-3.0 — Nick owns commercial/SaaS decisions.
