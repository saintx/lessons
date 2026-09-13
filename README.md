# Surfing YAML Frontmatter

This is the tree for [Surfing YAML Frontmatter](https://saintx.dev/posts/frontmatter-scan/) at tag `surf/0002-frontmatter-scan`.

## Fetch

```bash
git clone https://github.com/saintx/lessons.git
cd lessons
git switch surf
./fetch
uv tool install surf-cli==0.8.0
git checkout surf/0002-frontmatter-scan
```

`./fetch` runs the fetch scripts on the branch tip. Lesson state is the tag. Fetch once per machine; `corpus/` is gitignored and stays in place when you check out a tag.

pstack is Lauren Tan's plugin in [cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack), pinned at `889ec4b68fa5aab0e867dad71ec3fdf386ae48f3`, and lands at `corpus/pstack/`.

```bash
surf -f corpus/pstack/skills/principle-laziness-protocol/SKILL.md
surf -f corpus/pstack/skills/principle-*/SKILL.md
surf corpus/pstack/skills/principle-guard-the-context-window/SKILL.md "Guard the Context Window"
```

`python tag-pstack-skills.py` stamps `metadata.category` onto each fetched skill. The skills themselves are not in the tree; the mapping is. Re-run `./fetch` after `rm -rf corpus/pstack` if you want the untagged copies back.

Since `surf/0001-traverse-context` this tag adds `tag-pstack-skills.py` and this README. `fetch`, `fetch-pstack.sh`, `.gitignore`, and `LICENSE` are the same. The pin is still `889ec4b68fa5aab0e867dad71ec3fdf386ae48f3`.

## Experimenting

`git switch -c mine surf/0002-frontmatter-scan` gives you a branch of your own at this post's state.
