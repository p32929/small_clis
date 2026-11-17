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

## You might also like

<a href="https://openstore.pfay.workers.dev/cards/p32929?n=4&amp;repo=small_clis"><picture><source media="(prefers-color-scheme: dark)" srcset="https://openstore.pfay.workers.dev/cards/p32929.svg?n=4&amp;repo=small_clis&amp;theme=dark"><img src="https://openstore.pfay.workers.dev/cards/p32929.svg?n=4&amp;repo=small_clis&amp;theme=light" width="100%" alt="More apps by p32929 on OpenStore"></picture></a>

<p><a href="https://p32929.github.io/share/?repo=small_clis"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-share-dark.svg"><img src="https://p32929.github.io/readme/footer-share-light.svg" width="50%" align="top" alt="Share this project with your friends in one click"></picture></a><a href="https://p32929.github.io/support/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-support-dark.svg"><img src="https://p32929.github.io/readme/footer-support-light.svg" width="50%" align="top" alt="If you like my work and want to support me, feel free to support"></picture></a><br><a href="https://openstore.pfay.workers.dev/add"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-join-dark.svg"><img src="https://p32929.github.io/readme/footer-join-light.svg" width="100%" align="top" alt="Put your own apps on OpenStore: free, your listing lives in your own repo"></picture></a></p>
