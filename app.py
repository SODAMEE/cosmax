"""성분노트 — Streamlit Cloud 앱
디자인과 JavaScript 인터랙션(피부 타입 선택, 성분 드롭다운 등)을 그대로
유지하기 위해 원본 HTML을 이 파일 안에 문자열로 통합했습니다.
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="성분노트 — 사기 전에 먼저 확인하는 화장품 성분",
    page_icon="🧪",
    layout="wide",
)

# Streamlit 기본 여백/헤더/푸터 제거 → HTML이 전체 화면을 차지하도록
st.markdown(
    """
    <style>
      #MainMenu, header, footer { visibility: hidden; }
      .block-container {
          padding: 0 !important;
          max-width: 100% !important;
      }
      iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_SOURCE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>성분노트 — 사기 전에 먼저 확인하는 화장품 성분</title>
<style>
  :root {
    --paper: #fff8f6;
    --paper-raised: #f8f8f8;
    --ink: #2a2024;
    --ink-soft: #6e5a5e;
    --ink-faint: #a28f92;
    --line: #ebd9db;
    --accent: #e8959e;
    --accent-strong: #ad5560;
    --accent-soft: #fcebed;
    --accent-deep: #ad5560;
    --ink-on-fill: #33191d;
    --secondary: #ffa987;
    --secondary-strong: #ff8f63;
    --safe: #2f8c5b;
    --safe-bg: #e3f3e7;
    --caution: #a6741f;
    --caution-bg: #fbf0dc;
    --avoid: #b14538;
    --avoid-bg: #fbe7e2;
    --shadow: 0 24px 48px -28px rgba(173, 85, 96, 0.28);
    --radius: 18px;
    --font-sans: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Malgun Gothic", "Segoe UI", system-ui, sans-serif;
    --font-mono: ui-monospace, "SFMono-Regular", "Consolas", "Liberation Mono", "Menlo", monospace;
  }

  :root[data-theme="dark"] {
    --paper: #201519;
    --paper-raised: #2a1d20;
    --ink: #f2e7e9;
    --ink-soft: #c9afb2;
    --ink-faint: #8c7175;
    --line: #453035;
    --accent: #f0a0aa;
    --accent-strong: #f6bac1;
    --accent-soft: #3a2429;
    --accent-deep: #ad5560;
    --ink-on-fill: #33191d;
    --secondary: #ffb294;
    --secondary-strong: #ff9e78;
    --safe: #6bcb92;
    --safe-bg: #16351f;
    --caution: #e3b45a;
    --caution-bg: #3a2c11;
    --avoid: #e1867a;
    --avoid-bg: #3b1d16;
    --shadow: 0 24px 48px -28px rgba(0, 0, 0, 0.6);
  }

  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --paper: #201519;
      --paper-raised: #2a1d20;
      --ink: #f2e7e9;
      --ink-soft: #c9afb2;
      --ink-faint: #8c7175;
      --line: #453035;
      --accent: #f0a0aa;
      --accent-strong: #f6bac1;
      --accent-soft: #3a2429;
      --accent-deep: #ad5560;
      --ink-on-fill: #33191d;
      --secondary: #ffb294;
      --secondary-strong: #ff9e78;
      --safe: #6bcb92;
      --safe-bg: #16351f;
      --caution: #e3b45a;
      --caution-bg: #3a2c11;
      --avoid: #e1867a;
      --avoid-bg: #3b1d16;
      --shadow: 0 24px 48px -28px rgba(0, 0, 0, 0.6);
    }
  }

  * { box-sizing: border-box; }
  html { -webkit-text-size-adjust: 100%; }

  body {
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: var(--font-sans);
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }

  img, svg { display: block; max-width: 100%; }

  a { color: inherit; }

  :focus-visible {
    outline: 2.5px solid var(--accent);
    outline-offset: 3px;
    border-radius: 4px;
  }

  .wrap {
    max-width: 1120px;
    margin: 0 auto;
    padding-inline: clamp(1.25rem, 4vw, 2.5rem);
  }

  /* ---------- Header ---------- */
  header.site {
    position: sticky;
    top: 0;
    z-index: 40;
    backdrop-filter: blur(10px);
    background: color-mix(in srgb, var(--paper) 82%, transparent);
    border-bottom: 1px solid var(--line);
  }

  .nav-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding-block: 0.9rem;
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    font-weight: 800;
    font-size: 1.05rem;
    letter-spacing: -0.01em;
    text-decoration: none;
  }

  .logo-mark {
    width: 30px;
    height: 30px;
    border-radius: 8px;
    background: var(--accent-strong);
    color: var(--paper-raised);
    display: grid;
    place-items: center;
    flex: none;
  }

  .logo-mark svg { width: 17px; height: 17px; stroke: currentColor; fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    border-radius: 999px;
    font-family: inherit;
    font-weight: 700;
    font-size: 0.92rem;
    padding: 0.7rem 1.35rem;
    min-height: 44px;
    border: 1.5px solid transparent;
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.15s ease, background 0.15s ease, border-color 0.15s ease;
    white-space: nowrap;
  }
  .btn:active { transform: translateY(1px); }

  .btn-primary { background: var(--secondary); color: var(--ink-on-fill); }
  .btn-primary:hover { background: var(--secondary-strong); }

  .btn-ghost { background: transparent; color: var(--ink); border-color: var(--line); }
  .btn-ghost:hover { border-color: var(--accent-strong); color: var(--accent-strong); }

  .btn-sm { padding: 0.55rem 1.05rem; font-size: 0.85rem; }

  /* ---------- Hero ---------- */
  .hero {
    position: relative;
    overflow: hidden;
    padding-block: clamp(2.75rem, 7vw, 5.5rem);
  }

  .hero::before {
    content: "";
    position: absolute;
    inset: -15% -10%;
    background:
      radial-gradient(38% 45% at 12% 15%, color-mix(in srgb, var(--accent) 40%, transparent), transparent 70%),
      radial-gradient(32% 40% at 88% 10%, color-mix(in srgb, var(--secondary) 35%, transparent), transparent 70%),
      radial-gradient(45% 50% at 50% 100%, color-mix(in srgb, var(--accent-soft) 70%, transparent), transparent 70%);
    filter: blur(50px);
    z-index: 0;
    pointer-events: none;
  }

  .hero > .wrap { position: relative; z-index: 1; }

  .hero-grid {
    display: grid;
    grid-template-columns: 1.1fr 0.95fr;
    gap: clamp(2rem, 5vw, 4rem);
    align-items: center;
  }

  .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: var(--font-mono);
    font-size: 0.78rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--accent-strong);
    background: var(--accent-soft);
    border-radius: 999px;
    padding: 0.35rem 0.75rem;
    margin-bottom: 1.1rem;
  }

  h1 {
    font-size: clamp(1.9rem, 1.3rem + 2.6vw, 3.15rem);
    line-height: 1.18;
    letter-spacing: -0.02em;
    margin: 0 0 1.1rem;
    text-wrap: balance;
  }

  h1 em {
    font-style: normal;
    color: var(--accent-strong);
  }

  .lede {
    font-size: clamp(1rem, 0.94rem + 0.3vw, 1.15rem);
    color: var(--ink-soft);
    max-width: 46ch;
    margin: 0 0 1.9rem;
  }

  .hero-ctas {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-bottom: 1.4rem;
  }

  .hero-note {
    font-size: 0.85rem;
    color: var(--ink-faint);
  }

  /* ---------- Hero visual: scan card ---------- */
  .scan-card {
    position: relative;
    background: var(--paper-raised);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 1.5rem;
    overflow: hidden;
  }

  .scan-frame {
    position: relative;
    border-radius: 12px;
    background: color-mix(in srgb, var(--ink) 4%, var(--paper-raised));
    padding: 1.2rem 1.1rem;
    overflow: hidden;
  }

  .scan-frame::before,
  .scan-frame::after,
  .corner-tl, .corner-br {
    content: "";
    position: absolute;
    width: 22px;
    height: 22px;
    border: 3px solid var(--accent);
  }
  .scan-frame::before { top: 8px; left: 8px; border-right: none; border-bottom: none; border-radius: 4px 0 0 0; }
  .scan-frame::after { bottom: 8px; right: 8px; border-left: none; border-top: none; border-radius: 0 0 4px 0; }
  .corner-tl { top: 8px; right: 8px; border-left: none; border-bottom: none; border-radius: 0 4px 0 0; }
  .corner-br { bottom: 8px; left: 8px; border-right: none; border-top: none; border-radius: 0 0 0 4px; }

  .label-lines {
    font-family: var(--font-mono);
    font-size: 0.78rem;
    color: var(--ink-soft);
    display: grid;
    gap: 0.5rem;
    padding: 0.6rem 0.4rem 0.8rem;
  }

  .label-lines .lbl-head {
    font-size: 0.68rem;
    letter-spacing: 0.1em;
    color: var(--ink-faint);
    text-transform: uppercase;
    margin-bottom: 0.1rem;
  }

  .label-lines span.hl {
    color: var(--avoid);
    font-weight: 700;
  }

  .scanline {
    position: absolute;
    left: 6%;
    right: 6%;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    box-shadow: 0 0 14px 2px color-mix(in srgb, var(--accent) 60%, transparent);
    animation: sweep 3.2s ease-in-out infinite;
  }

  @keyframes sweep {
    0%   { top: 12%; opacity: 0; }
    10%  { opacity: 1; }
    50%  { top: 82%; }
    90%  { opacity: 1; }
    100% { top: 12%; opacity: 0; }
  }

  .verdict-pop {
    position: absolute;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-family: var(--font-mono);
    font-size: 0.72rem;
    font-weight: 700;
    padding: 0.3rem 0.6rem;
    border-radius: 999px;
    box-shadow: var(--shadow);
  }
  .verdict-pop.p1 { top: 14%; right: -8px; background: var(--safe-bg); color: var(--safe); animation: pop 3.2s ease-in-out infinite; }
  .verdict-pop.p2 { bottom: 18%; left: -10px; background: var(--avoid-bg); color: var(--avoid); animation: pop 3.2s ease-in-out infinite 0.25s; }

  @keyframes pop {
    0%, 40% { transform: scale(0.7); opacity: 0; }
    55%, 85% { transform: scale(1); opacity: 1; }
    100% { transform: scale(1); opacity: 1; }
  }

  @media (prefers-reduced-motion: reduce) {
    .scanline { animation: none; opacity: 0; }
    .verdict-pop { animation: none; opacity: 1; transform: none; }
  }

  /* ---------- Section shared ---------- */
  section { padding-block: clamp(2.5rem, 6vw, 4.5rem); }
  section.alt { background: var(--paper-raised); border-block: 1px solid var(--line); }

  .section-head { max-width: 62ch; margin-bottom: clamp(1.75rem, 4vw, 2.75rem); }
  .section-head .eyebrow { margin-bottom: 0.9rem; }
  h2 { font-size: clamp(1.5rem, 1.2rem + 1vw, 2.1rem); letter-spacing: -0.015em; margin: 0 0 0.6rem; text-wrap: balance; }
  .section-head p { color: var(--ink-soft); margin: 0; font-size: 1rem; }

  /* ---------- Pain points ---------- */
  .pain-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.1rem;
  }

  .pain-card {
    background: var(--paper-raised);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 1.4rem 1.3rem;
  }

  .pain-card .tag {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    color: var(--avoid);
    background: var(--avoid-bg);
    display: inline-block;
    padding: 0.2rem 0.55rem;
    border-radius: 6px;
    margin-bottom: 0.75rem;
  }

  .pain-card h3 { font-size: 1.02rem; margin: 0 0 0.4rem; letter-spacing: -0.01em; }
  .pain-card p { margin: 0; font-size: 0.92rem; color: var(--ink-soft); }

  /* ---------- Ingredient database ---------- */
  #ingredient-db { position: relative; overflow: hidden; }

  .section-deco {
    position: absolute;
    right: -3%;
    bottom: -6%;
    width: clamp(200px, 24vw, 320px);
    height: auto;
    stroke: var(--ink);
    fill: none;
    stroke-width: 1.2;
    stroke-linecap: round;
    stroke-linejoin: round;
    opacity: 0.06;
    z-index: 0;
    pointer-events: none;
  }

  #ingredient-db .wrap { position: relative; z-index: 1; }

  .ingdb-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.1rem;
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .ingdb-card {
    background: var(--paper-raised);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 1.4rem 1.3rem;
  }

  .ingdb-tag {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    color: var(--caution);
    background: var(--caution-bg);
    display: inline-block;
    padding: 0.2rem 0.55rem;
    border-radius: 6px;
    margin-bottom: 0.75rem;
  }

  .ingdb-card h3 { font-family: var(--font-mono); font-size: 0.98rem; font-weight: 700; margin: 0 0 0.4rem; letter-spacing: -0.01em; }
  .ingdb-card p { margin: 0; font-size: 0.88rem; color: var(--ink-soft); }

  /* ---------- How it works ---------- */
  .steps {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    counter-reset: step;
  }

  .step {
    position: relative;
    padding-top: 2.6rem;
  }

  .step::before {
    counter-increment: step;
    content: "0" counter(step);
    font-family: var(--font-mono);
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--accent-strong);
    background: var(--accent-soft);
    width: 2.3rem;
    height: 2.3rem;
    border-radius: 50%;
    display: grid;
    place-items: center;
    position: absolute;
    top: 0;
    left: 0;
  }

  .step h3 { font-size: 1.05rem; margin: 0 0 0.5rem; letter-spacing: -0.01em; }
  .step p { margin: 0; color: var(--ink-soft); font-size: 0.93rem; }

  .steps .step:not(:last-child)::after {
    content: "";
    position: absolute;
    top: 1.15rem;
    left: 2.9rem;
    right: -1.5rem;
    height: 1px;
    background: repeating-linear-gradient(90deg, var(--line) 0 6px, transparent 6px 12px);
  }
  @media (max-width: 900px) {
    .steps .step::after { display: none; }
  }

  /* ---------- Demo ---------- */
  .demo-grid {
    display: grid;
    grid-template-columns: 0.95fr 1.05fr;
    gap: clamp(1.75rem, 4vw, 3rem);
    align-items: start;
  }

  .panel {
    background: var(--paper-raised);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: clamp(1.3rem, 3vw, 1.9rem);
  }

  .field-label {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--ink-faint);
    margin-bottom: 0.6rem;
    display: block;
  }

  .pill-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin-bottom: 1.5rem;
  }

  .pill {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-family: inherit;
    font-size: 0.88rem;
    font-weight: 600;
    border: 1.5px solid var(--line);
    background: var(--paper);
    color: var(--ink-soft);
    border-radius: 999px;
    padding: 0.5rem 1.1rem;
    min-height: 44px;
    cursor: pointer;
    transition: all 0.15s ease;
  }
  .pill:hover { border-color: var(--accent); color: var(--ink); }

  .pill.is-active {
    background: var(--accent);
    border-color: var(--accent);
    color: var(--ink-on-fill);
  }

  .demo-hint { font-size: 0.82rem; color: var(--ink-faint); margin: 0.6rem 0 0; }

  .dropdown-toggle {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.6rem;
    font-family: inherit;
    font-size: 0.92rem;
    font-weight: 600;
    color: var(--ink);
    background: var(--paper);
    border: 1.5px solid var(--line);
    border-radius: 14px;
    padding: 0 1.1rem;
    min-height: 44px;
    cursor: pointer;
    transition: border-color 0.15s ease;
  }
  .dropdown-toggle:hover { border-color: var(--accent); }
  .dropdown-toggle[aria-expanded="true"] { border-color: var(--accent-strong); border-radius: 14px 14px 0 0; }

  .toggle-label { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; text-align: left; }

  .chev { flex: none; width: 16px; height: 16px; stroke: currentColor; fill: none; stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; transition: transform 0.15s ease; }
  .dropdown-toggle[aria-expanded="true"] .chev { transform: rotate(180deg); }

  .dropdown-panel {
    display: flex;
    flex-direction: column;
    border: 1.5px solid var(--accent-strong);
    border-top: none;
    border-radius: 0 0 14px 14px;
    overflow: hidden;
  }

  .option-row {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    width: 100%;
    font-family: inherit;
    font-size: 0.9rem;
    font-weight: 500;
    color: var(--ink-soft);
    background: var(--paper);
    border: none;
    border-top: 1px solid var(--line);
    padding: 0.7rem 1.1rem;
    min-height: 44px;
    cursor: pointer;
    text-align: left;
    transition: background 0.15s ease, color 0.15s ease;
  }
  .option-row:first-child { border-top: none; }
  .option-row:hover { background: var(--paper-raised); }

  .option-check {
    flex: none;
    width: 20px;
    height: 20px;
    border-radius: 6px;
    border: 1.5px solid var(--line);
    display: grid;
    place-items: center;
    color: transparent;
    background: var(--paper-raised);
    transition: all 0.15s ease;
  }
  .option-check svg { width: 13px; height: 13px; stroke: currentColor; fill: none; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }

  .option-row.is-active { color: var(--ink); background: var(--avoid-bg); }
  .option-row.is-active .option-check { background: var(--avoid); border-color: var(--avoid); color: #fff; }

  [hidden] { display: none !important; }

  /* result side */
  .result-subhead {
    font-size: 0.95rem;
    font-weight: 800;
    letter-spacing: -0.01em;
    margin: 1.4rem 0 0.75rem;
  }
  .result-subhead:first-of-type { margin-top: 0; }

  .watch-list { display: grid; gap: 0.6rem; margin: 0; padding: 0; list-style: none; }

  .watch-item {
    display: flex;
    align-items: flex-start;
    gap: 0.65rem;
    padding: 0.75rem 0.85rem;
    border-radius: 10px;
    border: 1px solid var(--line);
    background: var(--paper);
  }

  .watch-icon {
    flex: none;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    background: var(--caution-bg);
    color: var(--caution);
  }
  .watch-icon svg { width: 14px; height: 14px; stroke: currentColor; fill: none; stroke-width: 2.6; stroke-linecap: round; stroke-linejoin: round; }

  .watch-list.combo .watch-icon { background: var(--avoid-bg); color: var(--avoid); }
  .watch-list.recommend .watch-icon { background: var(--safe-bg); color: var(--safe); }

  .watch-body { flex: 1 1 auto; min-width: 0; }

  .watch-name { font-family: var(--font-mono); font-weight: 700; font-size: 0.92rem; margin-bottom: 0.2rem; overflow-wrap: break-word; word-break: break-word; }
  .watch-why { font-size: 0.85rem; color: var(--ink-soft); overflow-wrap: break-word; word-break: break-word; }

  .watch-empty { color: var(--ink-faint); font-size: 0.88rem; padding: 1.1rem 0.5rem; text-align: center; border: 1px dashed var(--line); border-radius: 10px; }

  .routine-list { display: grid; gap: 0.6rem; margin: 0; padding: 0; list-style: none; }

  .routine-step {
    display: flex;
    align-items: flex-start;
    gap: 0.65rem;
    padding: 0.75rem 0.85rem;
    border-radius: 10px;
    border: 1px solid var(--line);
    background: var(--paper);
  }

  .routine-num {
    flex: none;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    background: var(--accent-soft);
    color: var(--accent-strong);
    font-family: var(--font-mono);
    font-weight: 700;
    font-size: 0.8rem;
  }

  /* ---------- CTA ---------- */
  .cta-band {
    text-align: center;
    background: var(--accent-deep);
    color: #fdfdfa;
    border-radius: var(--radius);
    padding: clamp(2rem, 5vw, 3.2rem);
    margin-inline: clamp(1.25rem, 4vw, 2.5rem);
  }
  .cta-band h2 { color: #fdfdfa; margin-bottom: 0.5rem; }
  .cta-band p { color: color-mix(in srgb, #fdfdfa 78%, transparent); margin: 0 0 1.4rem; }
  .cta-band .btn-primary { background: #fdfdfa; color: var(--accent-deep); }
  .cta-band .btn-primary:hover { background: color-mix(in srgb, #fdfdfa 90%, var(--accent)); }

  footer.site {
    text-align: center;
    padding: 2.5rem 1.25rem 3rem;
    color: var(--ink-faint);
    font-size: 0.85rem;
  }

  /* ---------- Responsive ---------- */
  /* Desktop default: pain-grid / steps = 3 columns (see base rules above) */

  /* Tablet: 2 columns */
  @media (max-width: 900px) {
    .hero-grid { grid-template-columns: 1fr; }
    .pain-grid { grid-template-columns: repeat(2, 1fr); }
    .steps { grid-template-columns: repeat(2, 1fr); }
    .demo-grid { grid-template-columns: 1fr; }
    .ingdb-grid { grid-template-columns: repeat(2, 1fr); }
  }

  /* Mobile: 1 column + larger base type */
  @media (max-width: 600px) {
    html { font-size: 18px; }
    .pain-grid { grid-template-columns: 1fr; }
    .steps { grid-template-columns: 1fr; }
    .ingdb-grid { grid-template-columns: 1fr; }
  }

  @media (max-width: 520px) {
    .hero-ctas .btn { flex: 1 1 auto; }
    .hero-ctas { flex-direction: column; }
  }
</style>
</head>
<body>

  <header class="site">
    <div class="wrap nav-row">
      <a class="logo" href="#top">
        <span class="logo-mark">
          <svg viewBox="0 0 24 24"><path d="M9 3h6M10 3v5.2L4.8 18a2 2 0 0 0 1.8 3h10.8a2 2 0 0 0 1.8-3L14 8.2V3" /><path d="M7.5 14h9" /></svg>
        </span>
        성분노트
      </a>
    </div>
  </header>

  <main id="top">
    <section class="hero">
      <div class="wrap hero-grid">
        <div>
          <span class="eyebrow">민감성 · 트러블 피부를 위한 성분 판독기</span>
          <h1>성분 때문에<br><em>고민하지 마세요</em></h1>
          <p class="lede">성분표 속 어려운 이름들 때문에 고민하지 마세요. 내 피부 타입에 맞는 성분과 조심할 조합, 케어 루틴까지 한 번에 알려드려요.</p>
          <div class="hero-ctas">
            <a class="btn btn-primary" href="#demo">무료로 성분 확인해보기</a>
          </div>
          <p class="hero-note">회원가입 없이 체험판으로 먼저 확인해볼 수 있어요.</p>
        </div>

        <div class="scan-card" aria-hidden="true">
          <div class="scan-frame">
            <span class="corner-tl"></span>
            <span class="corner-br"></span>
            <div class="scanline"></div>
            <div class="label-lines">
              <div class="lbl-head">전성분 (INCI)</div>
              <div>정제수, 글리세린, 다이메티콘</div>
              <div>페녹시에탄올, <span class="hl">향료</span></div>
              <div><span class="hl">에탄올</span>, 메틸파라벤</div>
              <div>티트리잎추출물, 토코페롤</div>
            </div>
            <span class="verdict-pop p1">✓ 적합</span>
            <span class="verdict-pop p2">✕ 비적합</span>
          </div>
        </div>
      </div>
    </section>

    <section class="alt">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">이런 경험, 있으신가요</span>
          <h2>성분표는 늘 어렵고, 트러블은 늘 뒤늦게 옵니다</h2>
          <p>화장품 뒷면 성분표는 낯선 화학 용어로 빼곡해서, 읽어도 내게 맞는지 판단하기가 쉽지 않아요.</p>
        </div>
        <div class="pain-grid">
          <div class="pain-card">
            <span class="tag">이해 불가</span>
            <h3>성분표를 봐도 알 수가 없어요</h3>
            <p>어려운 화학 용어로 나열된 성분표만으로는 이게 내 피부에 맞는 제품인지 판단하기 어려워요.</p>
          </div>
          <div class="pain-card">
            <span class="tag">뒤늦은 후회</span>
            <h3>모르고 사서 트러블을 겪어요</h3>
            <p>알코올, 특정 향료, 특정 방부제처럼 나에게 트러블을 유발하는 성분을 모른 채 구매하곤 해요.</p>
          </div>
          <div class="pain-card">
            <span class="tag">반복되는 시행착오</span>
            <h3>맞는 제품 찾기까지 비용이 쌓여요</h3>
            <p>안 맞는 제품을 버리고 다시 다른 제품을 시도하는 과정이 반복되며 시간과 비용이 낭비돼요.</p>
          </div>
        </div>
      </div>
    </section>

    <section id="how">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">이용 방법</span>
          <h2>세 단계면 충분해요</h2>
          <p>내 피부 타입만 알아도, 조심해야 할 성분을 미리 걸러낼 수 있어요.</p>
        </div>
        <div class="steps">
          <div class="step">
            <h3>내 피부 타입 선택</h3>
            <p>건성·지성·복합성·민감성 중 내 피부 타입을 골라주세요.</p>
          </div>
          <div class="step">
            <h3>주의 성분 · 조합 확인</h3>
            <p>내 피부 타입이 자극받기 쉬운 성분과, 함께 쓰면 안 좋은 성분 조합을 보여드려요.</p>
          </div>
          <div class="step">
            <h3>성분표에서 미리 피하기</h3>
            <p>매장이나 온라인에서 성분표를 볼 때, 이 목록에 있는 성분이 있는지 미리 확인해보세요.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="alt" id="demo">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">체험해보기</span>
          <h2>피부 타입과 조심할 성분을 골라보세요</h2>
          <p>피부 타입을 고르고, 이미 쓰고 있거나 신경 쓰이는 성분을 선택하면 주의할 조합과 함께 쓰면 좋은 성분을 알려드려요.</p>
        </div>

        <div class="demo-grid">
          <div class="panel">
            <span class="field-label">① 피부 타입 선택</span>
            <div class="pill-row" id="skinTypeRow">
              <button type="button" class="pill" data-skin="건성">건성</button>
              <button type="button" class="pill" data-skin="지성">지성</button>
              <button type="button" class="pill" data-skin="복합성">복합성</button>
              <button type="button" class="pill is-active" data-skin="민감성">민감성</button>
            </div>

            <span class="field-label">② 조심해야 할 성분 선택</span>
            <button type="button" id="ingredientToggle" class="dropdown-toggle" aria-expanded="false" aria-controls="ingredientPanel">
              <span class="toggle-label" id="ingredientToggleLabel">성분을 선택해주세요</span>
              <svg class="chev" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
            </button>
            <div id="ingredientPanel" class="dropdown-panel" hidden>
              <button type="button" class="option-row" data-ing="알코올">
                <span class="option-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>🧪 알코올
              </button>
              <button type="button" class="option-row" data-ing="인공향료">
                <span class="option-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>🌸 인공향료
              </button>
              <button type="button" class="option-row" data-ing="파라벤">
                <span class="option-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>🧫 파라벤
              </button>
              <button type="button" class="option-row" data-ing="실리콘">
                <span class="option-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>✨ 실리콘
              </button>
              <button type="button" class="option-row" data-ing="특정 방부제">
                <span class="option-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>🛡️ 특정 방부제
              </button>
              <button type="button" class="option-row" data-ing="레티놀">
                <span class="option-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>🌙 레티놀
              </button>
              <button type="button" class="option-row" data-ing="비타민C">
                <span class="option-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>🍊 비타민C
              </button>
              <button type="button" class="option-row" data-ing="AHA/BHA">
                <span class="option-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>🍋 AHA/BHA
              </button>
              <button type="button" class="option-row" data-ing="벤조일퍼옥사이드">
                <span class="option-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>💥 벤조일퍼옥사이드
              </button>
              <button type="button" class="option-row" data-ing="에센셜 오일">
                <span class="option-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>🌿 에센셜 오일
              </button>
            </div>
            <p class="demo-hint">여러 개 선택할 수 있어요. 선택한 성분을 다시 누르면 해제돼요.</p>
          </div>

          <div class="panel" id="resultPanel">
            <span class="eyebrow" id="resultSkinLabel">민감성 피부 맞춤 결과</span>

            <h3 class="result-subhead">조심해야 할 성분 조합</h3>
            <ul id="watchComboList" class="watch-list combo"></ul>

            <h3 class="result-subhead">함께 쓰면 좋은 성분 추천</h3>
            <ul id="recommendList" class="watch-list recommend"></ul>

            <h3 class="result-subhead">기초 케어 순서 추천</h3>
            <ol id="routineList" class="routine-list"></ol>
          </div>
        </div>
      </div>
    </section>

    <section id="ingredient-db">
      <svg class="section-deco" viewBox="0 0 200 200" aria-hidden="true">
        <path d="M85 20h30 M95 20v42l-38 78a11 11 0 0 0 10 16h66a11 11 0 0 0 10-16l-38-78V20" />
        <path d="M60 118h80" />
        <path d="M108 55c17-12 34 0 28 17s-28 11-28-6" />
      </svg>
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">성분 데이터베이스</span>
          <h2>이런 성분들을 데이터베이스로 관리하고 있어요</h2>
          <p>자주 등장하는 주의 성분을 우려 유형과 함께 정리해, 스캔·가이드 판정의 기준으로 사용해요.</p>
        </div>
        <ul class="ingdb-grid">
          <li class="ingdb-card">
            <span class="ingdb-tag">알레르기·자극 유발</span>
            <h3>🌸 향료 (Fragrance/Parfum)</h3>
            <p>화장품에서 가장 흔한 알레르기 유발 성분으로, 접촉성 피부염 사례가 많아 민감성·트러블 피부는 무향 제품을 우선 고려하는 게 좋아요.</p>
          </li>
          <li class="ingdb-card">
            <span class="ingdb-tag">건조·자극 유발</span>
            <h3>🧪 변성알코올 (Alcohol Denat.)</h3>
            <p>휘발성이 강해 사용감은 산뜻하지만 피지막을 과도하게 제거해 건성·민감성 피부에 당김과 따가움을 유발할 수 있어요.</p>
          </li>
          <li class="ingdb-card">
            <span class="ingdb-tag">자극·장벽 손상</span>
            <h3>🫧 소듐라우릴설페이트 (SLS)</h3>
            <p>세정력이 매우 강한 계면활성제로, 피부 장벽의 지질까지 씻어내 건조와 자극을 일으키기 쉬워요.</p>
          </li>
          <li class="ingdb-card">
            <span class="ingdb-tag">방부제 · 고농도 시 자극</span>
            <h3>🧴 페녹시에탄올 (Phenoxyethanol)</h3>
            <p>널리 쓰이는 방부제지만 고농도로 배합되면 민감성 피부에서 따가움이나 붉어짐을 유발할 수 있어요.</p>
          </li>
          <li class="ingdb-card">
            <span class="ingdb-tag">알레르기·접촉성 피부염</span>
            <h3>🛡️ 메칠이소치아졸리논 (MI)</h3>
            <p>사용 제한이 강화되고 있는 방부제로, 접촉성 피부염 보고 사례가 많아 민감성 피부는 특히 주의가 필요해요.</p>
          </li>
          <li class="ingdb-card">
            <span class="ingdb-tag">모공 막힘 우려</span>
            <h3>✨ 다이메티콘 (Dimethicone)</h3>
            <p>매끄러운 사용감을 주는 실리콘 성분이지만, 두껍게 발리면 피지와 뒤엉켜 지성·트러블 피부에서 모공을 막을 수 있어요.</p>
          </li>
          <li class="ingdb-card">
            <span class="ingdb-tag">모공 막힘 우려</span>
            <h3>🛢️ 미네랄오일 (Mineral Oil)</h3>
            <p>보습 효과는 좋지만 분자가 커 얇은 막을 형성해, 지성 피부에서는 트러블을 유발할 가능성이 있어요.</p>
          </li>
          <li class="ingdb-card">
            <span class="ingdb-tag">자극·광과민성</span>
            <h3>🌙 레티놀 (Retinol)</h3>
            <p>각질 개선에 효과적이지만 자극이 강해 민감성·건성 피부는 저농도로 시작하고 사용 중 자외선 차단이 꼭 필요해요.</p>
          </li>
          <li class="ingdb-card">
            <span class="ingdb-tag">산성 자극</span>
            <h3>🍊 아스코르빅애씨드 (Vitamin C)</h3>
            <p>낮은 pH에서 효능이 높아지는 만큼 자극도 커져, 민감성 피부는 사용 초기 따가움·붉어짐을 느낄 수 있어요.</p>
          </li>
          <li class="ingdb-card">
            <span class="ingdb-tag">건조·자극</span>
            <h3>💥 벤조일퍼옥사이드 (Benzoyl Peroxide)</h3>
            <p>여드름균 억제에 효과적이지만 각질층을 건조시키는 힘이 강해, 건성·민감성 피부는 함께 쓰는 제품 강도 조절이 필요해요.</p>
          </li>
        </ul>
      </div>
    </section>

    <section>
      <div class="cta-band wrap">
        <h2>내 피부에 맞는 성분인지, 사기 전에 먼저 확인하세요</h2>
        <p>회원가입 없이 지금 바로 체험해볼 수 있어요.</p>
        <a class="btn btn-primary" href="#demo">성분노트 시작하기</a>
      </div>
    </section>
  </main>

  <footer class="site">
    © 성분노트 · 서비스 기획 워크시트 기반 프로토타입
  </footer>

<script>
(function () {
  "use strict";

  var COMBO_DB = [
    { a: "레티놀", b: "AHA/BHA", why: "각질 턴오버 자극이 겹쳐 자극 반응이 커질 수 있어요." },
    { a: "레티놀", b: "비타민C", why: "각각 단독으로도 자극적인데, 함께 쓰면 자극이 배가될 수 있어요." },
    { a: "레티놀", b: "벤조일퍼옥사이드", why: "함께 쓰면 서로 효능이 떨어지고 자극이 커질 수 있어요." },
    { a: "AHA/BHA", b: "비타민C", why: "산성 성분이 겹쳐 장벽 자극과 당김이 심해질 수 있어요." },
    { a: "알코올", b: "AHA/BHA", why: "각질 제거와 건조가 겹쳐 자극이 커질 수 있어요." },
    { a: "인공향료", b: "에센셜 오일", why: "휘발성 방향 성분이 중복되며 자극 가능성이 높아져요." }
  ];

  var RECOMMEND = {
    "건성": [
      { name: "🧱 세라마이드", why: "피부 장벽을 채워 수분 손실을 막아줘요." },
      { name: "💧 히알루론산", why: "피부 속까지 수분을 끌어와 촉촉함을 오래 유지해줘요." },
      { name: "🫒 스쿠알란", why: "가볍게 흡수되면서 유수분 밸런스를 잡아줘요." }
    ],
    "지성": [
      { name: "⚖️ 나이아신아마이드", why: "피지 분비를 조절하고 모공을 관리해줘요." },
      { name: "🍋 저농도 살리실산 (BHA)", why: "모공 속 노폐물을 부드럽게 정리해줘요." },
      { name: "🪨 클레이 성분 (카올린 등)", why: "과도한 유분과 노폐물을 흡착해줘요." }
    ],
    "복합성": [
      { name: "🩹 판테놀", why: "부위별로 다른 상태를 진정시키고 밸런스를 잡아줘요." },
      { name: "🍵 녹차 추출물", why: "피지 조절과 진정 효과를 동시에 줘요." },
      { name: "💦 글리세린", why: "부담 없이 수분을 채워 부위별 편차를 줄여줘요." }
    ],
    "민감성": [
      { name: "🩹 판테놀 (비타민B5)", why: "손상된 장벽을 진정시키고 회복을 도와줘요." },
      { name: "🌱 마데카소사이드 (병풀 추출물)", why: "자극받은 피부를 진정시키는 대표 성분이에요." },
      { name: "🌵 알로에베라 추출물", why: "저자극으로 수분과 진정 효과를 함께 줘요." }
    ]
  };

  var ROUTINE = {
    "건성": [
      { step: "클렌징", form: "저자극 크림·밀크 클렌저" },
      { step: "토너", form: "고보습 로션 타입 토너" },
      { step: "세럼 · 크림", form: "고영양 크림·밤 제형" },
      { step: "마무리", form: "오일로 유분 마무리 + 로션 타입 선크림" }
    ],
    "지성": [
      { step: "클렌징", form: "폼·젤 클렌저" },
      { step: "토너", form: "산뜻한 워터리 토너" },
      { step: "세럼", form: "가벼운 젤·워터리 세럼" },
      { step: "마무리", form: "가벼운 젤 로션 + 매트 선크림" }
    ],
    "복합성": [
      { step: "클렌징", form: "약산성 폼 클렌저" },
      { step: "토너", form: "밸런싱 워터리 토너" },
      { step: "세럼", form: "가벼운 워터리 세럼" },
      { step: "마무리", form: "부위별로 다른 두께의 로션·크림 + 선크림" }
    ],
    "민감성": [
      { step: "클렌징", form: "무향 저자극 밀크 클렌저" },
      { step: "토너", form: "무알코올 진정 토너" },
      { step: "세럼", form: "저농도 저자극 세럼" },
      { step: "마무리", form: "순한 크림 + 무기자차 선크림" }
    ]
  };

  var selectedSkin = "민감성";
  var selectedIngredients = new Set(["인공향료", "레티놀"]);

  var skinRow = document.getElementById("skinTypeRow");
  var ingredientToggle = document.getElementById("ingredientToggle");
  var ingredientToggleLabel = document.getElementById("ingredientToggleLabel");
  var ingredientPanel = document.getElementById("ingredientPanel");
  var resultSkinLabel = document.getElementById("resultSkinLabel");
  var watchComboList = document.getElementById("watchComboList");
  var recommendList = document.getElementById("recommendList");
  var routineList = document.getElementById("routineList");

  var ICON_AVOID = '<svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg>';
  var ICON_SAFE = '<svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg>';

  var ING_EMOJI = {
    "알코올": "🧪", "인공향료": "🌸", "파라벤": "🧫", "실리콘": "✨", "특정 방부제": "🛡️",
    "레티놀": "🌙", "비타민C": "🍊", "AHA/BHA": "🍋", "벤조일퍼옥사이드": "💥", "에센셜 오일": "🌿"
  };
  function withEmoji(name) {
    return (ING_EMOJI[name] || "") + " " + name;
  }

  function updateToggleLabel() {
    ingredientToggleLabel.textContent = selectedIngredients.size
      ? Array.from(selectedIngredients).map(withEmoji).join(", ") + " 선택됨"
      : "성분을 선택해주세요";
  }

  function renderCombos() {
    var matches = COMBO_DB.filter(function (c) {
      return selectedIngredients.has(c.a) || selectedIngredients.has(c.b);
    });

    if (!matches.length) {
      watchComboList.innerHTML = '<li class="watch-empty">선택한 성분과 관련된 주의 조합이 없어요. 다른 성분도 선택해보세요.</li>';
      return;
    }

    watchComboList.innerHTML = matches.map(function (c) {
      var bothSelected = selectedIngredients.has(c.a) && selectedIngredients.has(c.b);
      var note = bothSelected
        ? "두 성분을 모두 선택하셨어요 — "
        : "'" + (selectedIngredients.has(c.a) ? c.a : c.b) + "'를 선택하셨네요 — ";
      return (
        '<li class="watch-item">' +
          '<span class="watch-icon">' + ICON_AVOID + '</span>' +
          '<div class="watch-body"><div class="watch-name">' + withEmoji(c.a) + ' + ' + withEmoji(c.b) + '</div><div class="watch-why">' + note + c.why + '</div></div>' +
        '</li>'
      );
    }).join("");
  }

  function renderRecommend() {
    resultSkinLabel.textContent = selectedSkin + " 피부 맞춤 결과";
    recommendList.innerHTML = RECOMMEND[selectedSkin].map(function (r) {
      return (
        '<li class="watch-item">' +
          '<span class="watch-icon">' + ICON_SAFE + '</span>' +
          '<div class="watch-body"><div class="watch-name">' + r.name + '</div><div class="watch-why">' + r.why + '</div></div>' +
        '</li>'
      );
    }).join("");
  }

  function renderRoutine() {
    routineList.innerHTML = ROUTINE[selectedSkin].map(function (r, i) {
      return (
        '<li class="routine-step">' +
          '<span class="routine-num">' + (i + 1) + '</span>' +
          '<div class="watch-body"><div class="watch-name">' + r.step + '</div><div class="watch-why">' + r.form + '</div></div>' +
        '</li>'
      );
    }).join("");
  }

  skinRow.addEventListener("click", function (e) {
    var btn = e.target.closest("button[data-skin]");
    if (!btn) return;
    skinRow.querySelectorAll(".pill").forEach(function (p) { p.classList.remove("is-active"); });
    btn.classList.add("is-active");
    selectedSkin = btn.dataset.skin;
    renderRecommend();
    renderRoutine();
  });

  ingredientToggle.addEventListener("click", function () {
    var expanded = ingredientToggle.getAttribute("aria-expanded") === "true";
    ingredientToggle.setAttribute("aria-expanded", String(!expanded));
    ingredientPanel.hidden = expanded;
  });

  ingredientPanel.addEventListener("click", function (e) {
    var btn = e.target.closest("button[data-ing]");
    if (!btn) return;
    var ing = btn.dataset.ing;
    if (selectedIngredients.has(ing)) {
      selectedIngredients.delete(ing);
      btn.classList.remove("is-active");
    } else {
      selectedIngredients.add(ing);
      btn.classList.add("is-active");
    }
    updateToggleLabel();
    renderCombos();
  });

  ingredientPanel.querySelectorAll("button[data-ing]").forEach(function (btn) {
    if (selectedIngredients.has(btn.dataset.ing)) btn.classList.add("is-active");
  });

  updateToggleLabel();
  renderCombos();
  renderRecommend();
  renderRoutine();
})();
</script>
</body>
</html>"""

components.html(HTML_SOURCE, height=6800, scrolling=True)
