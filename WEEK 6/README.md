# 🌍 Ubuntu Image Fetcher  

> *"I am because we are."* — Ubuntu Philosophy  

Welcome to the **Ubuntu Image Fetcher**, a mindful tool for connecting with the web community, respectfully fetching shared images, and organizing them for later appreciation.  

This project is inspired by **Ubuntu principles** of **community, respect, sharing, and practicality**.  

---

## ✨ Features  

- 📥 Download images from **one or multiple URLs**  
- 📂 Saves images in an organized directory: `Fetched_Images/`  
- ✅ Verifies that downloads are **valid images** before saving  
- 🔄 Prevents duplicate downloads using **file hash comparison**  
- ⚡ Gracefully handles errors and timeouts without crashing  
- 🌐 Uses respectful HTTP requests with a custom `User-Agent`  

---

## 🚀 Getting Started  

### 1. Clone this repository  
git clone https://github.com/YOUR_USERNAME/Ubuntu_Requests.git
cd Ubuntu_Requests

### 2. Install dependencies

This project uses the requests library. Install it with:

pip install requests

### 3. Run the program
python ubuntu_fetcher.py

---

#### 💻 Example Usage

##### Terminal Output:

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter image URLs (comma-separated): https://example.com/ubuntu.jpg, https://example.com/logo.png
✓ Successfully fetched: ubuntu.jpg
✓ Successfully fetched: logo.png

--- 

###### Connection strengthened. Community enriched.

#### Saved files:

Fetched_Images/
 ├── ubuntu.jpg
 └── logo.png

## 🔍 Challenge Features Implemented

✅ Multiple URL support (comma-separated input)

✅ Safety precautions (check Content-Type, set User-Agent, handle timeouts)

✅ Duplicate prevention (MD5 hash comparison)

✅ HTTP headers checked (Content-Type, optionally Content-Length)

---

## 🛡️ Precautions

When downloading images from unknown sources, this program:

Ensures the content is actually an image file

Uses timeouts to prevent hanging requests

Avoids duplicates to save storage space

---

## 🌱 Ubuntu Principles

Community → Connects with the global internet to fetch shared resources

Respect → Handles errors gracefully and responsibly

Sharing → Organizes images for later reuse and appreciation

Practicality → Provides a useful everyday tool

"A person is a person through other persons."
Your images exist because someone shared them. This tool brings them into your community respectfully.

## 📜 License

This project is licensed under the MIT License.
You are free to use, adapt, and share — in the spirit of Ubuntu.

✨ Connection strengthened. Community enriched. ✨

---