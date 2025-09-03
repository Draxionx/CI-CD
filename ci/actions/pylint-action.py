from .base import BaseAction
import sys, os

class PylintAction(BaseAction):

    @classmethod
    def name(cls) -> str:
        return "pylint"
    
    @classmethod
    def command(self) -> str:
        paths = os.getenv("PY_PATHS", "./src tests")
        args  = os.getenv("PYLINT_ARGS", "")
        return f"pylint {args} {paths}"
    
if __name__ == "__main__":
    sys.exit(PylintAction().run())