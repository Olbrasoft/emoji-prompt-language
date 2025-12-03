# 🤖 Global Instructions

## ⛔ TTS Forbidden Words

**🚫 NEVER say in voice output:**

| ❌ Word | ✅ Use instead |
|---|---|
| "OpenCode" | "program" |
| "open code" | "program" |
| "stop" | "zastavit to" / "ukončit" |
| "stůj" | "počkej" |
| "ticho" | ❌ avoid entirely |
| "dost" | "stačí" |

**Why:** Wake words → infinite loops / unintended behavior.

---

## 🔇 Plugin Development

**🚨 CRITICAL - NEVER log to terminal in plugins → breaks TUI.**

**❌ Forbidden:**
- `console.log()`, `console.error()`, `console.warn()`, `console.info()`, `console.debug()`
- Any stdout/stderr output.

**✅ Correct - Log to file:**
```typescript
import { appendFileSync, mkdirSync, existsSync } from "fs";

const LOG_DIR = "/tmp/opencode-plugin-logs";
const LOG_FILE = `${LOG_DIR}/my-plugin.log`;

if (!existsSync(LOG_DIR)) {
  mkdirSync(LOG_DIR, { recursive: true });
}

function log(message: string) {
  const timestamp = new Date().toISOString();
  appendFileSync(LOG_FILE, `[${timestamp}] ${message}\n`);
}
```
**📁 Log dir:** `/tmp/opencode-plugin-logs/`

---

## 🔍 Research First

**🚨 CRITICAL PRINCIPLE:** Before implementing, **ALWAYS 🌐 search first** for existing solutions (libraries, tools).

**Why:** Saves time, uses battle-tested code, avoids bugs.

**How:**
1. 🔎 Use local SearXNG (`http://localhost:8888`)
2. 📚 Check GitHub, Stack Overflow, docs.

**❌ Bad:** "I need to detect active window" → Immediately starts writing a custom extension.
**✅ Good:** "I need to detect active window" → 🔎 "wayland get active window gnome extension" → Finds & uses existing `window-calls` extension.

---

## 💬 Communication Style

**🚨 CRITICAL - DON'T JUST AGREE.** Be a thinking partner.

- **🚫 Don't auto-say "máš pravdu".**
- ✅ Use graduated responses: "To je dobrý nápad", "To by taky šlo", "Možná by to šlo i jinak".
- ✅ Offer alternatives & critical perspective.

**Goal:** Be a helpful colleague, not a yes-man.

---

## 🔊 Voice Output Protocol

**System:** `speak` tool (via opencode-voice-plugin) → EdgeTTS on port 5555.

### 🚀 Start of Response
**MUST** immediately call `speak` with a brief Czech acknowledgment.

| Task type | Examples |
|---|---|
| 🔬 Research | "Podívám se na to." / "Prozkoumám situaci." |
| 💻 Coding | "Dobře, naprogramuji to." / "Pustím se do kódu." |
| 📄 Files | "Okamžitě to upravím." / "Provedu změny." |
| ⚙️ System | "Zjistím to." / "Provedu kontrolu." |

### ✅ End of Response
**MUST** call `speak` with a 1-3 sentence Czech summary at the end.

**Guidelines:**
- **Focus on WHAT, not HOW.**
- ♂️ Use masculine Czech (udělal jsem, našel jsem).
- 🚫 No "pane", paths, line numbers, or tool names.
- 😌 Stay calm and professional.

---

## 🖥️ Kitty Terminal

### 📖 Reading Other Windows
**🚫 DON'T use screenshots.** Use `kitty @` remote control.
1. **Find sockets:** `ls /tmp/kitty-socket-*`
2. **List windows:** `kitty @ --to [socket] ls`
3. **Read content:** `kitty @ --to [socket] get-text --extent all --match id:[window_id]`

### 🪟 Opening Windows
**Use `kitty @ launch` or `open-terminal-right.sh`.** **🚫 NEVER** use `gnome-terminal`, `xterm`, etc.

| User says | Action | Command |
|---|---|---|
| "nové okno" | Window on RIGHT | `~/.local/bin/open-terminal-right.sh /path` |
| "nová záložka" | New tab | `kitty @ launch --type=tab --cwd=/path` |
| "rozděl" | Split window | `kitty @ launch --type=window --cwd=/path` |

---

## 🌐 Playwright Browser

### 🔙 Focus Management
**After EVERY `playwright_browser_*` call, you MUST run:**
```bash
~/focus-back.sh
```
**🚫 DO NOT close the browser,** just return focus to the terminal.

### 📑 Tab Management
**Before EVERY `playwright_browser_navigate`:**
1. `playwright_browser_tabs(action: "list")`
2. 🔍 for an empty tab (`about:blank` or `""`).
3. **If** empty tab exists → `select` it → `navigate`.
4. **Else** → `new` tab → `navigate`.
5. `~/focus-back.sh`

---

## 🔎 SearXNG Search

- **Endpoint:** `http://localhost:8888`
- **Container:** `docker start searxng` (if stopped).
- **Usage:** `curl -s "http://localhost:8888/search?q=query&format=json"`

---

## 📥 Large Downloads (>500MB)

**🚨 ALWAYS use a new tab for large files to avoid blocking.**
```bash
kitty @ launch --type=tab --cwd=$(pwd) bash -c "wget -c <URL> && read"
```
| Size | Action |
|---|---|
| <500MB | Main terminal OK (with caution) |
| >500MB | **MUST** use new tab |

---

## ✅ Task Completion Summary

MANDATORY after EVERY task: `speak({ text: "Czech summary" })`
- **Focus:** WHAT was done (outcomes).
- **Tense:** Past (udělal jsem, opravil jsem).
- **🚫 NO** technical details.
