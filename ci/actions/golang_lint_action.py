from .base import BaseAction
import sys, os

class GolangLintAction(BaseAction):

    @classmethod
    def name(cls) -> str:
        return "golangci-lint"
    
    @classmethod
    def command(self) -> str:
        args = os.getenv("GOLANGCI_ARGS", "")
        return f"golangci-lint run {args}"
    
if __name__ == "__main__":
    sys.exit(GolangLintAction().run())