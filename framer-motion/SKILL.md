# Framer Motion Skill

## What This Skill Does
A complete Framer Motion design-and-code intelligence engine. Search animations, patterns, easing curves, and components — then generate production-ready React code for any interaction or motion system.

## Structure
```
framer-motion/
├── SKILL.md                    ← This file
├── data/
│   ├── animations.csv          ← 30+ animations with variants code and triggers
│   ├── patterns.csv            ← 15 implementation patterns
│   ├── easing.csv              ← 11 easing curves and spring presets
│   └── components.csv          ← Full FM API reference (components + hooks)
├── scripts/
│   ├── search.py               ← BM25 search across all data
│   └── generate.py             ← Code generator for 10 component types
└── references/
    ├── core-concepts.md        ← Mental models, variant system, performance rules
    └── recipes.md              ← 10 copy-paste production recipes
```

## Search Command
```bash
python3 /app/.agents/skills/framer-motion/scripts/search.py "<query>" --domain <domain> [-n <results>]
```

### Domains
- `animations` — entrance, scroll, hover, tap, drag, loading, feedback animations
- `patterns` — AnimatePresence, stagger, layoutId, useScroll, page transitions
- `easing` — curves and spring configs (easeOut, spring, premium ease, etc.)
- `components` — motion.div, AnimatePresence, useScroll, useTransform, all hooks
- `all` — search everything at once

### Examples
```bash
# Find animations for a modal
python3 /app/.agents/skills/framer-motion/scripts/search.py "modal entrance" --domain animations

# Find how to do page transitions
python3 /app/.agents/skills/framer-motion/scripts/search.py "page transition route" --domain patterns

# Find best easing for a button
python3 /app/.agents/skills/framer-motion/scripts/search.py "button hover spring" --domain easing

# Find scroll-related hooks
python3 /app/.agents/skills/framer-motion/scripts/search.py "scroll parallax" --domain components

# Search everything for stagger
python3 /app/.agents/skills/framer-motion/scripts/search.py "stagger list" --domain all
```

## Code Generator
```bash
python3 /app/.agents/skills/framer-motion/scripts/generate.py <component> --stack <stack>
```

### Components
- `hero` — Animated hero with stagger children
- `card` — Product/feature card with hover + scroll reveal
- `modal` — Modal with backdrop and spring entrance
- `navbar` — Sticky nav that hides on scroll down
- `stagger-list` — Scroll-triggered staggered list
- `page-transition` — Route transition wrapper
- `tabs` — Tab switcher with animated layoutId indicator
- `drawer` — Side drawer with AnimatePresence
- `counter` — Animated number counter (scroll-triggered)
- `scroll-progress` — Reading progress bar

### Stacks
`react` | `nextjs` | `tailwind`

### Examples
```bash
python3 /app/.agents/skills/framer-motion/scripts/generate.py hero --stack tailwind
python3 /app/.agents/skills/framer-motion/scripts/generate.py modal --stack nextjs
python3 /app/.agents/skills/framer-motion/scripts/generate.py card --stack tailwind
```

## When to Use This Skill
- Before adding any animation to a UI — search for the right approach first
- When implementing page/route transitions
- When building interactive components (buttons, cards, modals, drawers)
- When implementing scroll-driven effects
- When choosing between spring/tween/inertia
- When generating boilerplate for common patterns

## Key Rules (always apply)
1. **Only animate `transform` and `opacity`** — never animate layout properties (width, height, top, left) directly
2. **Always use `AnimatePresence`** for any element with an `exit` prop
3. **Always add `key` prop** to list items inside AnimatePresence
4. **Always check `useReducedMotion()`** for accessibility
5. **Use `viewport={{ once: true }}`** to prevent re-triggering scroll animations
6. **Spring > Tween** for interactive elements (buttons, cards, menus)
7. **Tween > Spring** for precise, predictable durations (page transitions, loaders)
