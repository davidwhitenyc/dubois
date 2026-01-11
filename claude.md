# Git Commit Attribution Policy

## Who Creates Commits

**The user commits their own code directly using git.**

Do NOT offer to create commits for code the user wrote themselves. The user will use git commands directly for their own work.

**Only create commits when you (Claude) have actually written or significantly modified the code being committed.**

## Co-Authorship Attribution

**Every time you are asked to create a commit, you MUST explicitly ask:**
"Should I include co-authorship attribution in this commit?"

Do NOT assume the answer. Do NOT automatically add the `Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>` trailer without explicit confirmation from the user.

The user will decide on a case-by-case basis whether AI co-authorship should be included in the commit message.

**This policy remains in effect unless and until the user explicitly changes it.**