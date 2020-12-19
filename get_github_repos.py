import os
import subprocess
import sys
import yaml
from pathlib import Path

TOKEN = os.environ.get("GITHUB_TOKEN")

exclude = {
    "MaartenGr/BERTopic",  # torch
    "MaartenGr/KeyBERT",  # torch
    "phurwicz/hover",  # torch
    "voidful/TFkit",  # torch
}


def get_repos():
    from github import Github

    github = Github(TOKEN)
    search = github.search_code("mkdocstrings+filename:mkdocs.yml")
    return [
        result.repository.full_name
        for result in sorted(search, key=lambda result: result.repository.stargazers_count, reverse=True)
        if result.repository.full_name not in exclude
    ]


if __name__ == "__main__":
    print("\n".join(get_repos()))
