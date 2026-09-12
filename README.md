# Frontmatter, then the folder

This is the tree for [Frontmatter, then the folder](https://saintx.dev/posts/frontmatter-scan/) at tag `surf/0002-frontmatter-scan`.

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

Since `surf/0001-traverse-context` nothing landed except this README. `fetch`, `fetch-pstack.sh`, `.gitignore`, and `LICENSE` are the same. The pin is still `889ec4b68fa5aab0e867dad71ec3fdf386ae48f3`.

Next: `surf/0003-what-surf-sees`.

## Experimenting

`git switch -c mine surf/0002-frontmatter-scan` gives you a branch of your own at this post's state.

What a later post added is the three-dot diff between consecutive tags, for example `git diff surf/0002-frontmatter-scan...surf/0003-what-surf-sees`, or https://github.com/saintx/lessons/compare/surf/0002-frontmatter-scan...surf/0003-what-surf-sees.
