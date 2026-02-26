#!/usr/bin/env python3
"""
Part 5 Grader — awards 1 point per correct task and persists progress.
Usage:
    python part5Exercises/grade_part5.py
    (Windows) python part5Exercises\\grade_part5.py
"""
from __future__ import annotations
import json, os, sys, subprocess, time, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # /.../part5Exercises
REPO_ROOT = ROOT.parent                      # part5 folder
WORKSPACE_ROOT = REPO_ROOT.parent            # repository/workspace root
# Use shared workspace-level progress file for all parts
PROGRESS = WORKSPACE_ROOT / ".progress" / "points.json"
PROGRESS_DIR = PROGRESS.parent
MARKSHEET_DIR = WORKSPACE_ROOT / ".progress"

EXPECTED = {
    # Section 5.1 - More lists (function outputs)
    "1_the_longest_string.py": "eleventh\ndorothy\n",
    "2_number_of_matching_elements.py": "3\n",
    "3_go.py": "1\n",
    "4_sudoku_check_row.py": "True\nFalse\n",
    "5_sudoku_check_column.py": "False\nTrue\n",
    "6_sudoku_check_block.py": "False\nTrue\n",
    "7_sudoku_check_grid.py": "False\nTrue\n",
    # Section 5.2 - References (function outputs)
    "8_items_multiplied_by_two.py": "[4, 8, 10, 6, 22]\n",
    "9_remove_the_smallest.py": "[2, 4, 6, 3, 5]\n",
    "12_tic_tac_toe.py": "True\n[['', '', ''], ['', '', ''], ['X', '', '']]\nFalse\n[['', '', ''], ['', '', ''], ['X', '', '']]\n",
    "13_transpose_matrix.py": "[[1, 4, 7], [2, 5, 8], [3, 6, 9]]\n",
    # Section 5.3 - Dictionary (function outputs)
    "14_times_ten.py": "{3: 30, 4: 40, 5: 50, 6: 60}\n",
    "15_factorials.py": "1\n6\n120\n",
    "16_histogram.py": "a **\nb **\ns **\nt ***\na **\ni **\nc *\nl **\ny *\n",
    "19_invert_dictionary.py": "{'first': 1, 'second': 2, 'third': 3, 'fourth': 4}\n",
    "20_numbers_spelled_out.py": "two\neleven\nforty-five\nninety-nine\nzero\n",
    "21_movie_database.py": "[{'name': 'Gone with the Python', 'director': 'Victor Virus', 'year': 2017, 'runtime': 116}, {'name': 'Pythons on a Plane', 'director': 'Renny Harlin', 'year': 2001, 'runtime': 94}]\n",
    "22_find_movies.py": "[{'name': 'Gone with the Python', 'director': 'Victor Virus', 'year': 2017, 'runtime': 116}, {'name': 'Pythons on a Plane', 'director': 'Renny Harlin', 'year': 2001, 'runtime': 94}]\n",
    # Section 5.4 - Tuple (function outputs)
    "23_create_tuple.py": "(7, -1, 5)\n",
    "24_the_oldest_person.py": "Mary\n",
    "25_older_people.py": "['Adam', 'Mary']\n",
    "26_student_database.py": "Peter:\n 0 completed courses\n average grade 0.0\nPeter:\n 2 completed courses\n average grade 2.5\nEliza:\n 0 completed courses\n average grade 0.0\n",
    "27_square_of_letters.py": "AAA\nABA\nAAA\nAAAAA\nABBBA\nABCBA\nABBBA\nAAAAA\n",
}
INTERACTIVE = {
    # Section 5.3 - Dictionary (interactive programs)
    "17_phone_book_v1.py": {
        "inputs": ["2", "peter", "040-5466745", "2", "emily", "045-1212344", "1", "peter", "1", "mary", "3"],
        "expected_output": "command (1 search, 2 add, 3 quit): name: number: ok!\ncommand (1 search, 2 add, 3 quit): name: number: ok!\ncommand (1 search, 2 add, 3 quit): name: 040-5466745\ncommand (1 search, 2 add, 3 quit): name: no number\ncommand (1 search, 2 add, 3 quit): quitting...\n"
    },
    "18_phone_book_v2.py": {
        "inputs": ["2", "peter", "040-5466745", "2", "peter", "09-111333", "1", "peter", "1", "mary", "3"],
        "expected_output": "command (1 search, 2 add, 3 quit): name: number: ok!\ncommand (1 search, 2 add, 3 quit): name: number: ok!\ncommand (1 search, 2 add, 3 quit): name: 040-5466745\n09-111333\ncommand (1 search, 2 add, 3 quit): name: no number\ncommand (1 search, 2 add, 3 quit): quitting...\n"
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

def grade_part5():
    state = load_state()
    prev = state.get("parts", {}).get("5", {}).get("tasks", {})
    results = {}
    part_score = 0
    all_tasks = list(EXPECTED.keys()) + list(INTERACTIVE.keys())
    total_tasks = len(all_tasks)

    if total_tasks == 0:
        print("No tasks defined yet for Part 5. Add tasks to EXPECTED or INTERACTIVE dictionaries.")
        return

    print("Grading Part 5")
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
    state["parts"]["5"] = {"tasks": results, "score": part_score, "total": total_tasks}
    # Exclude Part 5 from cumulative total (this part remains visible but not counted)
    state["total_points"] = sum(p.get("score", 0) for k, p in state["parts"].items() if k != "5")
    save_state(state)
    write_marksheet(state, get_display_user())

    print("-" * 40)
    user = get_display_user()
    if user:
        print(f"{user}: your Part 5 score is {part_score}/{total_tasks}")
        print(f"{user}: your total score is {state['total_points']}")
    else:
        print(f"Part 5 score: {part_score}/{total_tasks}")
        print(f"Cumulative score: {state['total_points']}")
    print(f"(Saved to {PROGRESS})")

if __name__ == "__main__":
    grade_part5()
