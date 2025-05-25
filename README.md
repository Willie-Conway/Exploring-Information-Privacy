
# 🔐 Exploring Information Privacy — Cybersecurity Project

A comprehensive toolkit implementing modern **information privacy** techniques tailored for cybersecurity analysts and compliance teams.

---

## 🚀 Features

- 📛 **Data Anonymization** — k-anonymity, l-diversity, and t-closeness techniques
- 🔐 **Advanced Encryption** — Homomorphic encryption & differential privacy
- 📊 **Privacy Risk Assessment** — Automated scoring of data exposure
- 📜 **GDPR Compliance Checker** — Article-by-article regulation validation
- 🧠 **PII Detection & Classification** — Sensitive data recognition
- 🌐 **Data Flow Mapping** — Visual diagrams of data movement

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/Willie-Conway/Exploring-Information-Privacy-.git
cd Enformation-Information-Privacy
````

---

## 🧑‍💻 Cybersecurity Skills Demonstrated

* 🛡️ **Data Protection** — Applied anonymization techniques (k-anonymity, l-diversity, t-closeness)
* 🔐 **Encryption Practice** — Built a working homomorphic encryption module
* 📋 **Regulatory Compliance** — Automated GDPR checks across data handling
* 🔎 **Risk Analysis** — PII classification & privacy risk scoring
* 📈 **Communication** — Clear, professional data visualizations for reporting

---

## 🗣️ How to Present This in Interviews

**Highlight technical complexity:**

> “The homomorphic encryption module allows computations directly on encrypted data, preserving confidentiality during processing.”

> “Differential privacy introduces mathematically-backed noise to datasets for secure analysis.”

**Share business value:**

> “The GDPR compliance checker could reduce manual audit time by 20+ hours per cycle.”

> “Our PII detector identifies vulnerable unencrypted fields before exposure occurs.”

**Describe your process:**

> “I used test-driven development for the anonymization logic.”

> “Visualization tools were refined across three iterative feedback rounds.”

---

## 📊 Output Analysis

* ✅ **K-Anonymity**: Achieved generalization up to 2-anonymity
* ✅ **L-Diversity**: Validated 2-diversity presence
* ✅ **Homomorphic Encryption**: Encrypted sum of values (10+20+30), correctly decrypted to `60`
* ✅ **Differential Privacy**: Added controlled noise (e.g., `100 → 104.13`)
* ✅ **Privacy Risk Assessment**: No PII detected in the sample dataset
* ✅ **GDPR Compliance**: Article-wise compliance report with highlights

---

## 📂 Expected Output

Upon running `main.py`, you'll see:

```
=== Exploring Information Privacy ===
Running comprehensive privacy analysis...

📦 Python version: 3.12.x
📁 Working directory: /home/user/Exploring-Information-Privacy
📄 Directory contents: ['main.py', 'data_anonymization', ...]

✅ JSON report saved to: ./reports/privacy_report.json
✅ GDPR heatmap saved to: ./reports/gdpr_compliance.png
✅ Data flow diagram saved to: ./reports/data_flow.png

🎉 Report generation successful!
```

---

## 🌟 Key Enhancements

### 🔍 Visual Output

* GDPR compliance **heatmap** with intuitive coloring
* Network-style **data flow diagram**
* Output saved to `./reports/` directory

### 🧩 Main Script Enhancements

* Modular demo execution
* JSON report generation
* Timestamped logs & error handling
* Cross-platform paths with `pathlib`

### 📦 Production-Ready Improvements

* Type hints for maintainability
* Config file management
* Separation of concerns (execution vs. reporting)
* Rich `docstrings` for all modules

### 👔 Employer-Focused Outputs

* 📸 Visuals (`.png`): compliance, data flow
* 📄 Machine-readable: `privacy_report.json`
* 🖥️ Clear console logs

---

## ⚙️ How to Use

1. Make sure your working directory has `main.py` and required folders
2. Run:

```bash
python main.py
```

3. Check your output directory:

```bash
ls -l reports/
```

Expected files:

* `privacy_report.json`
* `gdpr_compliance.png`
* `data_flow.png`

---

## 🧰 Debugging Tips

If files are missing:

* Check printed paths in console
* Manually test file creation:

```python
with open("test.txt", "w") as f:
    f.write("test")
```

### 🛠️ Common Fixes

* ✅ **Permission Errors**: Uses relative paths inside the project
* ✅ **Cross-Platform Support**: Compatible with Windows, macOS, Linux
* ✅ **Visibility**: Prints absolute paths for quick navigation






