from .base import BaseAction
import os, sys

class ShellcheckAction(BaseAction):
    @classmethod
    def name(cls) -> str:
        return "shellcheck"

    def command(self) -> str:
        globs = os.getenv("SH_GLOBS", "**/*.sh")
        args  = os.getenv("SHELLCHECK_ARGS", "-S style -x")

        return (
            "bash -lc '"
            "shopt -s globstar nullglob; "
            f"files=( {globs} ); "
            'if (( ${#files[@]} == 0 )); then echo \"No shell scripts; skipping.\"; exit 0; fi; '
            f"shellcheck {args} \"${{files[@]}}\"'"
        )

if __name__ == '__main__':
    sys.exit(ShellcheckAction().run())