# Restic Backup Automation Tool

Only support Mac OS at the moment.

## Installation

Prerequisites:
- Python 3.5+
- Mac OS

---
1. Install using pip:
```bash
pip3 install git+https://github.com/leoyn/restic-backup-tool
```
---
2. Allow file access (when using user dir):
   1. Open folder of restic binary:
   ```bash
   cd $(dirname $(which restic)) && cd $(dirname $(readlink $(which restic))) && open "$(pwd)"
   ```
   1. Open Settings: `Security & Privacy` → `Privacy` → `Full Disk Access`
   2. Drag and drop `restic` binary into `Full Disk Access` list
---
3. Setup automatic backup
```bash
backup setup --repository=rclone:whatever:backups/desktop/Documents --location=/Users/username/Documents
Password: 🔑
```
---
Log files can be found in: `~/Library/Logs/backup.stdout.log` and `~/Library/Logs/backup.stderr.log`