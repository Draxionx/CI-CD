from .base import BaseAction
import sys

class PylintAction(BaseAction):

    @classmethod
    def name(cls) -> str:
        return "pylint"
    
    @classmethod
    def command(self) -> str:
        return "pylint ./src tests"
    
if __name__ == "__main__":
    sys.exit(PylintAction().run())