#!/usr/bin/env python3
"""
Framer Motion Skill — Code Generator
Usage:
  python3 generate.py "<component_type>" --stack <stack> [--theme <theme>]

Component types:
  hero          — Animated hero section
  card          — Animated product/feature card
  modal         — Modal with backdrop and spring entrance
  navbar        — Sticky nav with scroll hide/show
  stagger-list  — Staggered list with scroll reveal
  page-transition — Full page transition wrapper
  tabs          — Tab switcher with animated indicator
  drawer        — Side drawer with AnimatePresence
  counter       — Animated number counter
  scroll-progress — Reading progress bar

Stacks: react, nextjs, tailwind
"""

import sys
import argparse

TEMPLATES = {
    "hero": """
// ============================================================
// FRAMER MOTION — Animated Hero Section
// Stack: {stack}
// ============================================================
import {{ motion }} from 'framer-motion';

const containerVariants = {{
  hidden: {{}},
  visible: {{
    transition: {{
      staggerChildren: 0.12,
      delayChildren: 0.2,
    }},
  }},
}};

const itemVariants = {{
  hidden: {{ opacity: 0, y: 32 }},
  visible: {{
    opacity: 1,
    y: 0,
    transition: {{
      duration: 0.6,
      ease: [0.22, 1, 0.36, 1],
    }},
  }},
}};

export function AnimatedHero() {{
  return (
    <motion.div
      variants={{containerVariants}}
      initial="hidden"
      animate="visible"
      className="{hero_class}"
    >
      <motion.p variants={{itemVariants}} className="eyebrow">
        Your Eyebrow Text
      </motion.p>

      <motion.h1 variants={{itemVariants}} className="heading">
        Your Hero Headline
      </motion.h1>

      <motion.p variants={{itemVariants}} className="subtext">
        Supporting description that sells the value proposition.
      </motion.p>

      <motion.div variants={{itemVariants}} className="cta-group">
        <motion.button
          whileHover={{{{ scale: 1.04, y: -2 }}}}
          whileTap={{{{ scale: 0.97 }}}}
          transition={{{{ type: 'spring', stiffness: 400, damping: 20 }}}}
          className="btn-primary"
        >
          Primary CTA
        </motion.button>

        <motion.button
          whileHover={{{{ scale: 1.02 }}}}
          whileTap={{{{ scale: 0.97 }}}}
          transition={{{{ type: 'spring', stiffness: 400, damping: 20 }}}}
          className="btn-secondary"
        >
          Secondary CTA
        </motion.button>
      </motion.div>
    </motion.div>
  );
}}
""",

    "card": """
// ============================================================
// FRAMER MOTION — Animated Card with Hover
// Stack: {stack}
// ============================================================
import {{ motion }} from 'framer-motion';

export function AnimatedCard({{ title, description, image, price }}) {{
  return (
    <motion.div
      initial={{{{ opacity: 0, y: 24 }}}}
      whileInView={{{{ opacity: 1, y: 0 }}}}
      viewport={{{{ once: true, amount: 0.3 }}}}
      transition={{{{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}}}
      whileHover={{{{
        y: -6,
        boxShadow: '0 20px 40px rgba(0,0,0,0.15)',
        transition: {{{{ duration: 0.2 }}}},
      }}}}
      className="{card_class}"
    >
      <motion.div
        className="card-image"
        whileHover={{{{ scale: 1.04 }}}}
        transition={{{{ duration: 0.4 }}}}
        style={{{{ overflow: 'hidden' }}}}
      >
        <img src={{image}} alt={{title}} />
      </motion.div>

      <div className="card-body">
        <h3>{{title}}</h3>
        <p>{{description}}</p>
        {{price && <span className="price">{{price}}</span>}}

        <motion.button
          whileHover={{{{ scale: 1.03 }}}}
          whileTap={{{{ scale: 0.97 }}}}
          transition={{{{ type: 'spring', stiffness: 400, damping: 20 }}}}
          className="btn-primary"
        >
          Add to Cart
        </motion.button>
      </div>
    </motion.div>
  );
}}
""",

    "modal": """
// ============================================================
// FRAMER MOTION — Modal with Backdrop
// Stack: {stack}
// ============================================================
import {{ motion, AnimatePresence }} from 'framer-motion';

const backdropVariants = {{
  hidden: {{ opacity: 0 }},
  visible: {{ opacity: 1 }},
}};

const modalVariants = {{
  hidden: {{ opacity: 0, scale: 0.88, y: 24 }},
  visible: {{
    opacity: 1,
    scale: 1,
    y: 0,
    transition: {{ type: 'spring', stiffness: 300, damping: 24 }},
  }},
  exit: {{
    opacity: 0,
    scale: 0.9,
    y: 16,
    transition: {{ duration: 0.2, ease: 'easeIn' }},
  }},
}};

export function Modal({{ isOpen, onClose, children }}) {{
  return (
    <AnimatePresence>
      {{isOpen && (
        <motion.div
          className="modal-backdrop"
          variants={{backdropVariants}}
          initial="hidden"
          animate="visible"
          exit="hidden"
          transition={{{{ duration: 0.25 }}}}
          onClick={{onClose}}
          style={{{{
            position: 'fixed', inset: 0,
            background: 'rgba(0,0,0,0.6)',
            backdropFilter: 'blur(6px)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            zIndex: 1000,
          }}}}
        >
          <motion.div
            className="modal-content"
            variants={{modalVariants}}
            initial="hidden"
            animate="visible"
            exit="exit"
            onClick={{(e) => e.stopPropagation()}}
            style={{{{
              background: '#fff',
              borderRadius: '16px',
              padding: '32px',
              maxWidth: '560px',
              width: '100%',
              boxShadow: '0 40px 80px rgba(0,0,0,0.3)',
            }}}}
          >
            {{children}}
          </motion.div>
        </motion.div>
      )}}
    </AnimatePresence>
  );
}}
""",

    "navbar": """
// ============================================================
// FRAMER MOTION — Sticky Navbar (hides on scroll down)
// Stack: {stack}
// ============================================================
import {{ motion, useScroll, useMotionValueEvent }} from 'framer-motion';
import {{ useState }} from 'react';

export function AnimatedNavbar() {{
  const {{ scrollY }} = useScroll();
  const [hidden, setHidden] = useState(false);
  const [lastY, setLastY] = useState(0);

  useMotionValueEvent(scrollY, 'change', (y) => {{
    setHidden(y > lastY && y > 80);
    setLastY(y);
  }});

  return (
    <motion.header
      animate={{{{ y: hidden ? '-100%' : '0%' }}}}
      transition={{{{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}}}
      style={{{{
        position: 'fixed', top: 0, left: 0, right: 0,
        zIndex: 100,
        background: '#fff',
        boxShadow: '0 2px 20px rgba(0,0,0,0.08)',
      }}}}
    >
      <nav className="{nav_class}">
        <div className="logo">Your Brand</div>
        <div className="nav-links">
          {{['Home', 'Shop', 'About', 'Contact'].map((item) => (
            <motion.a
              key={{item}}
              href="#"
              whileHover={{{{ color: 'var(--brand-primary)' }}}}
              transition={{{{ duration: 0.15 }}}}
            >
              {{item}}
            </motion.a>
          ))}}
        </div>
      </nav>
    </motion.header>
  );
}}
""",

    "stagger-list": """
// ============================================================
// FRAMER MOTION — Staggered Scroll Reveal List
// Stack: {stack}
// ============================================================
import {{ motion }} from 'framer-motion';

const containerVariants = {{
  hidden: {{}},
  visible: {{
    transition: {{
      staggerChildren: 0.08,
      delayChildren: 0.1,
    }},
  }},
}};

const itemVariants = {{
  hidden: {{ opacity: 0, x: -20 }},
  visible: {{
    opacity: 1,
    x: 0,
    transition: {{ duration: 0.4, ease: [0.22, 1, 0.36, 1] }},
  }},
}};

export function StaggerList({{ items }}) {{
  return (
    <motion.ul
      variants={{containerVariants}}
      initial="hidden"
      whileInView="visible"
      viewport={{{{ once: true, amount: 0.2 }}}}
      style={{{{ listStyle: 'none', padding: 0 }}}}
    >
      {{items.map((item, i) => (
        <motion.li
          key={{i}}
          variants={{itemVariants}}
          className="{list_item_class}"
        >
          {{item}}
        </motion.li>
      ))}}
    </motion.ul>
  );
}}
""",

    "page-transition": """
// ============================================================
// FRAMER MOTION — Page Transition Wrapper
// Stack: {stack}
// ============================================================
// Usage in Next.js _app.js or React Router outlet:
// <PageTransition key={{router.route}}><YourPage/></PageTransition>

import {{ motion, AnimatePresence }} from 'framer-motion';

const pageVariants = {{
  initial: {{ opacity: 0, y: 16 }},
  enter: {{
    opacity: 1,
    y: 0,
    transition: {{ duration: 0.4, ease: [0.22, 1, 0.36, 1] }},
  }},
  exit: {{
    opacity: 0,
    y: -12,
    transition: {{ duration: 0.25, ease: 'easeIn' }},
  }},
}};

// Wrap this around your router outlet:
export function PageTransitionWrapper({{ children, routeKey }}) {{
  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={{routeKey}}
        variants={{pageVariants}}
        initial="initial"
        animate="enter"
        exit="exit"
      >
        {{children}}
      </motion.div>
    </AnimatePresence>
  );
}}
""",

    "tabs": """
// ============================================================
// FRAMER MOTION — Animated Tab Switcher with Indicator
// Stack: {stack}
// ============================================================
import {{ motion }} from 'framer-motion';
import {{ useState }} from 'react';
import {{ LayoutGroup }} from 'framer-motion';

const tabs = ['Overview', 'Features', 'Pricing', 'FAQ'];

export function AnimatedTabs() {{
  const [active, setActive] = useState(tabs[0]);

  return (
    <div>
      <LayoutGroup>
        <div style={{{{ display: 'flex', gap: '4px', borderBottom: '1px solid #e5e7eb' }}}}>
          {{tabs.map((tab) => (
            <button
              key={{tab}}
              onClick={{() => setActive(tab)}}
              style={{{{
                position: 'relative',
                padding: '10px 20px',
                background: 'none',
                border: 'none',
                cursor: 'pointer',
                fontWeight: active === tab ? 600 : 400,
                color: active === tab ? 'var(--brand-primary)' : '#6b7280',
                transition: 'color 0.2s',
              }}}}
            >
              {{tab}}
              {{active === tab && (
                <motion.div
                  layoutId="tab-indicator"
                  style={{{{
                    position: 'absolute',
                    bottom: -1,
                    left: 0,
                    right: 0,
                    height: '2px',
                    background: 'var(--brand-primary)',
                    borderRadius: '2px',
                  }}}}
                  transition={{{{ type: 'spring', stiffness: 500, damping: 35 }}}}
                />
              )}}
            </button>
          ))}}
        </div>
      </LayoutGroup>

      <motion.div
        key={{active}}
        initial={{{{ opacity: 0, y: 8 }}}}
        animate={{{{ opacity: 1, y: 0 }}}}
        transition={{{{ duration: 0.2 }}}}
        style={{{{ padding: '24px 0' }}}}
      >
        {{/* Tab content for: {{active}} */}}
        <p>Content for {{active}} tab</p>
      </motion.div>
    </div>
  );
}}
""",

    "counter": """
// ============================================================
// FRAMER MOTION — Animated Number Counter (scroll-triggered)
// Stack: {stack}
// ============================================================
import {{ motion, useMotionValue, useInView, animate }} from 'framer-motion';
import {{ useEffect, useRef }} from 'react';

export function AnimatedCounter({{ from = 0, to, duration = 1.5, suffix = '' }}) {{
  const ref = useRef(null);
  const motionValue = useMotionValue(from);
  const isInView = useInView(ref, {{ once: true, amount: 0.5 }});
  const [display, setDisplay] = useState(from);

  useEffect(() => {{
    if (isInView) {{
      const controls = animate(motionValue, to, {{
        duration,
        ease: [0.22, 1, 0.36, 1],
        onUpdate: (v) => setDisplay(Math.round(v)),
      }});
      return controls.stop;
    }}
  }}, [isInView]);

  return (
    <motion.span ref={{ref}}>
      {{display}}{{suffix}}
    </motion.span>
  );
}}

// Usage:
// <AnimatedCounter to={{1250}} suffix="+" />
// <AnimatedCounter to={{98}} suffix="%" duration={{2}} />
""",

    "scroll-progress": """
// ============================================================
// FRAMER MOTION — Scroll Progress Bar
// Stack: {stack}
// ============================================================
import {{ motion, useScroll, useSpring }} from 'framer-motion';

export function ScrollProgressBar() {{
  const {{ scrollYProgress }} = useScroll();
  const scaleX = useSpring(scrollYProgress, {{
    stiffness: 100,
    damping: 30,
    restDelta: 0.001,
  }});

  return (
    <motion.div
      style={{{{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        height: '3px',
        background: 'var(--brand-primary)',
        transformOrigin: '0%',
        scaleX,
        zIndex: 9999,
      }}}}
    />
  );
}}

// Drop this at the top level of your app — it just works.
""",

    "drawer": """
// ============================================================
// FRAMER MOTION — Side Drawer
// Stack: {stack}
// ============================================================
import {{ motion, AnimatePresence }} from 'framer-motion';

export function Drawer({{ isOpen, onClose, side = 'right', children }}) {{
  const variants = {{
    hidden: {{ x: side === 'right' ? '100%' : '-100%', opacity: 0 }},
    visible: {{
      x: 0,
      opacity: 1,
      transition: {{ type: 'spring', stiffness: 300, damping: 30 }},
    }},
    exit: {{
      x: side === 'right' ? '100%' : '-100%',
      opacity: 0,
      transition: {{ duration: 0.25, ease: 'easeIn' }},
    }},
  }};

  return (
    <AnimatePresence>
      {{isOpen && (
        <>
          {{/* Backdrop */}}
          <motion.div
            initial={{{{ opacity: 0 }}}}
            animate={{{{ opacity: 1 }}}}
            exit={{{{ opacity: 0 }}}}
            onClick={{onClose}}
            style={{{{
              position: 'fixed', inset: 0,
              background: 'rgba(0,0,0,0.5)',
              zIndex: 200,
            }}}}
          />

          {{/* Drawer panel */}}
          <motion.div
            variants={{variants}}
            initial="hidden"
            animate="visible"
            exit="exit"
            style={{{{
              position: 'fixed',
              top: 0,
              [side]: 0,
              bottom: 0,
              width: '360px',
              maxWidth: '100vw',
              background: '#fff',
              zIndex: 201,
              overflowY: 'auto',
              padding: '24px',
              boxShadow: '-20px 0 60px rgba(0,0,0,0.15)',
            }}}}
          >
            {{children}}
          </motion.div>
        </>
      )}}
    </AnimatePresence>
  );
}}
"""
}

STACK_CLASSES = {
    "tailwind": {
        "hero_class": "flex flex-col items-start gap-6 py-24 px-8 max-w-4xl mx-auto",
        "card_class": "bg-white rounded-2xl overflow-hidden cursor-pointer",
        "nav_class": "flex items-center justify-between px-8 h-16 max-w-7xl mx-auto",
        "list_item_class": "py-3 border-b border-gray-100",
    },
    "react": {
        "hero_class": "hero-section",
        "card_class": "product-card",
        "nav_class": "navbar-inner",
        "list_item_class": "list-item",
    },
    "nextjs": {
        "hero_class": "hero-section",
        "card_class": "product-card",
        "nav_class": "navbar-inner",
        "list_item_class": "list-item",
    },
}

def main():
    parser = argparse.ArgumentParser(description="Framer Motion Code Generator")
    parser.add_argument("component", choices=list(TEMPLATES.keys()), help="Component to generate")
    parser.add_argument("--stack", default="tailwind", choices=["react", "nextjs", "tailwind"])
    args = parser.parse_args()

    classes = STACK_CLASSES.get(args.stack, STACK_CLASSES["react"])
    template = TEMPLATES[args.component]
    code = template.format(stack=args.stack, **classes)

    print(f"// Generated by Framer Motion Skill | Component: {args.component} | Stack: {args.stack}")
    print(code)

if __name__ == "__main__":
    main()
