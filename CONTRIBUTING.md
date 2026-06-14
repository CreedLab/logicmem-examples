# Contributing to LogicMem Examples

🎉 Thanks for wanting to contribute! Every example helps developers understand how AI memory should work.

## How to Add an Example

1. **Fork the repo** and create your branch:
   ```bash
   git checkout -b examples/add-my-use-case
   ```

2. **Add your example** in the `examples/` directory:
   - Follow the naming convention: `XX_name.py` (e.g., `06_customer_support.py`)
   - Include a clear docstring at the top explaining what it demonstrates
   - Keep it under 100 lines if possible

3. **Update README.md** — add your example to the table in the Examples section

4. **Test it** — make sure it runs with just `pip install logicmem` and a valid `LOGICMEM_API_KEY`

5. **Submit a PR** — we'll review and merge fast

## Style Guide

### DO:
- ✅ Use clear, descriptive docstrings
- ✅ Keep examples copy-paste runnable (no partial code)
- ✅ Show realistic use cases, not toy examples
- ✅ Include comments explaining the "why"
- ✅ Use `outcome_score` and `importance` parameters to show depth
- ✅ Make the output interesting — don't just `print("hello")`

### DON'T:
- ❌ No abstract/generic examples ("foo" and "bar")
- ❌ No code that requires external services beyond LogicMem
- ❌ No overly complex examples — if it needs 500 lines, split it up
- ❌ No markdown/code blocks outside of Python files — everything should run

## Good Example Topics

- Customer support agent with memory
- Code review assistant that remembers past decisions
- Sales agent that tracks what worked
- Research agent that builds knowledge over time
- Personal assistant that remembers your preferences
- Multi-agent system with shared memory

## Questions?

Jump into our Discord: https://logicmem.io/discord

We're a small team but we respond fast. If you have an idea for an example but don't want to build it yourself, open an issue — someone might pick it up.
