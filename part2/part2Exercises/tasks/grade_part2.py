#!/usr/bin/env python3
"""
Part 2 Grader — awards 1 point per correct task and persists progress.
Usage:
    python part2Exercises/grade_part2.py
    (Windows) python part2Exercises\\grade_part2.py
"""
from __future__ import annotations
import json, os, sys, subprocess, time, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # /.../part2Exercises
REPO_ROOT = ROOT.parent                      # part2 folder
WORKSPACE_ROOT = REPO_ROOT.parent            # repository/workspace root
# Use shared workspace-level progress file for all parts
PROGRESS = WORKSPACE_ROOT / ".progress" / "points.json"
PROGRESS_DIR = PROGRESS.parent
MARKSHEET_DIR = WORKSPACE_ROOT / ".progress"

# For non-interactive tasks: key is filename, value is expected output string
EXPECTED = {
    # Section 2.4.7 - Story (non-interactive once inputs provided)
}

# For interactive tasks: key is filename, value is dict with "inputs" (list) and "expected_output" (string)
INTERACTIVE = {
    # Section 2.1 - Programming terminology
    "2.1.1_fix_syntax.py": {
        "inputs": ["150"],
        "expected_output": "Please type in number: The number was greater than one hundred\nNow its value has decreased by one hundred\nIts value is now50\n"
    },
    "2.1.2_number_of_characters.py": {
        "inputs": ["python"],
        "expected_output": "Please type in a word: There are 6 letters in the word python\nThank you!\n"
    },
    "2.1.3_typecasting.py": {
        "inputs": ["1.34"],
        "expected_output": "Please type in a number: Integer part: 1\nDecimal part: 0.34\n"
    },
    
    # Section 2.2 - More conditionals
    "2.2.1_age_of_maturity.py": {
        "inputs": ["32"],
        "expected_output": "How old are you? You are of age!\n"
    },
    "2.2.2_greater_than_or_equal_to.py": {
        "inputs": ["5", "8"],
        "expected_output": "Please type in the first number: Please type in another number: The greater number was: 8\n"
    },
    "2.2.3_the_elder.py": {
        "inputs": ["Alan", "26", "Ada", "27"],
        "expected_output": "Person 1:\nName: Age: Person 2:\nName: Age: The elder is Ada\n"
    },
    "2.2.4_alphabetically_last.py": {
        "inputs": ["car", "scooter"],
        "expected_output": "Please type in the 1st word: Please type in the 2nd word: scooter comes alphabetically last.\n"
    },
    
    # Section 2.3 - Combining conditions
    "2.3.1_age_check.py": {
        "inputs": ["13"],
        "expected_output": "What is your age? Ok, you're 13 years old\n"
    },
    "2.3.2_nephews.py": {
        "inputs": ["Morty"],
        "expected_output": "Please type in your name: I think you might be one of Mickey Mouse's nephews.\n"
    },
    "2.3.3_grades_and_points.py": {
        "inputs": ["76"],
        "expected_output": "How many points [0-100]: Grade: 3\n"
    },
    "2.3.4_fizzbuzz.py": {
        "inputs": ["45"],
        "expected_output": "Number: FizzBuzz\n"
    },
    "2.3.5_leap_year.py": {
        "inputs": ["2020"],
        "expected_output": "Please type in a year: That year is a leap year.\n"
    },
    "2.3.6_alphabetically_in_the_middle.py": {
        "inputs": ["x", "c", "p"],
        "expected_output": "1st letter: 2nd letter: 3rd letter: The letter in the middle is p\n"
    },
    "2.3.7_gift_tax_calculator.py": {
        "inputs": ["27000"],
        "expected_output": "Value of gift: Amount of tax: 1900.0 euros\n"
    },
    
    # Section 2.4 - Simple loops
    "2.4.1_shall_we_continue.py": {
        "inputs": ["Y", "Y", "N"],
        "expected_output": "Shall we continue? Shall we continue? Shall we continue? Okay then!\n"
    },
    "2.4.2_input_validation.py": {
        "inputs": ["14", "-2", "11", "8"],
        "expected_output": "Please type in a number: Please type in a number: Please type in a number: Please type in a number: You typed in: 8\n"
    },
    "2.4.3_fix_the_code_countdown.py": {
        "inputs": ["5"],
        "expected_output": "Are you ready?\nPlease type in a number: 5\n4\n3\n2\n1\nNow!\n"
    },
    "2.4.4_repeat_password.py": {
        "inputs": ["sekred", "secret", "cantremember", "sekred"],
        "expected_output": "Password: Repeat password: They do not match!\nRepeat password: They do not match!\nRepeat password: User account created!\n"
    },
    "2.4.5_pin_and_number_of_attempts.py": {
        "inputs": ["3245", "1234", "0000", "4321"],
        "expected_output": "PIN: Wrong\nPIN: Wrong\nPIN: Wrong\nPIN: Correct\nYou tried 4 times\n"
    },
    "2.4.6_the_next_leap_year.py": {
        "inputs": ["2019"],
        "expected_output": "Year: The next leap year after 2019 is 2020\n"
    },
    "2.4.7_story.py": {
        "inputs": ["Mary", "dancer"],
        "expected_output": "Please type in a name: Please type in a profession: Here is the story:\nMary is a dancer. Mary is an exceptional dancer. Mary is a Finnish dancer whose parents are of Martian descent.\n"
    },
    "2.4.8_working_with_numbers.py": {
        "inputs": ["2", "10"],
        "expected_output": "First: Last: 2\n4\n6\n8\n10\n"
    },
}

def load_state():
    if PROGRESS.exists():
        try:
            return json.loads(PROGRESS.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"parts": {}, "total_points": 0, "updated_at": None}

def save_state(state):
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    PROGRESS.write_text(json.dumps(state, indent=2), encoding="utf-8")

def write_marksheet(state: dict, user: str | None) -> None:
    """Render a marksheet markdown file in workspace-level .progress with per-part details."""
    MARKSHEET_DIR.mkdir(parents=True, exist_ok=True)
    lines = []
    title_name = user if user else "Student"
    lines.append("# Fundamentals of Programming")
    lines.append("")
    lines.append(f"## Hi {title_name}, check your scores below!")
    lines.append("")
    lines.append(f"Last updated: {state.get('updated_at','')}")
    lines.append("")
    # Table header
    lines.append("| Part | Score | Max | Percent | Progress |")
    lines.append("|------|-------|-----|---------|----------|")
    parts = state.get("parts", {})
    # Sort parts numerically when possible
    def part_sort_key(k: str):
        try:
            return (0, int(k))
        except Exception:
            return (1, str(k))
    for part_key in sorted(parts.keys(), key=part_sort_key):
        p = parts[part_key]
        score = int(p.get("score", 0))
        total = int(p.get("total", 0))
        percent = int(round((score / total) * 100)) if total else 0
        # simple 10-char bar
        filled = int(round((score / total) * 10)) if total else 0
        bar = "█" * filled + "░" * (10 - filled)
        lines.append(f"| Part {part_key} | {score} | {total} | {percent}% | {bar} |")
    lines.append("")
    # Calculate max points excluding Part 5 (Parts 1-4, 6: 31+22+34+37+19 = 143)
    max_points = sum(p.get("total", 0) for k, p in parts.items() if k != "5")
    current_points = int(state.get('total_points', 0))
    lines.append(f"**Total points:** {current_points}/{max_points}")
    
    # Calculate grade on 4-point scale
    percentage = (current_points / max_points * 100) if max_points > 0 else 0
    if percentage < 50:
        grade = "Fail"
    elif percentage < 65:
        grade = "1"
    elif percentage < 85:
        grade = "2"
    else:
        grade = "3"
    lines.append(f"**Grade:** {grade} ({percentage:.1f}%)")
    lines.append("")
    lines.append("_Note: Part 5 is optional and not counted toward the total._")
    lines.append("")
    # Detailed per-part task summary
    if parts:
        lines.append("## Details by Part")
        for part_key in sorted(parts.keys(), key=part_sort_key):
            p = parts[part_key]
            tasks = p.get("tasks", {}) or {}
            passed = [t for t, ok in tasks.items() if ok]
            failed = [t for t, ok in tasks.items() if not ok]
            lines.append("")
            lines.append(f"### Part {part_key}")
            lines.append(f"- Tasks passed: {len(passed)}")
            lines.append(f"- Tasks failed: {len(failed)}")
            if failed:
                lines.append("- Failed task files:")
                for f in sorted(failed):
                    lines.append(f"  - `{f}`")
    lines.append("")
    lines.append("> This file is auto-generated by the grader whenever it runs.")

    (MARKSHEET_DIR / "marksheet.md").write_text("\n".join(lines), encoding="utf-8")

def _run_capture(args: list[str], cwd: Path | None = None, timeout: int = 5) -> tuple[int, str]:
    """Run a command and return (returncode, stdout). Never raises; returns (1, "") on failure."""
    try:
        proc = subprocess.run(args, cwd=str(cwd) if cwd else None, text=True, capture_output=True, timeout=timeout)
        return proc.returncode, proc.stdout.strip()
    except Exception:
        return 1, ""

def get_display_user() -> str | None:
    """Best-effort GitHub/VS Code identity for display.

    Priority:
    1) Env vars: GITHUB_USER/GITHUB_USERNAME/GH_USER
    2) GitHub CLI (gh): gh api user --jq .login
    3) Git user.name
    4) Owner parsed from git remote origin URL
    5) OS username (USERNAME/USER)
    """
    # 1) Environment variables
    for key in ("GITHUB_USER", "GITHUB_USERNAME", "GH_USER"):
        v = os.environ.get(key)
        if v:
            return v.strip()

    # 2) GitHub CLI
    if shutil.which("gh"):
        rc, out = _run_capture(["gh", "api", "user", "--jq", ".login"])  # requires gh auth login
        if rc == 0 and out:
            return out

    # 3) git user.name
    rc, out = _run_capture(["git", "-C", str(REPO_ROOT), "config", "--get", "user.name"])
    if rc == 0 and out:
        return out

    # 4) parse owner from origin URL
    rc, url = _run_capture(["git", "-C", str(REPO_ROOT), "config", "--get", "remote.origin.url"])
    if rc == 0 and url:
        # Examples: https://github.com/owner/repo.git or git@github.com:owner/repo.git
        m = re.search(r"github\.com[/:]([^/\s]+)/", url, re.IGNORECASE)
        if m:
            return m.group(1)

    # 5) OS username
    for key in ("USERNAME", "USER"):
        v = os.environ.get(key)
        if v:
            return v
    return None

def has_implementation(pyfile: Path) -> bool:
    """
    Check if a task file contains actual implementation code.
    Returns False if the file only contains TODO comments, docstrings, or is empty.
    This prevents students from getting credit for deleted/empty solutions.
    """
    if not pyfile.exists():
        return False
    
    try:
        content = pyfile.read_text(encoding="utf-8")
        # Remove docstrings and comments
        lines = content.split('\n')
        code_lines = []
        in_docstring = False
        docstring_char = None
        
        for line in lines:
            stripped = line.strip()
            
            # Track docstring boundaries
            if '"""' in stripped or "'''" in stripped:
                if not in_docstring:
                    # Starting docstring
                    docstring_char = '"""' if '"""' in stripped else "'''"
                    in_docstring = True
                    # Check if docstring closes on same line
                    if stripped.count(docstring_char) >= 2:
                        in_docstring = False
                    continue
                else:
                    # Ending docstring
                    in_docstring = False
                    continue
            
            # Skip lines inside docstrings
            if in_docstring:
                continue
            
            # Skip comments and empty lines
            if not stripped or stripped.startswith('#'):
                continue
            
            # Skip TODO comments
            if 'TODO' in stripped.upper() and '#' in stripped:
                continue
            
            # This is actual code
            code_lines.append(stripped)
        
        # File must have at least one line of actual code (not just imports/pass)
        substantive_code = [line for line in code_lines 
                          if line and line != 'pass' and not line.startswith('import ') and not line.startswith('from ')]
        
        return len(substantive_code) > 0
    except Exception:
        return False

def run_task(pyfile: Path, input_data: str = ""):
    """Run a Python task file, optionally providing input via stdin."""
    try:
        proc = subprocess.run(
            [sys.executable, str(pyfile)],
            cwd=str(pyfile.parent),
            text=True,
            input=input_data,
            capture_output=True,
            timeout=5
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return 124, "", "Timed out (5s)"
    except Exception as e:
        return 1, "", str(e)

def grade_part2():
    state = load_state()
    prev = state.get("parts", {}).get("2", {}).get("tasks", {})
    results = {}
    part_score = 0
    
    # Combine all tasks
    all_tasks = list(EXPECTED.keys()) + list(INTERACTIVE.keys())
    total_tasks = len(all_tasks)

    if total_tasks == 0:
        print("No tasks defined yet for Part 2. Add tasks to EXPECTED or INTERACTIVE dictionaries.")
        # Still write an updated marksheet/points.json with zero totals
        state.setdefault("parts", {})
        state["parts"]["2"] = {"tasks": {}, "score": 0, "total": 0}
        state["total_points"] = sum(p.get("score", 0) for k, p in state["parts"].items() if k != "5")
        save_state(state)
        write_marksheet(state, get_display_user())
        return

    print("Grading Part 2")
    print("-" * 40)

    # Grade non-interactive tasks
    for fname, expected in EXPECTED.items():
        path = ROOT / "tasks" / fname
        
        # Check if file has actual implementation
        if not has_implementation(path):
            results[fname] = False
            print(f"{fname:30}  FAIL (no implementation)")
            continue
        
        code, out, err = run_task(path)
        passed_now = (out == expected)
        passed = (code == 0 and passed_now)

        results[fname] = bool(passed)
        status = "PASS" if passed else "FAIL"
        if passed: part_score += 1
        print(f"{fname:30}  {status}")
        if not passed:
            exp = expected.replace("\n", "\\n")
            got = (out or "").replace("\n", "\\n")
            print(f"  expected: {exp}")
            print(f"  got     : {got}")
            if err:
                print(f"  stderr  : {err.strip()}")

    # Grade interactive tasks
    for fname, test_spec in INTERACTIVE.items():
        path = ROOT / "tasks" / fname
        
        # Check if file has actual implementation
        if not has_implementation(path):
            results[fname] = False
            print(f"{fname:30}  FAIL (no implementation)")
            continue
        
        # Prepare input: join with newlines
        input_str = "\n".join(test_spec["inputs"]) + "\n"
        expected = test_spec["expected_output"]

        code, out, err = run_task(path, input_str)
        passed_now = (out == expected)
        passed = (code == 0 and passed_now)

        results[fname] = bool(passed)
        status = "PASS" if passed else "FAIL"
        if passed: part_score += 1
        print(f"{fname:30}  {status}")
        if not passed:
            exp = expected.replace("\n", "\\n")
            got = (out or "").replace("\n", "\\n")
            print(f"  expected: {exp}")
            print(f"  got     : {got}")
            if err:
                print(f"  stderr  : {err.strip()}")

    state.setdefault("parts", {})
    state["parts"]["2"] = {"tasks": results, "score": part_score, "total": total_tasks}
    # Exclude Part 5 from total aggregation
    state["total_points"] = sum(p.get("score", 0) for k, p in state["parts"].items() if k != "5")
    save_state(state)
    # Write marksheet markdown
    write_marksheet(state, get_display_user())

    print("-" * 40)
    user = get_display_user()
    if user:
        print(f"{user}: your Part 2 score is {part_score}/{total_tasks}")
        print(f"{user}: your total score is {state['total_points']}")
    else:
        print(f"Part 2 score: {part_score}/{total_tasks}")
        print(f"Cumulative score: {state['total_points']}")
    print(f"(Saved to {PROGRESS})")

if __name__ == "__main__":
    grade_part2()
