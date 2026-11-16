# small_clis

A collection of small personal command-line tools. Each lives in its own folder with its own README — this page is just the index.

## The tools

| Tool | Platform | What it does |
|---|---|---|
| [**get-files**](get-files/) | Python (cross-platform) | Walks a directory and dumps every file's contents into one `output.txt`, each wrapped in a code block — handy for pasting a whole project into an LLM |
| [**killport**](killport/) | Windows (`.bat`) | Kills whatever process is holding a port, e.g. `killport 3000` — for when a dev server won't let go. Each tool's README also lists the Linux/macOS one-liner equivalents |

## Quick start

**get-files** — run it in any directory, answer whether to recurse, and read `output.txt`:

```bash
python get-files/get-files.py
```

**killport** — pass the port to free (Windows):

```cmd
killport\killport.bat 3000
```

See each tool's folder README for install-to-PATH steps and platform notes.

## Contributing

Contributions are very welcome, thank you! Before you start on a pull request, please open an issue and tell me what you would like to add or change. That way we can agree on it first, and your time is not wasted on something that might not fit. Thanks for helping make small_clis better.

## Share

<a href="https://p32929.github.io/share/?repo=small_clis"><img src="https://p32929.github.io/readme/share.svg" alt="Share this with your friends in just a click" width="420"></a>

## Support

<a href="https://p32929.github.io/support/"><img src="https://p32929.github.io/readme/support.svg" alt="If you like my works and want to support me, feel free to support" width="420"></a>
