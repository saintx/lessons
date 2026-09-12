# Traverse context without ingesting it

This is the tree for [Traverse context without ingesting it](https://saintx.dev/posts/surf-intro/) at tag `surf/0001-traverse-context`.

## Fetch

```bash
git clone https://github.com/saintx/lessons.git
cd lessons
git switch surf
./fetch
uv tool install surf-cli==0.8.0
git checkout surf/0001-traverse-context
```

`./fetch` runs the fetch scripts on the branch tip. Lesson state is the tag. Fetch once per machine; `corpus/` is gitignored and stays in place when you check out a tag.

pstack is Lauren Tan's plugin in [cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack), pinned at `889ec4b68fa5aab0e867dad71ec3fdf386ae48f3`, and lands at `corpus/pstack/`.

```bash
surf corpus/pstack/README.md
surf corpus/pstack/README.md "get started"
```

This is the first tag. Nothing preceded it. The committed files are `README.md`, `fetch`, `fetch-pstack.sh`, `.gitignore`, and `LICENSE`.

Next: `surf/0002-frontmatter-scan`.

## Experimenting

`git switch -c mine surf/0001-traverse-context` gives you a branch of your own at this post's state.

What a later post added is the three-dot diff between consecutive tags, for example `git diff surf/0001-traverse-context...surf/0002-frontmatter-scan`, or https://github.com/saintx/lessons/compare/surf/0001-traverse-context...surf/0002-frontmatter-scan.
