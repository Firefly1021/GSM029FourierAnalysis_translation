"""Translation requires an explicit Codex/agent processor; never emit placeholder translations."""
raise SystemExit(
    "No standalone translator is bundled. Configure the high-level translation processor or run this stage through Codex."
)
