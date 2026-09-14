# Markdown Edge Cases in surf: Structure, Code Blocks, and Backticks

This is the tree for [Markdown Edge Cases in surf: Structure, Code Blocks, and Backticks](https://saintx.dev/posts/markdown-edge-cases-in-surf/) at tag `surf/0003-markdown-edge-cases-in-surf`.

## Fetch

```bash
git clone https://github.com/saintx/lessons.git
cd lessons
git switch surf
./fetch
uv tool install surf-cli==0.8.0
git checkout surf/0003-markdown-edge-cases-in-surf
```

`./fetch` runs the fetch scripts on the branch tip. Lesson state is the tag. Fetch once per machine; `corpus/` is gitignored and stays in place when you check out a tag.

pstack is Lauren Tan's plugin in [cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack), pinned at `889ec4b68fa5aab0e867dad71ec3fdf386ae48f3`, and lands at `corpus/pstack/`. This post does not edit that tree.

```bash
surf corpus/pstack/skills/interrogate/references/reviewer-prompt.md "Output"
surf corpus/pstack/skills/interrogate/references/reviewer-prompt.md --list
surf corpus/pstack/README.md --list
surf corpus/pstack/README.md 'pstack#usage#just use [`/poteto-mode`](./skills/poteto-mode/SKILL.md)'
```

Since `surf/0002-surf-yaml-frontmatter` nothing landed except this README. `fetch`, `fetch-pstack.sh`, `tag-pstack-skills.py`, `.gitignore`, and `LICENSE` are the same. The pin is still `889ec4b68fa5aab0e867dad71ec3fdf386ae48f3`.

## Experimenting

`git switch -c mine surf/0003-markdown-edge-cases-in-surf` gives you a branch of your own at this post's state.
