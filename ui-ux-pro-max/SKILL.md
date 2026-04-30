# UI PRO MAX Skill

## What This Skill Does
Provides AI-powered design intelligence with 161 industry-specific reasoning rules, 67 UI styles, 161 color palettes, 57 font pairings, 25 chart types, and 99 UX guidelines. Use this skill whenever you need to generate, recommend, or reason about UI/UX design systems.

## How to Use

### Search Command
```bash
python3 /app/.agents/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
```

### Domains
- `product` — Industry/product type recommendations (SaaS, e-commerce, portfolio, fintech, etc.)
- `style` — UI styles (glassmorphism, minimalism, brutalism, bento grid, etc.)
- `typography` — Font pairings with Google Fonts imports
- `color` — Color palettes by product type
- `landing` — Landing page structure and CTA strategies
- `chart` — Chart types and library recommendations
- `ux` — Best practices and anti-patterns

### Stack-Specific Guidelines
```bash
python3 /app/.agents/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "<query>" --stack <stack>
```
Stacks: `html-tailwind`, `react`, `nextjs`, `astro`, `vue`, `nuxtjs`, `nuxt-ui`, `svelte`, `shadcn`, `swiftui`, `react-native`, `flutter`, `jetpack-compose`

### Design System Generation
```bash
python3 /app/.agents/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/design_system.py "<product_type>" --stack <stack>
```

## Examples
- Search for SaaS product design: `--domain product` query `"saas"`
- Get glassmorphism style details: `--domain style` query `"glassmorphism"`
- Get fintech color palette: `--domain color` query `"fintech"`
- Get React typography: `--stack react` query `"modern sans-serif"`
- Generate design system: `design_system.py "E-commerce" --stack shadcn`

## When to Use
- Before building any UI — query product type to get the optimal style, colors, fonts
- When asked about design systems, UI components, or visual styling
- When generating landing pages, dashboards, or app interfaces
- When recommending design patterns for a specific industry
