import os
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

# Ensure the project root is on path so imports like src.* work in Vercel env
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import app as flask_app  # noqa: E402

# Vercel entrypoint exposes the WSGI app as 'app'
app = flask_app

if __name__ == "__main__":
    run_simple("0.0.0.0", int(os.getenv("PORT", 3000)), app)


