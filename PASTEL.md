# Pastel private open-kritt clone — bootstrap

**Location:** `pastel-org/open-kritt` (local clone of https://github.com/Kritt-ai/open-kritt)  
**Program:** BLG-601 / `punkdb/docs/security-audits/kritt-harness-adapters.md`  
**Policy:** No OpenAI/Anthropic providers for Punk security scans. Multi-harness: CyberStrike → Hermes → OpenCode → Pi.

## Status

- [x] Shallow clone of upstream
- [ ] Mark as Pastel private working tree (do not push to public upstream)
- [ ] `./kritt setup` with Ollama-only credentials (when adapter lands)
- [ ] Docker Compose bind 127.0.0.1 only
- [ ] Register multi-harness adapters (Track B)
- [ ] First local-path scan of `punkdb/packages/cojson`

## Safety (from upstream threat model)

1. Run stack on dedicated Docker host / Colima VM — engine is privileged (Docker socket).
2. Bind UI/API to `127.0.0.1` only; put auth in front before any LAN exposure.
3. Job containers are root + outbound net by default — add egress allowlist at host firewall when possible.
4. Prefer **local path** scans of punkdb (no `GITHUB_TOKEN` for private monorepo).
5. Treat findings as sensitive until triaged into BLG `#security`.

## Commands (host)

```bash
cd ~/projects/pastel-org/open-kritt

# Inspect only until multi-harness fork work starts
cat docker-compose.yml | head -80
./kritt --help || node scripts/kritt.mjs --help

# Do NOT run ./kritt setup with Codex/Claude credentials for Pastel security profile.
```

## Fork work plan (Track B)

1. Rename remote: `origin` = private Pastel fork; `upstream` = Kritt-ai/open-kritt  
2. Engine: add harness adapters for `cyberstrike`, `hermes`, `opencode`, `pi`  
3. Providers: `ollama` (OpenAI-compatible base URL + key); optional `xai`  
4. Seed workflows for L1 crypto boundary + L3 permissions  
5. Export findings → `punkdb/docs/security-audits/findings/`

Until Track B lands, use Track A:

```bash
cd ~/projects/pastel-org/punkdb
pnpm security:harness -- --harness cyberstrike --prompt-file docs/security-audits/prompts/l1-crypto-boundary.md
pnpm security:harness -- --harness hermes --prompt-file docs/security-audits/prompts/2026-08-04-hermes-l1-wave.md
```

## License note

open-kritt is AGPL-3.0. Self-hosting for internal Pastel use is fine; public SaaS of a modified fork has AGPL obligations. Nick owns licensing decisions.
