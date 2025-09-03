from abc import ABC, abstractmethod
import subprocess

class BaseAction(ABC):

    @abstractmethod
    def name() -> str:
        """Name of action"""
    
    @abstractmethod
    def command(self) -> str:
        """Command to run action"""

    def run(self) -> int:
        cmd = self.command()
        n = type(self).name()
        print(f"[{n}] Running: {cmd}")
        rc = subprocess.call(cmd, shell=True)
        print(f"[{n}] {'Passed' if rc == 0 else f'Failed with exit code {rc}'}")
        return rc

