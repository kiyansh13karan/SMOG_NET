# 🚨 SmogNet: Predictive AI Atmospheric Systems

**SmogNet** is an AI-powered atmospheric intelligence and early warning platform designed to tackle severe air quality crises in major cities across Pakistan (Lahore, Karachi, Islamabad, Peshawar, Quetta). 

By analyzing multi-gas telemetry data, the platform uses Machine Learning to accurately predict the root cause of pollution spikes and automatically dispatches localized emergency alerts.

---

## 🌟 Key Features

1. **Interactive Predictor Simulator**
   - Adjust real-time sliders for 8 different pollutants (`PM2.5`, `PM10`, `NO`, `NO2`, `SO2`, `NH3`, `CO`, `Ozone`).
   - The Random Forest Machine Learning model instantly classifies the source of the smog (e.g., *Crop Burning, Vehicular Emissions, Dust Storms, Industrial, Mixed*).

2. **Real-Time City Monitor Dashboard**
   - A glassmorphism, responsive map view displaying simulated emotional and health-risk indices across different regions.
   - Preserves state across navigations, tracking real-time regional anomalies.

3. **Automated Emergency Alert System**
   - Triggers dynamic SMTP email alerts whenever hazardous AQI levels are breached.
   - Automatically injects the **current city**, **emission reason**, and **source-specific prevention guidelines** (e.g., specific instructions for crop burning in Lahore).
   - Formatted with engaging emojis and clear safety instructions.

4. **AI Health Assistant (Groq LLaMA 3.3)**
   - A localized Chatbot powered by LLaMA 3.3 tailored for Pakistan’s air quality health risks.
   - Provides immediate, AI-driven medical guidance on masks, safe limits, and symptoms.

---

## 🛠️ Technology Stack

- **Frontend**: HTML5, Tailwind CSS, Chart.js, Vanilla JavaScript, Glassmorphism UI.
- **Backend**: Python, Flask, smtplib (Email Alerts).
- **Machine Learning**: Scikit-learn (`RandomForestClassifier`), Pandas.
- **AI/LLM**: Groq API (LLaMA 3.3 70B).
- **Data & Storage**: DuckDB (via Jetro integrations), LocalStorage for frontend state.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js (for Tailwind CSS build process, optional)

### 1. Clone the Repository
```bash
git clone https://github.com/AlgoHub-2025/SMOG_NET_DATATHONE.git
cd SMOG_NET_DATATHONE
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the `backend/` directory with the following structure:
```env
# SMTP Configuration (For Email Alerts)
SMTP_USER="your-email@gmail.com"
SMTP_PASSWORD="your-app-password"

# Groq Configuration (For AI Chatbot)
GROQ_API_KEY="your-groq-api-key"
```

### 4. Run the Backend Server
```bash
cd backend
python app.py
```
The server will start on `http://127.0.0.1:5000`.

### 5. Access the Platform
Open your browser and navigate to:
- **Simulator**: `http://127.0.0.1:5000/index.html`
- **City Monitor**: `http://127.0.0.1:5000/smognet_intelligence_dashboard.html`
- **AI Assistant**: `http://127.0.0.1:5000/chatbot.html`

---

## 🛡️ License & Datathon Note
This project was developed for the **AlgoHub 2025 Datathon**. 
