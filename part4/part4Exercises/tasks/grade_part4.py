#!/usr/bin/env python3
"""
Part 4 Grader — awards 1 point per correct task and persists progress.
Usage:
    python part4Exercises/grade_part4.py
    (Windows) python part4Exercises\\grade_part4.py
"""
from __future__ import annotations
import json, os, sys, subprocess, time, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # /.../part4Exercises
REPO_ROOT = ROOT.parent                      # part4 folder
WORKSPACE_ROOT = REPO_ROOT.parent            # repository/workspace root
# Use shared workspace-level progress file for all parts
PROGRESS = WORKSPACE_ROOT / ".progress" / "points.json"
PROGRESS_DIR = PROGRESS.parent
MARKSHEET_DIR = WORKSPACE_ROOT / ".progress"

EXPECTED = {
    # Section 4.1 - More functions (non-interactive outputs)
    "4.1.1_line.py": "%%%%%%%\nLLLLLLLLLL\n***\n",
    "4.1.2_a_box_of_hashes.py": "##########\n##########\n##########\n##########\n##########\n",
    "4.1.3_a_square_of_hashes.py": "#####\n#####\n#####\n#####\n#####\n",
    "4.1.4_a_square.py": "*****\n*****\n*****\n*****\n*****\n",
    "4.1.5_a_triangle.py": "#\n##\n###\n####\n#####\n",
    "4.1.6_a_shape.py": "X\nXX\nXXX\nXXXX\nXXXXX\n*****\n*****\n*****\n",
    "4.1.7_a_spruce.py": "  *\n ***\n*****\n  *\n",
    "4.1.8_the_greatest_number.py": "4\n99\n0\n",
    "4.1.9_same_characters.py": "False\nTrue\nFalse\n",
    "4.1.10_first_second_last_words.py": "it\nwas\nnight\nwas\nwas\n",
    # Section 4.2 - Lists (some non-interactive function outputs)
    "4.2.6_length_of_list.py": "5\n",
    "4.2.7_arithmetic_mean.py": "3.0\n",
    "4.2.8_range_of_list.py": "4\n",
    # Section 4.3 - Definite iteration (function outputs)
    "4.3.1_star_studded.py": "P*y*t*h*o*n\na*b*c\n",
    "4.3.2_negative_to_positive.py": "[1, 2, 3, 4, 5]\n",
    "4.3.3_list_of_stars.py": "***\n*******\n*\n*\n**\n",
    "4.3.4_anagrams.py": "True\nTrue\nTrue\nFalse\nFalse\n",
    "4.3.5_palindromes.py": "True\nFalse\n",
    "4.3.6_sum_of_positives.py": "9\n",
    "4.3.7_even_numbers.py": "[2, 4]\n",
    "4.3.8_sum_of_lists.py": "[8, 10, 12]\n",
    "4.3.9_distinct_numbers.py": "[1, 2, 3]\n",
    "4.3.10_length_of_longest.py": "8\n7\n",
    "4.3.11_shortest.py": "first\ntim\n",
    "4.3.12_all_the_longest.py": "['eleventh']\n['dorothy', 'richard']\n",
    # Section 4.4 - Print statement formatting
    "4.4.1_integers_to_strings.py": "['1.23', '0.33', '0.11', '3.45']\n",
    # Section 4.5 - More strings and lists
    "4.5.1_everything_reversed.py": "['erom eno', 'elpmaxe', 'ereht', 'iH']\n",
    "4.5.2_most_common_character.py": "b\ne\n",
    "4.5.3_no_vowels_allowed.py": "ths s n xmpl\n",
    "4.5.4_no_shouting_allowed.py": "['def', 'lower', 'another']\n",
    "4.5.5_neighbours_in_list.py": "4\n",
}
INTERACTIVE = {
    # Section 4.2 - Lists (interactive exercises)
    "4.2.1_change_value.py": {
        "inputs": ["0", "10", "2", "250", "4", "-45", "-1"],
        "expected_output": "Index: New value: [10, 2, 3, 4, 5]\nIndex: New value: [10, 2, 250, 4, 5]\nIndex: New value: [10, 2, 250, 4, -45]\nIndex: "
    },
    "4.2.2_add_items.py": {
        "inputs": ["3", "10", "250", "-45"],
        "expected_output": "How many items: Item 1: Item 2: Item 3: [10, 250, -45]\n"
    },
    "4.2.3_addition_and_removal.py": {
        "inputs": ["a", "a", "a", "r", "a", "v"],
        "expected_output": "The list is now []\na(dd)/r(emove)/e(xit): The list is now [1]\na(dd)/r(emove)/e(xit): The list is now [1, 2]\na(dd)/r(emove)/e(xit): The list is now [1, 2, 3]\na(dd)/r(emove)/e(xit): The list is now [1, 2]\na(dd)/r(emove)/e(xit): The list is now [1, 2, 3]\na(dd)/r(emove)/e(xit): Bye!\n"
    },
    "4.2.4_same_word_twice.py": {
        "inputs": ["once", "upon", "a", "time", "upon"],
        "expected_output": "Word: Word: Word: Word: Word: You typed in 4 different words\n"
    },
    "4.2.5_list_twice.py": {
        "inputs": ["3", "1", "9", "5", "0"],
        "expected_output": "New item: The list now: [3]\nThe list in order: [3]\nNew item: The list now: [3, 1]\nThe list in order: [1, 3]\nNew item: The list now: [3, 1, 9]\nThe list in order: [1, 3, 9]\nNew item: The list now: [3, 1, 9, 5]\nThe list in order: [1, 3, 5, 9]\nNew item: Bye!\n"
    },
    # Section 4.5 - Grade statistics (complex interactive)
    "4.5.6_grade_statistics.py": {
        "inputs": ["15", "21", "28", "31", "35", "38", "42", ""],
        "expected_output": "Exam results: Exam results: Exam results: Exam results: Exam results: Exam results: Exam results: Exam results: Statistics:\nPoints average: 30.0\nPass percentage: 85.7\nGrade distribution:\n  5: ***\n  4: *\n  3: *\n  2: \n  1: **\n  0: *\n"
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

def run_task(pyfile: Path, input_data: str = ""):
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

def grade_part4():
    state = load_state()
    prev = state.get("parts", {}).get("4", {}).get("tasks", {})
    results = {}
    part_score = 0
    all_tasks = list(EXPECTED.keys()) + list(INTERACTIVE.keys())
    total_tasks = len(all_tasks)

    if total_tasks == 0:
        print("No tasks defined yet for Part 4. Add tasks to EXPECTED or INTERACTIVE dictionaries.")
        return

    print("Grading Part 4")
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
    state["parts"]["4"] = {"tasks": results, "score": part_score, "total": total_tasks}
    # Exclude Part 5 from cumulative total
    state["total_points"] = sum(p.get("score", 0) for k, p in state["parts"].items() if k != "5")
    save_state(state)
    write_marksheet(state, get_display_user())

    print("-" * 40)
    user = get_display_user()
    if user:
        print(f"{user}: your Part 4 score is {part_score}/{total_tasks}")
        print(f"{user}: your total score is {state['total_points']}")
    else:
        print(f"Part 4 score: {part_score}/{total_tasks}")
        print(f"Cumulative score: {state['total_points']}")
    print(f"(Saved to {PROGRESS})")

if __name__ == "__main__":
    grade_part4()
