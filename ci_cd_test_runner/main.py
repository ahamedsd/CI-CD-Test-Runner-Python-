import os
import subprocess
import datetime

REPORTS_DIR = "reports"
ASSETS_DIR = "assets"
LATEST_REPORT = os.path.join(REPORTS_DIR, "latest.html")
ARCHIVE_DIR = os.path.join(REPORTS_DIR, "archive")

os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)

# Step 1: Run pytest with HTML report
cmd = [
    "python", "-m", "pytest",
    "tests",
    "--maxfail=0",
    "--disable-warnings",
    f"--html={LATEST_REPORT}",
    "--self-contained-html"
]
result = subprocess.run(cmd, capture_output=True, text=True)

# Step 2: Append cyberpunk theme CSS & chart JS
with open(LATEST_REPORT, "r", encoding="utf-8") as f:
    html_content = f.read()

# Inject CSS
css_link = f'<link rel="stylesheet" href="{ASSETS_DIR}/styles.css">'
html_content = html_content.replace("</head>", f"    {css_link}\n</head>")

# Inject Chart.js and chart JS
chart_js = f"""
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="{ASSETS_DIR}/charts.js"></script>
"""
# Inject a chart container below the summary
chart_div = '<div id="chart-container"><canvas id="results-chart"></canvas></div>'
html_content = html_content.replace('<div class="summary">', f'{chart_div}\n<div class="summary">')
html_content = html_content.replace("</body>", f"{chart_js}\n</body>")

# Save updated report
with open(LATEST_REPORT, "w", encoding="utf-8") as f:
    f.write(html_content)

# Step 3: Archive previous report with timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
archive_path = os.path.join(ARCHIVE_DIR, f"report_{timestamp}.html")
subprocess.run(["copy", LATEST_REPORT, archive_path], shell=True)

print("✅ Latest report generated with cyberpunk theme and chart!")
