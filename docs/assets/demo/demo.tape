# Nuclear-grade README demo. Render from the repository root:
#   vhs docs/assets/demo/demo.tape
# tests/test_demo_tape.py replays every Type line below and checks each beat still
# prints. It does not render the GIF: re-render after changing the tape or commands. Tool calls are simulated; no agent runs.

Output docs/assets/demo/demo.gif

Set Shell "bash"
Set FontSize 16
Set Width 1440
Set Height 450
Set Padding 24
Set Theme "Builtin Solarized Light"
Set TypingSpeed 35ms

Hide
Type `export PS1='$ ' D=$(mktemp -d) EX=docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions`
Enter
Type `R=$PWD; alias ng="python $R/tools/ng.py" sim="python $R/docs/assets/demo/simulate_tool_call.py"`
Enter
Type `ng init $D >/dev/null && ng new add-fetch-tool --mode quick --repo $D >/dev/null && clear`
Enter
Show

Type `# 1. An agent tries to rewrite the CI that judges it (simulated call)`
Enter
Type `sim Write .github/workflows/ci.yml`
Enter
Sleep 2.5s

Type `# 2. ...or force-push straight to main`
Enter
Type `sim Bash "git push --force origin main"`
Enter
Sleep 2.5s

Type `# 3. A passing record still shows its open gaps`
Enter
Type `ng validate $EX --json | grep -E '"ok"|open_evidence'`
Enter
Sleep 2s
Type `ng badge .`
Enter
Sleep 2.5s

Type `# 4. A change record nobody filled in does not pass`
Enter
Type `(cd $D && ng validate .nuclear/changes/add-fetch-tool | head -2)`
Enter
Sleep 4s
