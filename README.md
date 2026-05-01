# Agent 001 — Skills Repository

Custom skills for Agent 001 on Base44. Install any skill by cloning this repo and copying the folder to `.agents/skills/`.

---

## Skills

### 🎨 ui-ux-pro-max
Design intelligence engine. 161 style rules, 67 UI styles, 161 color palettes, 57 font pairings, 25 chart types.

```bash
python3 .agents/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain> -n <results>
```
Domains: `style` `color` `typography` `product` `landing` `chart` `ux`

---

### 🎬 framer-motion
Framer Motion animation intelligence. 30+ animations with variants code, 15 patterns, 11 easing presets, full API reference, 10-component code generator.

```bash
# Search
python3 .agents/skills/framer-motion/scripts/search.py "<query>" --domain <domain> -n <results>

# Generate component code
python3 .agents/skills/framer-motion/scripts/generate.py <component> --stack <stack>
```

**Search domains:** `animations` `patterns` `easing` `components` `all`

**Generator components:** `hero` `card` `modal` `navbar` `stagger-list` `page-transition` `tabs` `drawer` `counter` `scroll-progress`

---

### 🔗 Combined Search (UI PRO MAX + Framer Motion)
Queries both skills simultaneously — returns visual system + motion system in one call.

```bash
python3 .agents/skills/framer-motion/scripts/combined_search.py "<query>" --domain all -n 3
```

**Domains:** `ui` `motion` `all`

Returns: style recommendations → color palette → typography → animations → patterns → synthesis guide.

---

## Install Instructions

```bash
# Clone the repo
git clone https://github.com/ZAFAR9/agent001-skills /tmp/agent001-skills

# Install framer-motion skill
cp -r /tmp/agent001-skills/framer-motion /app/.agents/skills/framer-motion

# Install ui-ux-pro-max skill
cp -r /tmp/agent001-skills/ui-ux-pro-max /app/.agents/skills/ui-ux-pro-max
pip install rank-bm25 -q

# Test combined search
python3 /app/.agents/skills/framer-motion/scripts/combined_search.py "saas dashboard" --domain all -n 2
```

---

*Maintained by Agent 001 — Base44*
