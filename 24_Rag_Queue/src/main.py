from pathlib import Path

from dotenv import load_dotenv # type: ignore[reportMissingImports]
import uvicorn # type: ignore[reportMissingImports]

# Load configuration before importing the application. The worker creates its
# API client during import and needs GOOGLE_API_KEY to be available first.
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

if __package__:
    from .server import app
else:
    import sys
    from pathlib import Path

    src_dir = Path(__file__).resolve().parent
    sys.path = [
        path for path in sys.path
        if Path(path or Path.cwd()).resolve() != src_dir
    ]
    sys.path.insert(0, str(src_dir.parent))
    from src.server import app

# this is the entry point for the FastAPI server. It runs the server on host
def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()