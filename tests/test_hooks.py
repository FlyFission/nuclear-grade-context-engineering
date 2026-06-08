import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOOKS = ROOT / "hooks"
HOOK_SCRIPTS = sorted(HOOKS.glob("*.py"))

# F2: in-session hooks must be pure standard library with no network or subprocess use.
BANNED = ("socket", "urllib", "requests", "http", "subprocess", "ftplib", "smtplib", "telnetlib")

# Lens 2 / A8: the SessionStart preamble mirrors CORE.md's decision matrix; guard the mirror.
CLUSTERS = (
    "Agent authority",
    "Configuration management",
    "Claims discipline",
    "Incident & deficiency",
    "Hygiene",
)


def _run_hook(script: Path, stdin_obj: dict) -> dict:
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=json.dumps(stdin_obj),
        text=True,
        capture_output=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


def test_hook_scripts_exist():
    assert HOOK_SCRIPTS, "expected hook scripts under hooks/"


def test_hooks_are_pure_stdlib_and_zero_network():
    for script in HOOK_SCRIPTS:
        src = script.read_text(encoding="utf-8")
        for banned in BANNED:
            assert banned not in src, f"{script.name} must not reference {banned!r} (zero-network, pure-stdlib)"


def test_session_start_injects_a_static_preamble():
    out = _run_hook(HOOKS / "session_start.py", {"hook_event_name": "SessionStart", "source": "startup"})
    ctx = out["hookSpecificOutput"]["additionalContext"]
    assert "state the mode" in ctx
    assert "advisory" in ctx.lower()  # the honesty note must be present
    assert len(ctx) < 2200, "preamble must stay within its ~300-token budget"


def test_user_prompt_submit_never_echoes_the_prompt():
    secret = "ZZZ-do-not-echo-this-prompt-ZZZ"
    out = _run_hook(
        HOOKS / "user_prompt_submit.py",
        {"hook_event_name": "UserPromptSubmit", "user_prompt": secret},
    )
    ctx = out["hookSpecificOutput"]["additionalContext"]
    assert secret not in ctx, "the injected line must be static, never the user's prompt"
    assert "state the mode" in ctx


def test_preamble_has_no_injection_markers():
    src = (HOOKS / "session_start.py").read_text(encoding="utf-8").lower()
    for marker in ("ignore previous", "disregard", "override the", "auto-approve", "exfiltrate", "system:"):
        assert marker not in src, f"preamble contains an injection marker: {marker!r}"


def test_preamble_clusters_stay_in_sync_with_core():
    core = (ROOT / "CORE.md").read_text(encoding="utf-8")
    preamble = (HOOKS / "session_start.py").read_text(encoding="utf-8")
    for cluster in CLUSTERS:
        assert cluster in core, f"cluster missing from CORE.md: {cluster}"
        assert cluster in preamble, f"preamble drifted from CORE.md (missing cluster): {cluster}"
