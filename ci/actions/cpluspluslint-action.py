from .base import BaseAction
import sys

class CPlusPlusLint(BaseAction):

    @classmethod
    def name(cls) -> str:
        return "clang-tidy"
    
    @classmethod
    def command(self) -> str:
        return "run-clang-tidy -p build -header-filter='src/.*' src/"
    
if __name__ == "__main__":
    sys.exit(CPlusPlusLint().run())