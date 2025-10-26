#!/usr/bin/env python3
"""
Part 3 Grader — awards 1 point per correct task and persists progress.
Usage:
    python part3Exercises/grade_part3.py
    (Windows) python part3Exercises\\grade_part3.py
"""
from __future__ import annotations
import json, os, sys, subprocess, time, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # /.../part3Exercises
REPO_ROOT = ROOT.parent                      # part3 folder
WORKSPACE_ROOT = REPO_ROOT.parent            # repository/workspace root
# Use shared workspace-level progress file for all parts
PROGRESS = WORKSPACE_ROOT / ".progress" / "points.json"
PROGRESS_DIR = PROGRESS.parent
MARKSHEET_DIR = WORKSPACE_ROOT / ".progress"

# For non-interactive tasks: key is filename, value is expected output string
EXPECTED = {
    # Section 3.1 - Loops with conditions (non-interactive)
    "3.1.1_print_numbers.py": "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n22\n24\n26\n28\n30\n",
}

# For interactive tasks: key is filename, value is dict with "inputs" (list) and "expected_output" (string)
INTERACTIVE = {
    # Section 3.1 - Loops with conditions
    "3.1.2_fix_the_code_countdown.py": {
        "inputs": ["5"],
        "expected_output": "Are you ready?\nPlease type in a number: 5\n4\n3\n2\n1\nNow!\n"
    },
    "3.1.3_numbers.py": {
        "inputs": ["5"],
        "expected_output": "Please type in a number: 1\n2\n3\n4\n5\n"
    },
    "3.1.4_powers_of_two.py": {
        "inputs": ["8"],
        "expected_output": "Upper limit: 1\n2\n4\n8\n"
    },
    "3.1.5_powers_of_base_n.py": {
        "inputs": ["27", "3"],
        "expected_output": "Upper limit: Base: 1\n3\n9\n27\n"
    },
    "3.1.6_sum_of_consecutive_numbers_v1.py": {
        "inputs": ["2"],
        "expected_output": "Limit: 3\n"
    },
    "3.1.7_sum_of_consecutive_numbers_v2.py": {
        "inputs": ["2"],
        "expected_output": "Limit: The consecutive sum: 1 + 2 = 3\n"
    },
    
    # Section 3.2 - Working with strings
    "3.2.1_string_multiplied.py": {
        "inputs": ["hiya", "4"],
        "expected_output": "Please type in a string: Please type in an amount: hiyahiyahiyahiya\n"
    },
    "3.2.2_the_longer_string.py": {
        "inputs": ["hey", "hiya"],
        "expected_output": "Please type in string 1: Please type in string 2: hiya is longer\n"
    },
    "3.2.3_end_to_beginning.py": {
        "inputs": ["hiya"],
        "expected_output": "Please type in a string: a\ny\ni\nh\n"
    },
    "3.2.4_second_and_second_to_last.py": {
        "inputs": ["pascal"],
        "expected_output": "Please type in a string: The second and the second to last characters are a\n"
    },
    "3.2.5_a_line_of_hashes.py": {
        "inputs": ["3"],
        "expected_output": "Width: ###\n"
    },
    "3.2.6_a_rectangle_of_hashes.py": {
        "inputs": ["10", "3"],
        "expected_output": "Width: Height: ##########\n##########\n##########\n"
    },
    "3.2.7_underlining.py": {
        "inputs": ["Hi there!", "This is a test", "a", ""],
        "expected_output": "Please type in a string: Hi there!\n---------\n\nPlease type in a string: This is a test\n--------------\n\nPlease type in a string: a\n-\n\nPlease type in a string: "
    },
    "3.2.8_right_aligned.py": {
        "inputs": ["python"],
        "expected_output": "Please type in a string: **************python\n"
    },
    "3.2.9_a_framed_word.py": {
        "inputs": ["testing"],
        "expected_output": "Word: ******************************\n*          testing           *\n******************************\n"
    },
    "3.2.10_substrings_part1.py": {
        "inputs": ["test"],
        "expected_output": "Please type in a string: t\nte\ntes\ntest\n"
    },
    "3.2.11_substrings_part2.py": {
        "inputs": ["test"],
        "expected_output": "Please type in a string: t\nst\nest\ntest\n"
    },
    "3.2.12_does_it_contain_vowels.py": {
        "inputs": ["hello there"],
        "expected_output": "Please type in a string: a not found\ne found\no found\n"
    },
    "3.2.13_find_the_first_substring.py": {
        "inputs": ["mammoth", "m"],
        "expected_output": "Please type in a word: Please type in a character: mam\n"
    },
    "3.2.14_find_all_substrings.py": {
        "inputs": ["mammoth", "m"],
        "expected_output": "Please type in a word: Please type in a character: mam\nmmo\nmot\n"
    },
    "3.2.15_the_second_occurrence.py": {
        "inputs": ["abcabc", "ab"],
        "expected_output": "Please type in a string: Please type in a substring: The second occurrence of the substring is at index 3.\n"
    },
    
    # Section 3.3 - More loops
    "3.3.1_multiplication.py": {
        "inputs": ["2", "3"],
        "expected_output": "Please type in a number: Please type in another number: 1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n"
    },
    "3.3.2_first_letters_of_words.py": {
        "inputs": ["Humpty Dumpty sat on a wall"],
        "expected_output": "Please type in a sentence: H\nD\ns\no\na\nw\n"
    },
    "3.3.3_factorial.py": {
        "inputs": ["5"],
        "expected_output": "Please type in a number: The factorial of the number 5 is 120\n"
    },
    "3.3.4_flip_the_pairs.py": {
        "inputs": ["tasks"],
        "expected_output": "Please type in a string: astsk\n"
    },
    "3.3.5_taking_turns.py": {
        "inputs": ["hiya", "hi"],
        "expected_output": "Please type in string 1: Please type in string 2: hhiyia\n"
    },
    
    # Section 3.4 - Defining functions
    "3.4.1_seven_brothers.py": {
        "inputs": [],
        "expected_output": "['Aapo', 'Eero', 'Juhani', 'Lauri', 'Simeoni', 'Timo', 'Tuomas']\n",
        "test_code": "print(seven_brothers())"
    },
    "3.4.2_the_first_character.py": {
        "inputs": [],
        "expected_output": "p\ny\n",
        "test_code": "print(first_character('python'))\nprint(first_character('yellow'))"
    },
    "3.4.3_mean.py": {
        "inputs": [],
        "expected_output": "3.0\n4.0\n",
        "test_code": "print(mean(5, 3, 1))\nprint(mean(10, 1, 1))"
    },
    "3.4.4_print_many_times.py": {
        "inputs": [],
        "expected_output": "python\npython\npython\n",
        "test_code": "print_many_times('python', 3)"
    },
    "3.4.5_a_square_of_hashes.py": {
        "inputs": [],
        "expected_output": "###\n###\n###\n",
        "test_code": "hash_square(3)"
    },
    "3.4.6_chessboard.py": {
        "inputs": [],
        "expected_output": "101\n010\n101\n",
        "test_code": "chessboard(3)"
    },
    "3.4.7_a_word_squared.py": {
        "inputs": [],
        "expected_output": "ab\nba\n",
        "test_code": "squared('ab')"
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
    lines.append("| Part | Score | Max | Percent | Progress |")
    lines.append("|------|-------|-----|---------|----------|")
    parts = state.get("parts", {})
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
    try:
        proc = subprocess.run(args, cwd=str(cwd) if cwd else None, text=True, capture_output=True, timeout=timeout)
        return proc.returncode, proc.stdout.strip()
    except Exception:
        return 1, ""

def get_display_user() -> str | None:
    for key in ("GITHUB_USER", "GITHUB_USERNAME", "GH_USER"):
        v = os.environ.get(key)
        if v:
            return v.strip()
    if shutil.which("gh"):
        rc, out = _run_capture(["gh", "api", "user", "--jq", ".login"])
        if rc == 0 and out:
            return out
    rc, out = _run_capture(["git", "-C", str(REPO_ROOT), "config", "--get", "user.name"])
    if rc == 0 and out:
        return out
    rc, url = _run_capture(["git", "-C", str(REPO_ROOT), "config", "--get", "remote.origin.url"])
    if rc == 0 and url:
        m = re.search(r"github\.com[/:]([^/\s]+)/", url, re.IGNORECASE)
        if m:
            return m.group(1)
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

def run_task(pyfile: Path, input_data: str = "", test_code: str | None = None):
    try:
        if test_code:
            # For function-based tasks, use importlib to handle numeric filenames
            test_script = f"""
import sys
import importlib.util
sys.path.insert(0, r'{pyfile.parent}')

# Load module using importlib
spec = importlib.util.spec_from_file_location('test_module', r'{pyfile}')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Import all from module into globals
for name in dir(module):
    if not name.startswith('_'):
        globals()[name] = getattr(module, name)

{test_code}
"""
            proc = subprocess.run(
                [sys.executable, "-c", test_script],
                cwd=str(pyfile.parent),
                text=True,
                capture_output=True,
                timeout=5
            )
        else:
            # Regular interactive task
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

def grade_part3():
    state = load_state()
    prev = state.get("parts", {}).get("3", {}).get("tasks", {})
    results = {}
    part_score = 0
    all_tasks = list(EXPECTED.keys()) + list(INTERACTIVE.keys())
    total_tasks = len(all_tasks)

    if total_tasks == 0:
        print("No tasks defined yet for Part 3. Add tasks to EXPECTED or INTERACTIVE dictionaries.")
        return

    print("Grading Part 3")
    print("-" * 40)

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

    for fname, test_spec in INTERACTIVE.items():
        path = ROOT / "tasks" / fname
        
        # Check if file has actual implementation
        if not has_implementation(path):
            results[fname] = False
            print(f"{fname:30}  FAIL (no implementation)")
            continue
        
        input_str = "\n".join(test_spec["inputs"]) + "\n"
        expected = test_spec["expected_output"]
        test_code = test_spec.get("test_code")
        code, out, err = run_task(path, input_str, test_code)
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
    state["parts"]["3"] = {"tasks": results, "score": part_score, "total": total_tasks}
    # Exclude Part 5 from cumulative total
    state["total_points"] = sum(p.get("score", 0) for k, p in state["parts"].items() if k != "5")
    save_state(state)
    write_marksheet(state, get_display_user())

    print("-" * 40)
    user = get_display_user()
    if user:
        print(f"{user}: your Part 3 score is {part_score}/{total_tasks}")
        print(f"{user}: your total score is {state['total_points']}")
    else:
        print(f"Part 3 score: {part_score}/{total_tasks}")
        print(f"Cumulative score: {state['total_points']}")
    print(f"(Saved to {PROGRESS})")

if __name__ == "__main__":
    grade_part3()
