# Framer Motion — Core Concepts Reference

## The Mental Model
Framer Motion works by declaratively describing animation *states*, not keyframes. You define what something looks like in different states (hidden, visible, hover, tap) and FM handles the interpolation.

## The 5 Core Props
```jsx
<motion.div
  initial={{ opacity: 0, y: 20 }}    // Starting state (before mount or before animate)
  animate={{ opacity: 1, y: 0 }}     // Target state
  exit={{ opacity: 0, y: -10 }}      // State when component unmounts (needs AnimatePresence)
  transition={{ duration: 0.4 }}     // How to interpolate between states
  variants={myVariants}              // Reusable named states (alternative to inline objects)
/>
```

## Variants System
Variants let you define states by name and reuse them across component trees. They also enable parent→child orchestration.

```jsx
const variants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0 },
  exit: { opacity: 0, scale: 0.9 }
};

<motion.div variants={variants} initial="hidden" animate="visible" exit="exit" />
```

**Parent orchestration** — define transition on parent, children inherit:
```jsx
const parent = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.1, delayChildren: 0.2 }
  }
};
const child = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0 }
};
```

## AnimatePresence
Required for exit animations. Wrap any conditional render.
```jsx
<AnimatePresence>
  {isOpen && <motion.div exit={{ opacity: 0 }} />}
</AnimatePresence>
```
- `mode="wait"` — waits for exit before entering (page transitions)
- `mode="popLayout"` — shrinks outgoing before removing (list deletions)
- `mode="sync"` — default, overlap allowed

## Gesture Props
```jsx
whileHover={{ scale: 1.05 }}
whileTap={{ scale: 0.96 }}
whileDrag={{ opacity: 0.8 }}
whileFocus={{ outline: '2px solid blue' }}
whileInView={{ opacity: 1 }}        // Triggers when entering viewport
```

## Transition Types
```jsx
// Tween (default) — time-based
transition={{ duration: 0.4, ease: 'easeOut' }}

// Spring — physics-based
transition={{ type: 'spring', stiffness: 300, damping: 20 }}

// Inertia — momentum with friction
transition={{ type: 'inertia', velocity: 200 }}
```

## Layout Animations
Add `layout` prop to animate position/size changes automatically:
```jsx
<motion.div layout />         // Animates all layout changes
<motion.div layout="position" /> // Only position
<motion.div layout="size" />     // Only size
```

For shared element transitions between components/routes:
```jsx
// View A
<motion.div layoutId="product-card-1" />

// View B (different route/component)
<motion.div layoutId="product-card-1" />  // Same ID = FM animates between them
```

## Scroll Animations
```jsx
// Page scroll
const { scrollY, scrollYProgress } = useScroll();

// Element scroll
const ref = useRef();
const { scrollYProgress } = useScroll({ target: ref });

// Map scroll to value
const opacity = useTransform(scrollYProgress, [0, 0.5], [0, 1]);
const y = useTransform(scrollY, [0, 500], [0, -100]);
```

## Performance Rules
1. **Only animate transform and opacity** — these are GPU-accelerated. Never animate width/height/top/left for motion.
2. **Use `will-change: transform`** on elements with heavy animations (use sparingly)
3. **Disable animations on low-power devices** — check `useReducedMotion()`
4. **Don't over-spring** — too many spring animations simultaneously = jank
5. **Use `layout` carefully** — layout animations are expensive on complex DOM trees

## Common Mistakes
- ❌ Forgetting `AnimatePresence` → exit animations silently don't work
- ❌ Missing `key` prop on list items → FM can't detect changes
- ❌ Using `height: 'auto'` in CSS transition → use FM's `layout` instead
- ❌ Animating `margin`/`padding` → use `x`/`y` transforms instead
- ❌ Not setting `mode="wait"` on page transitions → both pages render simultaneously
- ❌ Same `layoutId` on multiple visible elements → chaos
- ❌ Forgetting `viewport={{ once: true }}` → elements re-animate on every scroll
