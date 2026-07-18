# PRD: Workout Session Viewer Webapp

## 1. Problem

Current training plan exists as a markdown file. When at the gym, Pranav has to:
- Scroll through text to find the exercise
- Visualise the movement from written notes
- Remember sets/reps/rest between browsing

He needs a **mobile-first webapp** that presents each session as a scrollable card stack — image first, instructions second — so he can prop his phone on the gym bench and follow without friction.

## 2. Users

- **Pranav** (primary). 52M, Mumbai. Gym 2x/week (Tue + Thu). Has a phone. Does not want to log in, install an app, or create an account.
- Future: same app could serve his running plan too (long run, tempo, speed sessions).

## 3. Functional Requirements

### 3.1 Session View (core screen)

- User lands on a page showing a **session** (e.g. "Tuesday — Upper Body + Core")
- Each **exercise** is one card. Card shows:
  - **Image** (photo or diagram of the exercise — squat, bench press, dead bug, etc.)
  - **Sets × Reps** (e.g. "3 × 10")
  - **Coaching note** (1 short sentence — "Bar on traps. Knees track toes.")
  - **Rest timer** (optional: tap to start a countdown)
- User swipes or scrolls down through cards in order

### 3.2 Sessions

Pre-seeded with the two gym sessions from the plan:

| Day | Session |
|---|---|
| Tuesday | Bench Press, Rows, Shoulder Press, Plank, Dead Bug |
| Thursday | Squat, Deadlift (RDL), Bench, Rows, Core Circuit, Glute Bridge |

Future: Pranav can add custom sessions or modify rep counts.

### 3.3 No auth, no backend

- Static PWA or single HTML file
- All data lives in a JSON blob or a tiny local store
- Hosted on GitHub Pages, Netlify, or similar — one URL to bookmark

### 3.4 Mobile-first

- Works on a phone screen in portrait mode
- Cards are large, text is readable without zoom
- Touch-friendly (swipe, tap)
- Works offline once loaded (service worker cache)

### 3.5 Image sourcing

- Prior art: use openly-licensed exercise photos or line diagrams
- If no good free images exist, generate them (FAL.ai / FLUX) — clean white-background photos of a person performing each movement
- Or: use simple SVG stick-figure diagrams with motion arrows (cheaper, consistent style)

## 4. Non-functional Requirements

- Loads in < 2s on 4G
- No build step required (vanilla HTML/CSS/JS or single-file framework)
- Can be edited by editing one JSON file — Pranav doesn't need to rebuild
- No tracking, no analytics, no cookies

## 5. Out of Scope (v1)

- User accounts
- Workout logging / history
- Progress charts
- Social features
- Push notifications
- Wearable integration

## 6. Future (v2 ideas)

- Running session view (Recovery / Speed / Tempo / Long run — pace, RPE, distance)
- Rest timer with sound
- "Today" auto-detection (shows Tue or Thu based on day of week)
- Exercise library view (all exercises with images)
- Progressive overload tracking (logging weights used)

## 7. Technical Approach (recommended)

**Option A — Single HTML file** (fastest to ship)
- One `index.html` with embedded CSS + JS + exercise data as a JSON object
- Host on GitHub Pages or Netlify drop
- Exercise images: generate with FLUX, store as data URLs or hosted images

**Option B — Simple static site** (slightly more maintainable)
- `index.html` + `style.css` + `app.js` + `exercises.json`
- Same hosting
- Easier to update exercise data without touching code

Recommend: **Option A** for v1. Less moving parts. Pranav can open it from his phone's browser, bookmark it, done.

## 8. Exercise images needed

| Exercise | Image type |
|---|---|
| Barbell Bench Press | Side view, bar at chest |
| Cable/Machine Seated Row | Side view, arms pulled back |
| Dumbbell Shoulder Press | Side view, dumbbells above head |
| Plank | Side view, body straight line |
| Dead Bug | Overhead/angled, arm+leg extended |
| Barbell Back Squat | Side view, at parallel depth |
| Barbell Deadlift (RDL) | Side view, hips hinged, back straight |
| Glute Bridge | Side view, hips raised, straight line |
| Thoracic Rotation | Top/angled, knees together, arm rotated |

9 images total for v1.
