#!/usr/bin/env python3
"""
Script to export dependencies from pyproject.toml to requirements.txt
Run this script before deploying to platforms that require requirements.txt
"""

import tomli
import sys

def main():
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomli.load(f)
        
        dependencies = data.get("project", {}).get("dependencies", [])
        
        # Strip version requirements
        clean_deps = []
        for dep in dependencies:
            name = dep.split(">=")[0].strip()
            clean_deps.append(name)
        
        with open("requirements.txt", "w") as f:
            f.write("\n".join(clean_deps))
        
        print("Successfully exported dependencies to requirements.txt")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())