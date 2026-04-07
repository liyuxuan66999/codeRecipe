def toBullets(stats: list[str]) -> str:
    cleaned = [s.strip() for s in stats if isinstance(s, str) and s.strip()]
    return "\n".join(f"- {s}" for s in cleaned)