"""Lightweight DB bootstrap helper (optional helper script).
This file is not used by FastAPI directly but can be run to initialize DB.
"""

from . import get_connection, init_db


def bootstrap():
    init_db()


if __name__ == "__main__":
    bootstrap()
