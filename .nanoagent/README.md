# NanoAgent Workspace Files

This directory stores workspace-local NanoAgent configuration.

- `agent-profile.json`: workspace memory, audit, custom tools, and MCP server settings.
- `.nanoignore`: workspace paths excluded from NanoAgent file tools.
- `agents/*.md`: custom agents. Files ending in `.template` are inactive until renamed to `.md`.
- `skills/**/SKILL.md`: workspace skills. Template files are inactive until renamed to `SKILL.md`.
- `memory/lessons.jsonl`: reusable local lessons about mistakes, failures, and fixes.
- `logs/tool-audit.jsonl`: optional tool audit log when enabled in `agent-profile.json`.

Root-level `AGENTS.md` files are loaded as persistent workspace instructions.