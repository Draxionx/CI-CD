from .base import BaseAction
import sys, os

class PyCodeStyleAction(BaseAction):

    @classmethod
    def name(cls) -> str:
        return "pycodestyle"
    
    @classmethod
    def command(self) -> str:
        paths = os.getenv("PY_PATHS", "./src tests")
        args  = os.getenv("PYCODESTYLE_ARGS", "--max-line-length=100")
        return f"pycodestyle {args} {paths}"
    
if __name__ == "__main__":
    sys.exit(PyCodeStyleAction().run())