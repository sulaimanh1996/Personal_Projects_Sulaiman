# 🎯 PLAYWRIGHT ELEMENT SELECTORS & INTERACTION REFERENCE
Copy-paste templates for all element interactions

## 🔍 **LOCATOR REFERENCE GUIDE**

### **📌 COPY-PASTE TEMPLATES**

#### **ID SELECTOR**
```python
# Single element by ID
self.page.locator("#(FILL_ID_HERE)").click()
# Example: self.page.locator("#submit-button").click()
```

#### **CLASS SELECTOR (Single Class)**
```python
# Single class
self.page.locator(".(FILL_CLASS_NAME_HERE)").click()
# Example: self.page.locator(".btn-primary").click()
```

#### **CLASS SELECTOR (Multiple Classes)**
```python
# Multiple classes (no spaces between dots)
self.page.locator(".(FILL_CLASS1).(FILL_CLASS2).(FILL_CLASS3)").click()
# Example: self.page.locator(".btn.btn-primary.btn-large").click()
```

#### **CLASS ATTRIBUTE (Exact Match)**
```python
# Exact class string match
self.page.locator("[class=\"(FILL_EXACT_CLASS_STRING_HERE)\"]").click()
# Example: self.page.locator("[class=\"btn btn_primary btn_small btn_inventory\"]").click()
```

#### **DATA-TEST ATTRIBUTE**
```python
# Data-test attribute (most reliable for testing)
self.page.locator("[data-test=\"(FILL_DATA_TEST_VALUE_HERE)\"]").click()
# Example: self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
```

#### **NAME ATTRIBUTE**
```python
# Name attribute (forms)
self.page.locator("[name=\"(FILL_NAME_HERE)\"]").click()
# Example: self.page.locator("[name=\"username\"]").fill("my_user")
```

#### **TEXT CONTENT**
```python
# Click by visible text
self.page.locator("text=(FILL_TEXT_HERE)").click()
# Example: self.page.locator("text=Add to Cart").click()
```

#### **PLACEHOLDER ATTRIBUTE**
```python
# Placeholder text (input fields)
self.page.locator("[placeholder=\"(FILL_PLACEHOLDER_HERE)\"]").click()
# Example: self.page.locator("[placeholder=\"Enter username\"]").fill("user123")
```

#### **ROLE SELECTOR (Accessibility)**
```python
# By role and name (best practice)
self.page.locator("role=(FILL_ROLE_HERE)[name=\"(FILL_NAME_HERE)\"]").click()
# Example: self.page.locator("role=button[name=\"Submit\"]").click()
```

#### **XPATH SELECTOR**
```python
# XPath expressions
self.page.locator("xpath=//(FILL_XPATH_HERE)").click()
# Example: self.page.locator("xpath=//button[@id='submit']").click()
```

#### **CSS SELECTOR (Advanced)**
```python
# Custom CSS selectors
self.page.locator("(FILL_CSS_SELECTOR_HERE)").click()
# Example: self.page.locator("button[type='submit']").click()
```

#### **CONTAINS ATTRIBUTE**
```python
# Partial attribute match
self.page.locator("[attribute*=\"(FILL_PARTIAL_VALUE_HERE)\"]").click()
# Example: self.page.locator("[class*=\"btn-primary\"]").click()
```

#### **NTH ELEMENT**
```python
# Select specific occurrence (0-based index)
self.page.locator("(FILL_SELECTOR_HERE)").nth((FILL_INDEX_HERE)).click()
# Example: self.page.locator(".button").nth(1).click()  # Second button
```

## 🧭 **INTERACTION METHODS**

### **📱 CLICK ACTIONS**
```python
# Basic click
self.page.locator("(SELECTOR)").click()

# Click with options
self.page.locator("(SELECTOR)").click(button="right")      # Right click
self.page.locator("(SELECTOR)").click(modifiers=["Shift"]) # Shift+click
self.page.locator("(SELECTOR)").click(force=True)          # Force click
```

### **⌨️ INPUT ACTIONS**
```python
# Fill input field
self.page.locator("(SELECTOR)").fill("(FILL_TEXT_HERE)")

# Clear and fill
self.page.locator("(SELECTOR)").clear()
self.page.locator("(SELECTOR)").fill("(FILL_TEXT_HERE)")

# Press keys
self.page.locator("(SELECTOR)").press("Enter")
self.page.locator("(SELECTOR)").press("Tab")
self.page.locator("(SELECTOR)").press("Escape")
```

### **☑️ FORM ACTIONS**
```python
# Checkbox
self.page.locator("(SELECTOR)").check()                    # Check
self.page.locator("(SELECTOR)").uncheck()                  # Uncheck

# Dropdown selection
self.page.locator("(SELECTOR)").select_option("(VALUE)")   # By value
self.page.locator("(SELECTOR)").select_option(label="(TEXT)")  # By text

# File upload
self.page.locator("(SELECTOR)").set_input_files("path/to/file.jpg")
```

### **🖱️ MOUSE ACTIONS**
```python
# Hover
self.page.locator("(SELECTOR)").hover()

# Drag and drop
self.page.locator("(SOURCE_SELECTOR)").drag_to(self.page.locator("(TARGET_SELECTOR)"))

# Double click
self.page.locator("(SELECTOR)").dblclick()
```

## ⏱️ **WAITING & VALIDATION**

### **⏳ WAIT METHODS**
```python
# Wait for element
self.page.locator("(SELECTOR)").wait_for()

# Wait for element state
self.page.locator("(SELECTOR)").wait_for(state="visible")
self.page.locator("(SELECTOR)").wait_for(state="hidden")
self.page.locator("(SELECTOR)").wait_for(state="attached")

# Wait with timeout
self.page.locator("(SELECTOR)").wait_for(timeout=5000)  # 5 seconds
```

### **✅ VALIDATION METHODS**
```python
# Check if element exists/visible
if self.page.locator("(SELECTOR)").is_visible():
    print("✅ Element found")

# Get text content
text = self.page.locator("(SELECTOR)").text_content()
print(f"Text: {text}")

# Get attribute value
value = self.page.locator("(SELECTOR)").get_attribute("class")

# Count elements
count = self.page.locator("(SELECTOR)").count()
```

## 🎯 **REAL-WORLD EXAMPLES FROM PROJECT_02**

### **🔐 Login Examples**
```python
# Fill username
self.page.locator("[id='user-name']").fill("standard_user")

# Fill password  
self.page.locator("[id='password']").fill("secret_sauce")

# Click login button
self.page.locator("[id='login-button']").click()
```

### **🛒 Product Examples**
```python
# Add product to cart
self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

# Remove from cart
self.page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
```

### **🍔 Navigation Examples**
```python
# Open hamburger menu
self.page.locator("role=button[name=\"Open Menu\"]").click()

# Click logout
self.page.locator("role=link[name=\"Logout\"]").click()
```

## 💡 **BEST PRACTICES**

### **🎯 Selector Priority (Most Reliable → Least Reliable)**
1. **`data-test` attributes** - Most stable for testing
2. **`id` attributes** - Usually unique and stable  
3. **`role` selectors** - Accessibility-friendly
4. **`name` attributes** - Good for forms
5. **`class` selectors** - Can change with styling
6. **Text content** - Can change with translations
7. **XPath** - Fragile, avoid if possible

### **🔧 Tips**
- **Always prefer `data-test`** attributes when available
- **Use `role` selectors** for accessibility compliance
- **Avoid complex XPath** - they break easily
- **Test selectors in browser console** before using
- **Keep selectors simple** and readable

## 🆘 **TROUBLESHOOTING**

### **Common Issues:**
```python
# Element not found
# ❌ self.page.locator("#nonexistent").click()
# ✅ self.page.locator("#existing").wait_for().click()

# Multiple elements found
# ❌ self.page.locator(".button").click()  # Clicks first
# ✅ self.page.locator(".button").nth(1).click()  # Specific one

# Element not clickable
# ❌ self.page.locator("#hidden").click()
# ✅ self.page.locator("#hidden").wait_for(state="visible").click()
```