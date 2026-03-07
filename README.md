# web-summary-openai

## Quick Summary
This repository contains notebook-based experiments for scraping website content and generating concise AI summaries using the OpenAI API.

## Setup
1. Install `uv` (package/dependency manager).
2. From the project root, install dependencies:
```bash
uv sync
```
3. Create a `.env` file in the project root and add:
```env
OPENAI_API_KEY=your_api_key_here
```
4. Open notebooks in the `main/` folder (for example `web_summary.ipynb`) and run cells top-to-bottom.

## Useful UV Commands
- `uv -h`: Show all available `uv` commands.
- `uv -v`: Show installed `uv` version.
- `uv sync`: Install/update dependencies from `pyproject.toml` and lockfile.

TODO:
- Upgrade logic to use playwright / selenium for better webscraping web summary
- Migrate logic to .py when using a more production-scale summarizer
