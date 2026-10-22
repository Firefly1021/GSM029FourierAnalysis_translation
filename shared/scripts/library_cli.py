"""Portable launcher: python shared/scripts/library_cli.py <mathbook command>."""
import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from mathbook.cli import main

if __name__=='__main__':
    raise SystemExit(main())
