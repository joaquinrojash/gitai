\# gitai



AI-powered git commit message and PR description generator.



Reads your `git diff` and generates a conventional commit message in seconds.



\## Install



```bash

pip install gitai

export ANTHROPIC\_API\_KEY="your-key-here"

```



\## Usage



```bash

\# Generate a commit message for staged changes

gitai commit



\# Stage everything and commit in one step  

gitai commit --auto



\# Preview without committing

gitai commit --dry-run



\# Generate a PR description vs main branch

gitai pr



\# PR description vs a different branch

gitai pr --base develop

```



\## Example output



```

╭─── Suggested commit ───╮

│ feat(auth): add OAuth2  │

│ login with Google       │

╰─────────────────────────╯

Use this message? \[y/n]:

```



\## Requirements



\- Python 3.10+

\- An Anthropic API key (get one free at console.anthropic.com)



\## License



MIT

