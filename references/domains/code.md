# Domain: Code

Applies to features, scripts, tools, and multi-file changes.

## 1. Definition of done

- Runs from a clean checkout with documented setup.
- Entry point obvious: one command to build, one to run, one to test.
- Failure paths handled: invalid input, empty result, timeout, permission, network failure.
- No speculative abstraction. One use: inline. Two uses: a function. Three or more: a module.
- No dead code, commented-out blocks, or TODO in delivered paths.
- Tests, or a reproducible check command, for the behavior that matters.
- Versions pinned or stated; examples match the version in use.

## 2. Craft minimums

- Names reveal intent: `retry_with_backoff` beats `handle2`.
- Functions do one thing at one level of abstraction.
- Validate at boundaries: user input, network, files, environment. Trust internal calls.
- Fail loudly: no silent `except: pass`, no default that hides a broken state.
- Comments explain why, not what; if the what needs a comment, rename things.
- Errors carry context: what was attempted, with what input, what to do next.
- Configuration is explicit at the edge, not read from globals deep inside.

## 3. Verification

1. Run it; a snippet never executed is a hypothesis.
2. Run the tests, then exercise failure cases manually if untested.
3. Check the API against the installed version, not memory.
4. Check dependency changes: lockfile diff, new transitive packages, license. Confirm each new package exists in the registry and is intended; hallucinated and typosquatted names both install cleanly.
5. Check secrets: nothing committed, logged, or in error output.
6. Read the diff; every changed line should trace to the request. Unrelated changes are noise or accidents.

## 4. Security basics

- No secrets in code, logs, or error output.
- Parameterized queries, never string-built SQL.
- Escape output at the boundary where it is rendered.
- Validate file paths against traversal.
- Treat deserialization and shell invocation as hostile input surfaces.
- Least privilege for tokens, scopes, and filesystem access.

## 5. Failure modes

- Unrequested abstraction or configuration.
- Happy-path-only implementation.
- Swallowed exceptions.
- Unverified API calls that compile but fail at runtime.
- Dependency bloat for a one-line problem.
- Tests that assert the implementation instead of behavior.
- Refactoring adjacent code the request did not touch.

## 6. Verification before delivery

- Clean checkout runs.
- Tests pass.
- Error paths exercised at least once.
- Diff reviewed line by line.
- Setup and run instructions accurate for someone who has never seen the repository.
