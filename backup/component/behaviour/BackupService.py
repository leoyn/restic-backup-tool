import os
from backup.component.structure.PlistConfigManager import PlistConfigManager


class BackupService:
    instance = None

    @staticmethod
    def getInstance():
        if BackupService.instance == None:
            BackupService.instance = BackupService()
        return BackupService.instance

    def __init__(self):
        self.plistConfigManager = PlistConfigManager()

    def setup(self, repository, location, password):
        self.plistConfigManager.create(repository, location, password)
