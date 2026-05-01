# Framer Motion — Production Recipes

## Recipe 1: Hero Section with Stagger
```jsx
const container = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.12, delayChildren: 0.2 } }
};
const item = {
  hidden: { opacity: 0, y: 32 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.6, ease: [0.22, 1, 0.36, 1] } }
};

<motion.div variants={container} initial="hidden" animate="visible">
  <motion.h1 variants={item}>Headline</motion.h1>
  <motion.p variants={item}>Subtext</motion.p>
  <motion.button variants={item}>CTA</motion.button>
</motion.div>
```

## Recipe 2: Premium Button
```jsx
<motion.button
  whileHover={{ scale: 1.04, y: -2, boxShadow: '0 8px 24px rgba(0,0,0,0.2)' }}
  whileTap={{ scale: 0.97 }}
  transition={{ type: 'spring', stiffness: 400, damping: 20 }}
>
  Click Me
</motion.button>
```

## Recipe 3: Product Card Grid (Stagger + Scroll)
```jsx
const grid = { hidden: {}, visible: { transition: { staggerChildren: 0.07 } } };
const card = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: [0.22, 1, 0.36, 1] } }
};

<motion.div className="grid" variants={grid} initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.1 }}>
  {products.map(p => (
    <motion.div key={p.id} variants={card} whileHover={{ y: -6 }} className="card">
      {/* card content */}
    </motion.div>
  ))}
</motion.div>
```

## Recipe 4: Tab Switcher with layoutId indicator
```jsx
const [active, setActive] = useState('Tab 1');

<LayoutGroup>
  <div className="tabs">
    {tabs.map(tab => (
      <button key={tab} onClick={() => setActive(tab)} style={{ position: 'relative' }}>
        {tab}
        {active === tab && (
          <motion.div
            layoutId="indicator"
            style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: 2, background: 'var(--primary)' }}
            transition={{ type: 'spring', stiffness: 500, damping: 35 }}
          />
        )}
      </button>
    ))}
  </div>
</LayoutGroup>
```

## Recipe 5: Notification/Toast
```jsx
<AnimatePresence>
  {notifications.map(n => (
    <motion.div
      key={n.id}
      layout
      initial={{ opacity: 0, y: -20, scale: 0.95 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={{ opacity: 0, x: 100, transition: { duration: 0.2 } }}
      transition={{ type: 'spring', stiffness: 300, damping: 24 }}
      className="toast"
    >
      {n.message}
    </motion.div>
  ))}
</AnimatePresence>
```

## Recipe 6: Scroll Parallax Hero Background
```jsx
const { scrollY } = useScroll();
const y = useTransform(scrollY, [0, 500], [0, -150]);

<div style={{ position: 'relative', overflow: 'hidden', height: '80vh' }}>
  <motion.img
    src="/hero.jpg"
    style={{ y, scale: 1.2, width: '100%', height: '100%', objectFit: 'cover' }}
  />
  <div className="hero-content">/* Your text */</div>
</div>
```

## Recipe 7: Smooth Accordion
```jsx
function Accordion({ title, children }) {
  const [open, setOpen] = useState(false);
  return (
    <div>
      <button onClick={() => setOpen(!open)}>{title}</button>
      <AnimatePresence initial={false}>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.3, ease: 'easeInOut' }}
            style={{ overflow: 'hidden' }}
          >
            <div style={{ padding: '16px 0' }}>{children}</div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
```

## Recipe 8: Drag-to-Reorder List
```jsx
import { Reorder } from 'framer-motion';
const [items, setItems] = useState(['Item 1', 'Item 2', 'Item 3']);

<Reorder.Group axis="y" values={items} onReorder={setItems} style={{ listStyle: 'none', padding: 0 }}>
  {items.map(item => (
    <Reorder.Item key={item} value={item} style={{ cursor: 'grab', padding: '12px', background: '#fff', marginBottom: '8px', borderRadius: '8px' }}>
      {item}
    </Reorder.Item>
  ))}
</Reorder.Group>
```

## Recipe 9: SVG Draw-On Effect
```jsx
<svg viewBox="0 0 100 100">
  <motion.circle
    cx="50" cy="50" r="40"
    stroke="currentColor" strokeWidth="4" fill="none"
    initial={{ pathLength: 0 }}
    animate={{ pathLength: 1 }}
    transition={{ duration: 1.5, ease: 'easeInOut' }}
  />
</svg>
```

## Recipe 10: 3D Card Tilt on Hover
```jsx
function TiltCard({ children }) {
  const x = useMotionValue(0);
  const y = useMotionValue(0);
  const rotateX = useTransform(y, [-100, 100], [8, -8]);
  const rotateY = useTransform(x, [-100, 100], [-8, 8]);

  function onMouseMove(e) {
    const rect = e.currentTarget.getBoundingClientRect();
    x.set(e.clientX - rect.left - rect.width / 2);
    y.set(e.clientY - rect.top - rect.height / 2);
  }

  return (
    <motion.div
      onMouseMove={onMouseMove}
      onMouseLeave={() => { x.set(0); y.set(0); }}
      style={{ rotateX, rotateY, transformStyle: 'preserve-3d' }}
      transition={{ type: 'spring', stiffness: 150, damping: 20 }}
    >
      {children}
    </motion.div>
  );
}
```
