# 🚀 AI LinkedIn Auto Job Applier (Customized)

## 📌 Overview
This project is a customized and enhanced version of an open-source LinkedIn Auto Job Applier bot. It automates job applications on LinkedIn while introducing intelligent resume selection, modular architecture, and improved execution stability.

The system is specifically designed for data and AI-related roles, focusing on efficiency, personalization, and real-world usability.

---

## 🙏 Credits
This project is originally inspired by an open-source LinkedIn job applier bot. Initial credit goes to the original author https://github.com/GodsScion/Auto_job_applier_linkedIn.git for the base implementation.

This version has been significantly modified, extended, and restructured with new features, improved stability, and personalized functionality.

---

## 👨‍💻 My Contributions

### 🔥 Major Enhancements

- **Multi-Resume Selection System (Core Feature)**
  - Automatically selects the most relevant resume based on:
    - Job Title
    - Keywords in Job Description
  - Falls back to a default resume if no match is found

- **Role-Specific Personalization**
  - This system supports only:
    - Data Scientist  
    - Data Analyst/Business Analyst  
    - AI Engineer  
    - ML Engineer
    - Default (generalised role)
      
- **Modular Code Architecture**
  - Clean separation of modules for scalability

- **Cleaner Execution**
  - Removed unnecessary popups and logs

- **Stability Fixes**
  - Fixed Selenium/browser issues
  - Removed unstable configurations

---

## 🧠 Resume Selection System

The system maps job roles to resumes using keyword-based matching.

### 📂 Folder Structure
```
all_resumes/
├── default/
├── data_analyst/
├── data_scientist/
├── ml_engineer/
├── ai_engineer/
```

### ⚙️ How It Works
1. Extract job title and description  
2. Match keywords with predefined roles  
3. Select corresponding resume  
4. Fallback to default if no match  

---

## 📤 Resume Upload Instructions

- Place resumes inside `all_resumes/` folders  
- Use one resume per folder (recommended)  
- Use `.pdf` format  

Example:
```
all_resumes/data_scientist/resume.pdf
```

---

## 📁 Creating the Resume Folder (Important)

The `all_resumes/` folder is **not included in the original repository** and must be created manually after cloning.

### Steps:

1. Create the main folder:
```
all_resumes/
```

2. Create the required subfolders:
```
all_resumes/default/
all_resumes/data_analyst/
all_resumes/data_scientist/
all_resumes/ml_engineer/
all_resumes/ai_engineer/
```

3. Add your resumes into the respective folders as per role.

---
### ⚠️ Make sure that all the resumes that are uploaded into the above subfolders (even if they are all made for different roles) are all named as "resume.pdf" as the system identifies the relevant resume based on the parent subfolder name and not the specific resume name.

> Note:  
> Other folders like `logs/` or Excel-related folders may be created automatically during runtime, but the `all_resumes/` folder must be set up manually before running the bot.

---

## 🌐 Browser Configuration

### ✅ Default: Brave Browser
This project is configured specifically for **Brave Browser**.

---

### 🔄 Using Other Browsers (Chrome / Edge)

1. Open `modules/open_chrome.py`  
2. Modify binary location  

For Chrome:
```python
options.binary_location = "path_to_chrome.exe"
```

For Edge:
```python
options.binary_location = "path_to_edge.exe"
```

3. Install correct WebDriver:
   - Chrome → ChromeDriver  
   - Edge → EdgeDriver  

4. Update driver paths if needed  

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd Auto_job_applier
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure
- Add LinkedIn credentials  
- Set job preferences  
- Verify resume folders  

### 4. Run
```bash
python runAiBot.py
```

---

## 📁 Project Structure

```
AUTO_JOB_APPLIER_LINKEDIN-MAIN/
│
├── all_resumes/                    # User-created folder (must be added manually)
│   ├── default/                    # Fallback resume
│   ├── data_analyst/               # Data Analyst resumes
│   ├── data_scientist/             # Data Scientist resumes
│   ├── ml_engineer/                # ML Engineer resumes
│   ├── ai_engineer/                # AI Engineer resumes
│
├── all_excels/                     # Stores job/application data including applied and failed applications(auto-created)
├── logs/                           # Runtime logs (auto-created)
|
├── config/                         # Configuration & customization layer
│   ├── personals.py                # User-specific details (name, email, phone, etc.)
│   ├── questions.py                # Predefined answers for application form questions
│   ├── resume_map.py               # Mapping logic between job roles and resume folders
│   ├── resume.py                   # Resume handling (selection, validation, upload support)
│   ├── search.py                   # Job search filters (roles, keywords, locations)
│   ├── secrets.py                  # Sensitive credentials (login info, API keys) ⚠️ (should not be pushed publicly)
│   ├── settings.py                 # General bot configuration (timeouts, limits, toggles)
│
├── modules/                        # Core automation and logic layer
│   ├── resume_selector.py          # Selects best resume based on job role/keywords
│   ├── clickers_and_finders.py     # Handles Selenium interactions (clicks, inputs, navigation)
│   ├── open_chrome.py              # Browser initialization and driver configuration
│   ├── helpers.py                  # Utility/helper functions used across modules
│   ├── validator.py                # Validates job/application conditions before applying
│
│   ├── resumes/                    # Resume processing sub-module
│   │   ├── extractor.py            # Extracts data/content from resumes
│   │   └── generator.py            # (Optional) Resume generation/formatting logic
│
│   ├── ai/                         # AI integration layer (optional/extendable)
│   │   ├── openaiConnections.py    # OpenAI API integration
│   │   ├── geminiConnections.py    # Gemini API integration
│   │   ├── deepseekConnections.py  # DeepSeek API integration
│   │   └── prompts.py              # Prompt templates for AI interactions
│
│   ├── images/                     # UI reference assets for automation
│   │   └── LinkedIn/
│   │       ├── EasyApplyButton/    # Easy Apply button templates
│   │       └── Logo/               # LinkedIn logo assets
│
│   ├── javascript/                 # Browser automation scripts
│   │   └── unfollow_companies.js   # Script to unfollow companies (utility feature)
│
├── setup/                          # Environment/setup scripts
│   ├── setup.sh                    # Linux/Mac setup script
│   ├── windows-setup.bat           # Windows batch setup
│   └── windows-setup.ps1           # Windows PowerShell setup
│
├── templates/                      # HTML/UI templates (if used)
│   └── index.html
│
├── app.py                          # Optional entry/helper script
├── runAiBot.py                     # Main execution script (primary entry point)
├── chromedriver.exe                # WebDriver (must match browser version)
│
├── .gitignore                      # Git ignore rules
├── LICENSE                         # License file
```

### 📝 Notes

- `all_resumes/` → **Must be created manually by the user before running the bot**
- `logs/` and `all_excels/` → **Automatically generated during runtime**
- `modules/` → Contains the core automation and logic of the system
- `config/` → Stores user-specific configuration (should avoid committing sensitive data)

---

---

## 📊 Key Features

- Automated LinkedIn Job Applications  
- Intelligent Resume Selection Engine  
- Role-Based Resume Management  
- Modular Architecture  
- Fallback Resume Handling  
- Clean Execution  

---

## 🚀 Future Improvements

- AI-based job description parsing  
- Resume scoring system  
- Dashboard for tracking applications  
- Human-like automation behavior  
- Dynamic AI resume generation  

---

## ⚠️ Disclaimer

- For educational and personal use only  
- Use responsibly to avoid violating LinkedIn policies  

---

## 👤 Author

Keerthikrishna Jog  
Computer Science Engineering (AI and Analytics) 
Focus: AI • Data • Automation • Analytics
LinkedIn: www.linkedin.com/in/keerthikrishnajog

---

## 🎯 Goal

To build a real-world automation system that:
- Improves job application efficiency  
- Demonstrates AI-driven decision-making  
- Strengthens portfolio for placements  
