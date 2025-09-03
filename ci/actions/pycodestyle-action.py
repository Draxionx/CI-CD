from .base import BaseAction
import sys

class PyCodeStyleAction(BaseAction):

    @classmethod
    def name(cls) -> str:
        return "pycodestyle"
    
    @classmethod
    def command(self) -> str:
        return "pycodestyle --max-line-length=100 ./src tests"
    
if __name__ == "__main__":
    sys.exit(PyCodeStyleAction().run())