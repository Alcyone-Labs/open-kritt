# Pastel private open-kritt fork — bootstrap

**Location:** `pastel-org/open-kritt`  
**Remotes:**
- `origin` → `git@github.com:Alcyone-Labs/open-kritt.git` (Pastel private fork)
- `upstream` → `https://github.com/Kritt-ai/open-kritt.git`

**Program:** BLG-601 / `punkdb/docs/security-audits/kritt-harness-adapters.md`  
**Policy:** No OpenAI/Anthropic providers for Punk security scans. Multi-harness: CyberStrike → Hermes → OpenCode → Pi.

## Status

- [x] Shallow clone of upstream
- [x] `origin` = Alcyone-Labs private fork; `upstream` = Kritt-ai
- [x] `PastelCliHarness` registered (`cyberstrike`, `hermes`, `opencode`, `pi`)
- [x] Backend constants + generation allow `ollama` provider pairing
- [ ] `./kritt setup` Ollama credentials path (engine provider_credentials)
- [ ] Docker Compose bind 127.0.0.1 only + egress allowlist
- [ ] Job images ship / mount CyberStrike + Hermes binaries
- [ ] First local-path scan of `punkdb/packages/cojson`

## Safety (from upstream threat model)

1. Run stack on dedicated Docker host / Colima VM — engine is privileged (Docker socket).
2. Bind UI/API to `127.0.0.1` only; put auth in front before any LAN exposure.
3. Job containers are root + outbound net by default — add egress allowlist at host firewall when possible.
4. Prefer **local path** scans of punkdb (no `GITHUB_TOKEN` for private monorepo).
5. Treat findings as sensitive until triaged into BLG `#security`.
6. Do **not** `git push upstream`. Push Pastel changes only to `origin` after Nick review.

## Commands

```bash
cd ~/projects/pastel-org/open-kritt
git remote -v
# origin    git@github.com:Alcyone-Labs/open-kritt.git
# upstream  https://github.com/Kritt-ai/open-kritt.git

# Engine unit smoke for Pastel harnesses
cd engine && python -m pytest tests/test_pastel_harnesses.py -q

# Until full compose is ready, use Track A runner:
cd ~/projects/pastel-org/punkdb
pnpm security:harness -- --harness cyberstrike --prompt-file docs/security-audits/prompts/l1-crypto-boundary.md
pnpm security:harness -- --harness hermes --prompt-file docs/security-audits/prompts/2026-08-04-hermes-l1-wave.md
```

## License note

open-kritt is AGPL-3.0. Self-hosting for internal Pastel use is fine; public SaaS of a modified fork has AGPL obligations. Nick owns licensing decisions.
