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

## Run with Docker
1. Build the image from project root:
```bash
docker build -t web-summary-openai .
```
2. Run with your API key from `.env`:
```bash
docker run --rm --env-file .env web-summary-openai
```
3. Run against a custom URL and model:
```bash
docker run --rm --env-file .env web-summary-openai "https://cnn.com" --model "gpt-4.1-mini"
```

TODO:
- Upgrade logic to use playwright / selenium for better webscraping web summary
- ~~Migrate logic to .py when using a more production-scale summarizer~~
- ~~Dockerize the function so its production-ready~~
