# 📚 WEEK 6 – Object-Oriented Programming in Python  

This folder contains two Python programs demonstrating key **OOP (Object-Oriented Programming)** concepts: **Inheritance** and **Polymorphism**.  

---

## 📂 Files in This Folder  

1. **`inheritance.py`**  
   - Demonstrates how a child class can inherit attributes and methods from a parent class.  
   - Example: A `GamingSmartphone` inherits from the base `Smartphone` class and adds new behavior.  

2. **`polymorphism.py`**  
   - Demonstrates how different classes can define their own version of a method with the same name.  
   - Example: `Car`, `Plane`, and `Boat` all implement their own version of `move()`.  

---

## 📝 inheritance.py  

### Code Features
- **Base Class:** `Smartphone`  
  - Attributes: `brand`, `model`, `storage`, `battery`  
  - Methods: `call()`, `charge()`, `__str__()`  

- **Inherited Class:** `GamingSmartphone`  
  - Inherits from `Smartphone`  
  - Adds `gpu` attribute  
  - Adds `play_game()` method  

### Example Output
Samsung Galaxy S23 with 256GB storage
Samsung Galaxy S23 is calling 123-456-789...
Battery charged to 100%
Asus ROG Phone 6 with 512GB storage
Playing Genshin Impact on Asus ROG Phone 6 with Adreno 730 GPU 🎮

---

## 📝 polymorphism.py  

### Code Features
- **Base Class:** `Vehicle`  
  - Method: `move()`  

- **Child Classes:**  
  - `Car` → `move()` prints `"Driving 🚗"`  
  - `Plane` → `move()` prints `"Flying ✈️"`  
  - `Boat` → `move()` prints `"Sailing 🚤"`  

### Example Output
Driving 🚗
Flying ✈️
Sailing 🚤

---

## ▶️ How to Run  

Open your terminal or command prompt, navigate to the **WEEK 6** folder, then run:  

cd "C:\Users\Admin\Desktop\PYTHON PROGRAMMING\WEEK 6"

# Run inheritance example
python inheritance.py

# Run polymorphism example
python polymorphism.py
🌱 Concepts Learned
Inheritance: Code reuse and extending functionality of base classes.

Polymorphism: Different objects can respond differently to the same method call.

✨ These examples bring the power of Object-Oriented Programming to life in Python!

---
