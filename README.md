# Devfolio — Mugilan V C

A personal, responsive developer portfolio built with **semantic HTML and CSS**. The page uses a consistent two-font / three-colour system, a Flexbox header and navigation, a responsive CSS Grid for project cards, and mobile-first layout rules.

## Live website

https://mugilstrange-ai.github.io/devfolio/

## Repository

https://github.com/mugilstrange-ai/devfolio

## Run locally

```bash
git clone https://github.com/mugilstrange-ai/devfolio.git
cd devfolio
python3 -m http.server 8000
```

Open http://localhost:8000, or open `index.html` directly in a browser. No dependencies or bundler required.

## Project structure

- `index.html`: semantic header, nav, main, About and Projects sections, contact footer
- `style.css`: brand/ink/paper variables, Flexbox, Grid, one/two-column responsive breakpoints, keyboard focus styling
- `assets/favicon.svg`: portfolio favicon (added in feature PR)

## Contact

- Email: mailto:mugilstrange@gmail.com
- GitHub: https://github.com/mugilstrange-ai
- LinkedIn: link is labeled **LinkedIn search**, since no personal profile URL could be verified. It is intentionally not presented as a verified personal profile.

## Deployment

GitHub Pages serves `index.html` from repository `main`, at the URL above. The portfolio is static HTML/CSS; no build step is required.
