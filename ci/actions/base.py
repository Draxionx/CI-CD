from abc import ABC, abstractmethod
import subprocess

class BaseAction(ABC):

    @abstractmethod
    def name() -> str:
        """Name of action"""
    
    @abstractmethod
    def command(self) -> str:
        """Command to run action"""

    def run(self) ->int:
        cmd = self.command()
        print("[{self.name}] Running: {cmd}")
        rc = subprocess.call(cmd, shell=True)
        if rc == 0:
            print("[{self.name}] Passed")
        else:
            print("[{self.name}] Failed with exit code {rc}")
        return rc

