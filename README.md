# 🎭 Task_06_Deep_Fake

**Researcher**: Advait Narvekar  
**Institution**: Syracuse University  
**Reporting Period**: August 2025 – Research Phase 2  
**Project Theme**: Deep Fake in Job Interviews  

---

## 📘 Overview

This repository contains my submission for **Research Task 06: Deep Fake**.  
The goal was to transform a written narrative into an AI-generated “deep fake” interview.  

Due to limitations of free/student tools, producing a video-based deep fake was not feasible. Instead, I created an **audio-based street interview** to simulate realistic dialogue among multiple speakers discussing the risks of deep fakes in the hiring process.  

The deliverable focuses not only on the final audio file but also on documenting the **workflow, design choices, technical challenges, and ethical reflections** that shaped the project.  

---

## 🎯 Objective

The primary goal of this task was to investigate:

**“How can free AI tools, specifically text-to-speech and audio editing, be leveraged to simulate a deep fake interview experience?”**

To achieve this, I focused on the following objectives:  
- 📝 Write a concise but realistic script to represent an interview scenario.  
- 🗣️ Assign distinct synthetic voices to multiple roles using Google Cloud Text-to-Speech (TTS).  
- 🎶 Automate the process of generating clips and stitching them into a final MP3.  
- 🔍 Reflect on the **technical, methodological, and ethical lessons** drawn from the process.  

---

## 🔍 Methodology

### 1. Script Creation
- Developed a short “street interview” scenario featuring four roles:  
  - **Jordan** – interviewer, curious and neutral.  
  - **Alex** – employee perspective, raising concerns.  
  - **Sarah** – hiring manager perspective, focused on process and detection.  
  - **Mark** – security-focused perspective, emphasizing organizational risks.  
- The script was designed to cover **awareness, detection strategies, and security implications** of deep fake candidates.  
- Stored in `src/prompts/street_interview.txt` to ensure clarity and reproducibility.  

### 2. Audio Generation
- Implemented `make_audio.py` to synthesize each line into MP3 format using **Google Cloud TTS**.  
- Mapped neural voices (`Neural2-C`, `Neural2-D`, `Neural2-F`, `Neural2-H`) to characters for distinction.  
- Built **fallback logic** to automatically substitute voices if a preferred one was unavailable, ensuring pipeline stability.  
- Generated **13 individual audio clips**, each corresponding to a script line.  

### 3. Audio Stitching
- Implemented `stitch.py` to concatenate the generated clips into a single continuous interview.  
- Added **600 ms pauses** between each clip to simulate conversational pacing.  
- Exported the final stitched file as `outputs/deepfake_job_interview.mp3`.  

### 4. Repository Structure
- `docs/` — process documentation (assignment .docx ignored in git)  
- `scripts/` — Python scripts (`make_audio.py` and `stitch.py`)  
- `src/prompts/` — plain text script of the interview  
- `data/audio_clips/` — generated per-line MP3s (ignored in git for cleanliness)  
- `outputs/` — final stitched interview file for submission  

---

## ⚙️ Tools & Resources

- **Google Cloud Text-to-Speech (TTS)**  
  - Used to generate synthetic voices with natural tone and clarity.  
  - Explored multiple voices to create distinction between characters.  

- **PyDub**  
  - Python audio library for editing and merging clips.  
  - Allowed insertion of silent pauses for natural pacing.  

- **Python**  
  - Used for automating both the audio generation (`make_audio.py`) and stitching (`stitch.py`).  
  - Ensured reproducibility and minimized manual editing.  

- **GitHub**  
  - Repository created for version control, organization, and submission.  

---

## 📈 Key Results

- ✅ Designed and documented a script representing realistic deep fake interview concerns.  
- ✅ Generated **13 MP3 clips**, each assigned to a distinct speaker voice.  
- ✅ Successfully merged clips into a **single continuous interview MP3**.  
- ✅ Implemented fallback logic to ensure reliable execution despite voice availability issues.  
- ✅ Structured repository for clarity, reproducibility, and submission requirements.  

---

## 🧠 Reflections

### Strengths
- Achieved a convincing interview-style dialogue with free tools.  
- Multiple voices and pause insertions created a natural conversational flow.  
- Modular design ensures that the workflow can be replicated for future experiments.  

### Challenges
- Lack of free video deep fake tools limited the output to audio.  
- Certain neural voices were unavailable, requiring fallback logic.  
- Audio pacing required manual experimentation to feel natural.  

### Ethical Implications
- The project highlights how **accessible synthetic media creation has become**.  
- Demonstrates risks for **remote hiring**, where fraudulent candidates could exploit deep fakes.  
- Underscores the necessity for **verification methods** and deep fake detection tools in professional contexts.  

### Takeaway
The project shows that even with basic, free resources, combining **text-to-speech with lightweight audio editing** can convincingly simulate a deep fake interview. This not only illustrates the creative possibilities of AI but also calls attention to the **serious ethical and security challenges** that accompany such technology.  

---