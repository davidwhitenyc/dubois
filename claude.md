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

## Git Push Limitations

**You (Claude) cannot push to remote repositories.**

Due to SSH authentication limitations, you do not have access to the user's SSH agent and cannot successfully execute `git push` commands.

**When you create a commit:**
1. Create the commit using `git commit`
2. Inform the user that the commit was created successfully
3. Tell the user they need to push manually using `git push`
4. Do NOT attempt to run `git push` yourself - it will fail with an authentication error

This is an intentional security boundary. The user will handle all push operations manually.