"""Visual theme for InterviewForge AI — an ironworks / forge motif.

Palette:
  iron-900  #1B1815   warm near-black background
  iron-800  #26221D   panel background
  ash-100   #EFE8DC   primary text / cream
  ember     #E8622C   primary accent (hot metal)
  gold      #E8A93A   secondary accent (spark / highlight)
  slate     #6E7A7A   muted steel for secondary text
Typography: Space Grotesk for headings (geometric, industrial),
IBM Plex Sans for body copy.
"""

FORGE_CSS = """
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">

<style>
:root {
  --iron-900: #1B1815;
  --iron-800: #262019;
  --iron-700: #322A21;
  --ash-100: #EFE8DC;
  --ash-300: #C9BFAF;
  --ember: #E8622C;
  --ember-dim: #B84A1E;
  --gold: #E8A93A;
  --slate: #8B9491;
}

html, body, [class*="css"]  {
  font-family: 'IBM Plex Sans', sans-serif;
}

.stApp {
  background:
    radial-gradient(ellipse 900px 500px at 15% -10%, rgba(232,98,44,0.10), transparent 60%),
    radial-gradient(ellipse 700px 500px at 100% 0%, rgba(232,169,58,0.06), transparent 55%),
    var(--iron-900);
  color: var(--ash-100);
}

h1, h2, h3, h4 {
  font-family: 'Space Grotesk', sans-serif !important;
  color: var(--ash-100) !important;
  letter-spacing: -0.01em;
}

/* Hero title bar */
.forge-hero {
  display: flex;
  align-items: baseline;
  gap: 14px;
  border-bottom: 1px solid var(--iron-700);
  padding-bottom: 18px;
  margin-bottom: 6px;
}
.forge-hero .anvil {
  font-size: 2.1rem;
  line-height: 1;
}
.forge-hero h1 {
  font-size: 2.0rem !important;
  margin: 0 !important;
  background: linear-gradient(90deg, var(--ash-100) 30%, var(--ember) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.forge-tagline {
  color: var(--slate);
  font-size: 0.95rem;
  margin-top: -4px;
}

/* Stage stepper (sidebar) */
.stage-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 7px 10px;
  border-radius: 8px;
  margin-bottom: 2px;
  font-size: 0.88rem;
}
.stage-item .num {
  width: 20px; height: 20px;
  border-radius: 5px;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.72rem;
  font-family: 'Space Grotesk', sans-serif;
  flex-shrink: 0;
}
.stage-current { background: rgba(232,98,44,0.14); }
.stage-current .num { background: var(--ember); color: #1B1815; font-weight: 700; }
.stage-current span.label { color: var(--ash-100); font-weight: 600; }
.stage-done .num { background: var(--iron-700); color: var(--gold); border: 1px solid var(--gold); }
.stage-done span.label { color: var(--ash-300); }
.stage-todo .num { background: var(--iron-700); color: var(--slate); }
.stage-todo span.label { color: var(--slate); }

/* Cards */
.forge-card {
  background: var(--iron-800);
  border: 1px solid var(--iron-700);
  border-left: 3px solid var(--ember);
  border-radius: 10px;
  padding: 16px 18px;
  margin-bottom: 14px;
}
.forge-card h4 { margin-top: 0 !important; font-size: 1.02rem !important; }
.forge-card.gold { border-left-color: var(--gold); }
.forge-card.slate { border-left-color: var(--slate); }

/* Priority chips */
.chip {
  display: inline-block;
  font-size: 0.72rem;
  font-family: 'Space Grotesk', sans-serif;
  padding: 2px 9px;
  border-radius: 20px;
  font-weight: 600;
  margin-left: 8px;
}
.chip-high { background: rgba(232,98,44,0.18); color: var(--ember); border: 1px solid var(--ember-dim); }
.chip-medium { background: rgba(232,169,58,0.18); color: var(--gold); border: 1px solid var(--gold); }
.chip-low { background: rgba(139,148,145,0.18); color: var(--slate); border: 1px solid var(--slate); }

/* Score dial-ish metric block */
.score-block {
  text-align: center;
  background: var(--iron-800);
  border: 1px solid var(--iron-700);
  border-radius: 12px;
  padding: 18px 10px;
}
.score-block .num {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.1rem;
  font-weight: 700;
  color: var(--ember);
}
.score-block .label {
  font-size: 0.78rem;
  color: var(--slate);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

/* Buttons */
div.stButton > button, div.stDownloadButton > button {
  background: var(--ember);
  color: #1B1815;
  border: none;
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  border-radius: 8px;
  padding: 0.5em 1.1em;
}
div.stButton > button:hover, div.stDownloadButton > button:hover {
  background: var(--gold);
  color: #1B1815;
}
div.stButton > button:disabled {
  background: var(--iron-700);
  color: var(--slate);
}

section[data-testid="stSidebar"] {
  background: var(--iron-800);
  border-right: 1px solid var(--iron-700);
}

hr { border-color: var(--iron-700) !important; }
</style>
"""


def hero_html(title="InterviewForge AI", tagline="Forge a sharper interview, one stage at a time."):
    return f"""
<div class="forge-hero">
  <div class="anvil">🔥</div>
  <h1>{title}</h1>
</div>
<div class="forge-tagline">{tagline}</div>
<div style="height: 18px"></div>
"""


def stage_sidebar_html(steps, current_index):
    rows = []
    for i, name in enumerate(steps):
        if i < current_index:
            cls, mark = "stage-done", "✓"
        elif i == current_index:
            cls, mark = "stage-current", str(i + 1)
        else:
            cls, mark = "stage-todo", str(i + 1)
        rows.append(
            f'<div class="stage-item {cls}"><div class="num">{mark}</div>'
            f'<span class="label">{name}</span></div>'
        )
    return "<div>" + "".join(rows) + "</div>"


def chip(priority):
    p = (priority or "").lower()
    cls = "chip-high" if p == "high" else "chip-medium" if p == "medium" else "chip-low"
    return f'<span class="chip {cls}">{priority}</span>'
