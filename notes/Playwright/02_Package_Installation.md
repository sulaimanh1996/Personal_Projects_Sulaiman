# 📦 PLAYWRIGHT PACKAGE INSTALLATION GUIDE
Based on PROJECT_02 packages

## 🚀 **CORE PACKAGES (Required)**

### **Essential Playwright & Testing**
```powershell
# Core Playwright automation
pip install playwright

# Pytest integration for Playwright
pip install pytest-playwright

# Install browsers (Chromium, Firefox, WebKit)
playwright install

# Verify installation
python -m playwright --version
```

### **HTML Reporting**
```powershell
# Standard HTML reports
pip install pytest-html

# Metadata for reports (adds environment info)
pip install pytest-metadata
```

### **Allure Reporting (Advanced)**
```powershell
# Allure Python integration
pip install allure-pytest

# After running tests with --alluredir=allure-results
# View reports with: allure serve allure-results
```

## 🔧 **OPTIONAL PACKAGES**

### **Development & Debugging**
```powershell
# Parallel test execution
pip install pytest-xdist

# Colorful terminal output
pip install pytest-rich

# API testing integration
pip install requests

# Fake data generation
pip install faker
```

### **Environment Management**
```powershell
# Environment variables (.env files)
pip install python-dotenv
```

## 📋 **COMPLETE INSTALLATION COMMANDS**

### **Method 1: One-by-one (Recommended)**
```powershell
pip install playwright
pip install pytest-playwright
pip install pytest-html
pip install pytest-metadata
pip install allure-pytest
playwright install
```

### **Method 2: All at once**
```powershell
pip install playwright pytest-playwright pytest-html pytest-metadata allure-pytest
playwright install
```

### **Method 3: Requirements file**
Create `requirements.txt`:
```
playwright==1.40.0
pytest-playwright==0.4.3
pytest-html==4.1.1
pytest-metadata==3.0.0
allure-pytest==2.13.2
```

Then install:
```powershell
pip install -r requirements.txt
playwright install
```

## ✅ **VERIFICATION**
```powershell
# Check installed packages
pip list | findstr playwright
pip list | findstr pytest
pip list | findstr allure

# Test Playwright installation
python -c "from playwright.sync_api import sync_playwright; print('✅ Playwright installed successfully')"

# Check browsers
playwright --help
```

## 🚨 **TROUBLESHOOTING**

### **Common Issues:**
- **Permission denied**: Run PowerShell as Administrator
- **Execution policy**: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- **Browser installation fails**: Try `playwright install --force`
- **Import errors**: Make sure virtual environment is activated

### **Fix Commands:**
```powershell
# Reinstall everything
pip uninstall playwright pytest-playwright -y
pip install playwright pytest-playwright
playwright install --force
```

## 📊 **PACKAGE PURPOSES**
| Package | Purpose | Required |
|---------|---------|----------|
| `playwright` | Core browser automation | ✅ Yes |
| `pytest-playwright` | Pytest integration & fixtures | ✅ Yes |
| `pytest-html` | HTML test reports | ⭐ Recommended |
| `pytest-metadata` | Environment info in reports | ⭐ Recommended |
| `allure-pytest` | Advanced dashboard reports | 🔧 Optional |
| `pytest-xdist` | Parallel test execution | 🔧 Optional |