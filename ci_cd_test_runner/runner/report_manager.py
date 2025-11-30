from pathlib import Path
import shutil
from datetime import datetime

def archive_report(report_path, archive_dir):
    report_path = Path(report_path)
    if not report_path.exists():
        return None

    archive_dir = Path(archive_dir)
    archive_dir.mkdir(parents=True, exist_ok=True)

    time_tag = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_name = archive_dir / f"report_{time_tag}.html"

    shutil.move(str(report_path), str(new_name))
    return str(new_name)
