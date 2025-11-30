import subprocess
import sys
from pathlib import Path

def execute_pytest(tests, reports_dir, report_name, pytest_opts, logger):
    Path(reports_dir).mkdir(parents=True, exist_ok=True)
    report_file = str(Path(reports_dir) / report_name)

    cmd = [
        sys.executable, "-m", "pytest",
        *tests,
        *pytest_opts,
        "--html", report_file,
        "--self-contained-html"
    ]

    logger.info("Executing: %s", " ".join(cmd))

    result = subprocess.run(cmd, text=True, capture_output=True)

    logger.debug("stdout:\n%s", result.stdout)
    logger.debug("stderr:\n%s", result.stderr)
    logger.info("Exit code: %s", result.returncode)

    return result.returncode, report_file
