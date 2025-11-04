Which issues were the easiest to fix, and which were the hardest? Why?

Easiest: Line length (E501) and unused import (F401, W0611) issues were the easiest to fix since they only required formatting adjustments or removing redundant imports.

Hardest: The naming convention (C0103) and global variable (W0603) issues were harder to fix because they required changing variable scope and ensuring functionality wasn’t broken.

Did the static analysis tools report any false positives? If so, describe one example.

No major false positives were encountered. However, Pylint flagged a “pointless string statement” (W0105) which was actually a valid placeholder comment in the code. This could be considered a mild false positive since it didn’t affect functionality.

How would you integrate static analysis tools into your actual software development workflow?

Integrate Flake8 and Pylint into a pre-commit hook using tools like pre-commit to automatically check code before each commit.

Run these tools as part of a CI/CD pipeline (e.g., GitHub Actions) to enforce code quality across all contributions.

Use IDE integrations to highlight issues in real time during local development.

What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

Code readability improved significantly due to consistent formatting and removal of unnecessary imports.

The code became more PEP 8 compliant, improving maintainability.

Potential bugs from global variables were reduced, making the system more modular and robust.

The final codebase is cleaner, easier to understand, and better aligned with professional software standards.