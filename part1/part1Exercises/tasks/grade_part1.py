#!/usr/bin/env python3
"""
Part 1 Grader — awards 1 point per correct task and persists progress.
Usage:
    python part1Exercises/grade_part1.py
    (Windows) python part1Exercises\\grade_part1.py
"""
from __future__ import annotations
import json, os, sys, subprocess, time, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # /.../part1Exercises
REPO_ROOT = ROOT.parent                      # part1 folder
WORKSPACE_ROOT = REPO_ROOT.parent            # repository/workspace root
# Use shared workspace-level progress file for all parts
PROGRESS = WORKSPACE_ROOT / ".progress" / "points.json"
PROGRESS_DIR = PROGRESS.parent
MARKSHEET_DIR = WORKSPACE_ROOT / ".progress"

# For non-interactive tasks: key is filename, value is expected output string
EXPECTED = {
    "1_emoticon.py": ":-)\n",
    "2_seven_brothers.py": "Aapo\nEero\nJuhani\nLauri\nSimeoni\nTimo\nTuomas\n",
    "3_row_your_boat.py": "Row, row, row your boat,\nGently down the stream.\nMerrily, merrily, merrily, merrily,\nLife is but a dream.\n",
    "4_minutes_in_year.py": "525600\n",
    "5_print_some_code.py": "print(\"Hello there!\")\n",
    "11_extraspace.py": "my name is Tim Tester, I am 20 years old\n\nmy skills are\n - python (beginner)\n - java (veteran)\n - programming (semiprofessional)\n\nI am looking for a job with a salary of 2000-3000 euros per month\n",
    "12_arithmetics.py": "27 + 15 = 42\n27 - 15 = 12\n27 * 15 = 405\n27 / 15 = 1.8\n",
    "13_fix_single_line.py": "5 + 8 - 4 = 9\n",
}

# For interactive tasks: key is filename, value is dict with "inputs" (list) and "expected_output" (string)
INTERACTIVE = {
    "6_name_twice.py": {
        "inputs": ["Paul"],
        "expected_output": "What is your name? Paul\nPaul\n"
    },
    "7_name_excalaimation_mark.py": {
        "inputs": ["Paul"],
        "expected_output": "What is your name? !Paul!Paul!\n"
    },
    "8_name_Address.py": {
        "inputs": ["Steve", "Sanders", "91 Station Road", "London EC05 6AW"],
        "expected_output": "Given name: Family name: Street address: City and postal code: Steve Sanders\n91 Station Road\nLondon EC05 6AW\n"
    },
    "9_fix_the_code.py": {
        "inputs": ["hickory", "dickory", "dock"],
        "expected_output": "The 1st part: The 2nd part: The 3rd part: hickory-dickory-dock!\n"
    },
    "10_story.py": {
        "inputs": ["Mary", "1572"],
        "expected_output": "Please type in a name: Please type in a year: Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.\n"
    },
    # Section 1.2 - Arithmetic operations
    "14_times_five.py": {
        "inputs": ["3"],
        "expected_output": "Please type in a number: 3 times 5 is 15\n"
    },
    "15_name_and_age.py": {
        "inputs": ["Frances Fictitious", "1990"],
        "expected_output": "What is your name? Which year were you born? Hi Frances Fictitious, you will be 35 years old at the end of the year 2025\n"
    },
    "16_seconds_in_a_day.py": {
        "inputs": ["1"],
        "expected_output": "How many days? Seconds in that many days: 86400\n"
    },
    "17_fix_the_code_product.py": {
        "inputs": ["2", "4", "5"],
        "expected_output": "Please type in the first number: Please type in the second number: Please type in the third number: The product is 40\n"
    },
    "18_sum_and_product.py": {
        "inputs": ["3", "7"],
        "expected_output": "Number 1: Number 2: The sum of the numbers: 10\nThe product of the numbers: 21\n"
    },
    "19_sum_and_mean.py": {
        "inputs": ["2", "1", "6", "7"],
        "expected_output": "Number 1: Number 2: Number 3: Number 4: The sum of the numbers is 16 and the mean is 4.0\n"
    },
    "20_food_expenditure.py": {
        "inputs": ["4", "2.50", "28.5"],
        "expected_output": "How many times a week do you eat at the student cafeteria? The price of a typical student lunch? How much money do you spend on groceries in a week? \nAverage food expenditure:\nDaily: 5.5 euros\nWeekly: 38.5 euros\n"
    },
    "21_students_in_groups.py": {
        "inputs": ["8", "4"],
        "expected_output": "How many students on the course? Desired group size? Number of groups formed: 2\n"
    },
    # Section 1.3 - Conditional statements
    "22_orwell.py": {
        "inputs": ["1984"],
        "expected_output": "Please type in a number: Orwell\n"
    },
    "23_absolute_value.py": {
        "inputs": ["-7"],
        "expected_output": "Please type in a number: The absolute value of this number is 7\n"
    },
    "24_soup_or_no_soup.py": {
        "inputs": ["Kramer", "2"],
        "expected_output": "Please tell me your name: How many portions of soup? The total cost is 11.8\nNext please!\n"
    },
    "25_order_of_magnitude.py": {
        "inputs": ["59"],
        "expected_output": "Please type in a number: This number is smaller than 1000\nThis number is smaller than 100\nThank you!\n"
    },
    "26_calculator.py": {
        "inputs": ["10", "17", "add"],
        "expected_output": "Number 1: Number 2: Operation: 10 + 17 = 27\n"
    },
    "27_temperatures.py": {
        "inputs": ["21"],
        "expected_output": "Please type in a temperature (F): 21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius\nBrr! It's cold in here!\n"
    },
    "28_daily_wages.py": {
        "inputs": ["8.5", "3", "Monday"],
        "expected_output": "Hourly wage: Hours worked: Day of the week: Daily wages: 25.5 euros\n"
    },
    "29_loyalty_bonus.py": {
        "inputs": ["55"],
        "expected_output": "How many points are on your card? Your bonus is 10 %\nYou now have 60.5 points\n"
    },
    "30_what_to_wear_tomorrow.py": {
        "inputs": ["11", "no"],
        "expected_output": "What is the weather forecast for tomorrow?\nTemperature: Will it rain (yes/no): Wear jeans and a T-shirt\nI recommend a jumper as well\n"
    },
    "31_solving_a_quadratic_equation.py": {
        "inputs": ["1", "2", "-8"],
        "expected_output": "Value of a: Value of b: Value of c: The roots are 2.0 and -4.0\n"
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

def grade_part1():
    state = load_state()
    prev = state.get("parts", {}).get("1", {}).get("tasks", {})
    results = {}
    part_score = 0
    
    # Combine all tasks
    all_tasks = list(EXPECTED.keys()) + list(INTERACTIVE.keys())
    total_tasks = len(all_tasks)

    print("Grading Part 1 — Getting Started")
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
    state["parts"]["1"] = {"tasks": results, "score": part_score, "total": total_tasks}
    # Exclude Part 5 from total points aggregation
    state["total_points"] = sum(p.get("score", 0) for k, p in state["parts"].items() if k != "5")
    save_state(state)
    # Write marksheet markdown
    write_marksheet(state, get_display_user())

    print("-" * 40)
    user = get_display_user()
    if user:
        print(f"{user}: your Part 1 score is {part_score}/{total_tasks}")
        print(f"{user}: your total score is {state['total_points']}")
    else:
        print(f"Part 1 score: {part_score}/{total_tasks}")
        print(f"Cumulative score: {state['total_points']}")
    print(f"(Saved to {PROGRESS})")

if __name__ == "__main__":
    grade_part1()
