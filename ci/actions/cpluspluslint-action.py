from .base import BaseAction
import sys, os

class CPlusPlusLint(BaseAction):

    @classmethod
    def name(cls) -> str:
        return "clang-tidy"
    
    @classmethod
    def command(self) -> str:
        build = os.getenv("CPP_BUILD_DIR", "build")
        src   = os.getenv("CPP_SRC", "src")
        hdr   = os.getenv("CPP_HEADER_FILTER", f"{src}/.*")
        return f"run-clang-tidy -p {build} -header-filter='{hdr}' {src}/"
    
if __name__ == "__main__":
    sys.exit(CPlusPlusLint().run())