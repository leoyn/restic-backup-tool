import os
from pathlib import Path
import sys


class PlistConfigManager:
    def create(self, repository, location, password):
        plistSourceDirectory = os.path.abspath(os.path.dirname(__file__) + "/../../")
        location = os.path.abspath(os.path.expanduser(location))

        with open(plistSourceDirectory + "/lauchd.orig.plist", "r") as source:
            content = source.read()

            content = content.replace("{password}", password)
            content = content.replace("{repository}", repository)
            content = content.replace("{location}", location)
            content = content.replace("{executable}", sys.argv[0])
            content = content.replace("{home}", str(Path.home()))

            filePath = str(Path.home()) + "/Library/LaunchAgents/automatic-backup.plist"

            with open(filePath, "w+") as destination:
                destination.writelines(content)

            if os.path.exists(filePath):
                os.system(f"launchctl unload -w {filePath}")
            os.system(f"launchctl load -w {filePath}")
