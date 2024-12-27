# Python Watch Linter PoC

This repository demonstrates how to set up a custom Python linter (using a `watcher.py` script) that:

1. Monitors `.py` files for changes (using the [`watchdog`](https://pypi.org/project/watchdog/) library).
2. Runs the custom linter (`cli.py`) upon each modification.
3. In VSCode, automatically updates (removes old and shows new) problems in the “Problems” panel thanks to the **background problem matcher** configuration in `tasks.json`.

## Project Structure

```
my-linter/
├── .vscode/
│   └── tasks.json
├── cli.py
├── watcher.py
├── linter/
│   ├── __init__.py
│   ├── runner.py
│   └── rules/
│       ├── __init__.py
│       ├── base_rule.py
│       └── print_rule.py
└── README.md
```

### Files Overview

- **`cli.py`**  
  The entry point for your custom Python linter. It imports your linting logic from `linter/runner.py` and outputs issues in the format:

  ```
  filename:line: message
  ```

  This format matches the regex used by the VSCode problem matcher.

- **`watcher.py`**  
  Uses the `watchdog` library to monitor `.py` files. Whenever a file changes, it:

  1. Prints a “start marker” (`PY_LINT: START_LINT`).
  2. Runs `cli.py`.
  3. Prints an “end marker” (`PY_LINT: END_LINT`).

- **`.vscode/tasks.json`**  
  Defines a background task called **“Watch Linter”**. The task runs `watcher.py`, and uses a **problem matcher** to capture the lint output, **clearing old problems** when it sees the `PY_LINT: START_LINT` line and finalizing the collection upon `PY_LINT: END_LINT`.

- **`linter/`**  
  Contains the core logic of your custom Python linter, including `runner.py` (which orchestrates AST analysis) and the `rules` subpackage (where each rule is implemented in a separate file).

## How It Works

1. **Watchdog**:  
   `watcher.py` monitors changes in Python files via the watchdog library.
2. **Markers**:  
   To help VSCode know when a new “lint round” starts and ends, the script prints:
   ```python
   print("PY_LINT: START_LINT")
   # ... run cli.py ...
   print("PY_LINT: END_LINT")
   ```
3. **Problem Matcher**:  
   The `background.beginsPattern` tells VSCode “clear the old problems and start collecting new ones” when it matches `PY_LINT: START_LINT`.  
   The `background.endsPattern` tells VSCode “stop collecting and display them” when it sees `PY_LINT: END_LINT`.  
   Meanwhile, each line from `cli.py` that matches the pattern `^([^:]+):(\d+): (.*)$` is turned into a problem with:
   - **file** = group 1,
   - **line** = group 2,
   - **message** = group 3.

---

## Customization

- **Additional Linter Rules**:  
  You can create more AST-based rules in the `linter/rules/` folder, each extending a base class (e.g., `base_rule.py`).
- **Project-wide vs. Single-file**:  
  Currently, `watcher.py` calls your `cli.py` for the **modified file**. You could update it to lint the entire workspace on each save if desired.
- **Patterns**:  
  If you print additional log lines, they won’t appear as errors in the Problems panel unless they match the regex in `pattern`.

---

## Known Caveats

- **Continuous Watch**:  
  The watcher runs until you press `Ctrl + C` in the terminal or close the VSCode task.
- **Terminal Clutter**:  
  The printed `PY_LINT: START_LINT` and `END_LINT` lines will appear in the terminal. You could silence them or format them differently if you prefer.
- **One-time vs. Real-time**:  
  If you want a more seamless experience (like ESLint’s underline in the editor, immediate feedback, etc.), consider creating a **VSCode extension** or leveraging Python extension hooks (like a `pylint` plugin).

---

## Conclusion

Using a **background task** and **Problem Matcher** is a quick way to simulate a real-time linting experience in VSCode without writing a full-fledged extension. As files change, the script runs your custom Python linter and updates issues in the “Problems” panel, removing older messages automatically by leveraging the `beginsPattern` and `endsPattern` configuration.

Feel free to adapt this approach for your own linter, add more rules, and customize the watch logic to fit your team’s workflow.
