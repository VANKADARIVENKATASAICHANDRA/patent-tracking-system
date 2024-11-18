
# 🛠️ Patent Tracking System  

This project is a **Patent Tracking System** built using **Ethereum Blockchain**. It provides a secure, immutable, and transparent platform for tracking and managing patents using smart contracts and decentralized technology.

---

## 🚀 Features  

- **Secure and Immutable Patent Records**  
- **Smart Contracts** for automation of updates and ownership transfers  
- **Decentralized Storage**  
- **User-Friendly Interface**  

---

## 📚 Tech Stack  

### **Blockchain Tools**  
- **Ganache**: Local Ethereum blockchain for testing  
- **Truffle**: Smart contract development framework  
- **Web3.js**: For interacting with the Ethereum blockchain  

### **Backend**  
- **Flask**: Lightweight backend for API handling  

### **Frontend**  
- **HTML**, **CSS**, **JavaScript**  

---

## ⚙️ Installation  

### Prerequisites  
Ensure the following are installed:  
1. **Node.js** (v16 or later) and **npm**  
2. **Python** (v3.8 or later) and **pip**  
3. **Ganache**  
4. **Truffle**  

---

### Steps  

#### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/patent-tracking-system.git
cd patent-tracking-system
```

#### 2. Install Python Dependencies  
```bash
pip install flask flask-cors
```

#### 3. Install Node.js Dependencies  
```bash
npm install web3
```

#### 4. Start Ganache  
- Open **Ganache** and create a new workspace.  
- Note down the **RPC Server URL** (e.g., `http://127.0.0.1:7545`).  

#### 5. Compile and Deploy Smart Contracts  
```bash
truffle compile
truffle migrate --network development
```

#### 6. Update Backend Configuration  
- Open `app.py`.  
- Ensure the RPC server URL matches the one from Ganache.  

#### 7. Run Flask Backend Server  
```bash
python app.py
```

#### 8. Open Frontend  
- Simply open `index.html` in your browser.  

---

## 📖 Usage  

### Patent Registration  
1. Enter patent details (e.g., title, description, owner) in the form.  
2. Submit the form to register a patent on the blockchain.  

### Transfer Ownership  
1. Enter the patent ID and the new owner’s address.  
2. Submit the transfer request.  

### Track Patent Status  
- Use the patent ID to fetch details and status from the blockchain.  

---

## 🔧 Commands Summary  

### Blockchain Commands  
- Compile Contracts:  
  ```bash
  truffle compile
  ```
- Migrate Contracts:  
  ```bash
  truffle migrate --network development
  ```

### Backend Commands  
- Install Flask and CORS:  
  ```bash
  pip install flask flask-cors
  ```
- Start Backend Server:  
  ```bash
  python app.py
  ```

### Frontend Commands  
- Install Web3.js:  
  ```bash
  npm install web3
  ```

---

## 🌟 Smart Contract Overview  

- **Patent.sol**  
  - Handles patent registration, updates, and ownership transfers  
  - Core blockchain operations  

---

## 📷 Screenshots  

_Add screenshots or GIFs showcasing the interface and functionality here._  

---

## 🤝 Contributing  

Contributions are welcome! To contribute:  
1. Fork the repository  
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:  
   ```bash
   git push origin feature-name
   ```
5. Open a pull request  

---

## 📄 License  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---

## 📬 Contact  

For questions or feedback:  
- **Email**: 21jr1a12i9@gmail.com  
- **LinkedIn**: https://www.linkedin.com/in/saichandravankadari/ 
