import subprocess
import sys
from pathlib import Path

def main():
    try:
        repo_dir = Path(__file__).resolve().parent

        if sys.platform == "win32":
            python = sys.executable

            uv_ok = subprocess.run(
                [python, "-m", "uv", "--version"],
                cwd=str(repo_dir),
                capture_output=True,
                text=True,
            ).returncode == 0

            if not uv_ok:
                subprocess.run(
                    [python, "-m", "pip", "install", "uv"],
                    cwd=str(repo_dir),
                    check=True,
                )

            subprocess.run([python, "-m", "uv", "venv", "--allow-existing"], cwd=str(repo_dir), check=True)
            subprocess.run([python, "-m", "uv", "sync"], cwd=str(repo_dir), check=True)

            venv_python = repo_dir / ".venv" / "Scripts" / "python.exe"
            subprocess.run([str(venv_python), str(repo_dir / "run.py")], cwd=str(repo_dir), check=True)
        else:
            init_script = repo_dir / "init.sh"
            subprocess.run([str(init_script)], cwd=str(repo_dir))
    # Handle Ctrl+C
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()