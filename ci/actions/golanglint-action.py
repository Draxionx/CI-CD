from .base import BaseAction
import sys

class GolangLintAction(BaseAction):

    @classmethod
    def name(cls) -> str:
        return "golangci-lint"
    
    @classmethod
    def command(self) -> str:
        return "golangci-lint run"
    
if __name__ == "__main__":
    sys.exit(GolangLintAction().run())