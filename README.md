# 🎭 Task_06_Deep_Fake

**Researcher**: Advait Narvekar  
**Institution**: Syracuse University  
**Reporting Period**: August 2025 – Research Phase 2  
**Project Theme**: Deep Fake in Job Interviews  

---

## 📘 Overview

This repository documents my work for **Research Task 06: Deep Fake**.  
The task required transforming a narrative into an AI-generated “deep fake” interview, ideally as a video.  
Since high-quality free video-generation tools are limited, I produced an **audio-based street interview** that demonstrates the same concept of simulation and realism.  

The emphasis of this task is not only on the **final artifact** but also on the **workflow and process** — exploring free/student tools, iterating on outputs, and critically reflecting on results.  

---

## 🎯 Objective

The core research question addressed was:

> **“How can AI-driven tools be used to create a simulated deep fake interview, and what are the challenges, limitations, and implications of this process?”**

To answer this, I focused on:
- ✍️ Designing a **scripted narrative** around deep fakes in hiring  
- 🗣️ Generating **realistic character voices** via Google Cloud Text-to-Speech  
- 🎶 Stitching clips into a continuous MP3 interview using PyDub  
- 🔍 Reflecting on **technical barriers, ethical risks, and practical takeaways**  

---

## 🔍 Methodology

1. **Script Development**  
   - Wrote a conversational script featuring four characters:  
     - **Jordan** (interviewer)  
     - **Alex** (casual employee)  
     - **Sarah** (hiring manager)  
     - **Mark** (security-focused perspective)  
   - Script stored in `src/prompts/street_interview.txt` for transparency.  

2. **Audio Generation with Google Cloud TTS**  
   - Used `make_audio.py` to generate individual MP3 clips.  
   - Mapped distinct voices (`Neural2-C, D, F, H`) to characters.  
   - Implemented fallbacks in case a preferred voice was unavailable.  

3. **Audio Stitching with PyDub**  
   - Used `stitch.py` to concatenate all clips into one file.  
   - Added short pauses (600ms) for conversational realism.  
   - Final artifact: `outputs/deepfake_job_interview.mp3`.  

4. **Repository Organization**  
