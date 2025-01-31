# Vision Automation Engineer Assignment  

This repository contains the solution to the **36zero Vision Automation Engineer take-home assignment**, which focuses on data processing, system integration, and automation using **Node-RED** and **Python**.

---

## 🚀 **Assignment Overview**
The key objectives of this project are:  
- Parsing and processing data in different formats such as **JSON** and **XML**  
- Integrating with systems like **REST APIs**, **Industrial PCs (IPC)**, and **OPC UA**  
- Showcasing automation with **low-code platforms (Node-RED)**  
- Exception handling and robust logging for maintainability  

---

## 📁 **Project Structure**
```plaintext
├── node-red-flows/         # Node-RED flow files (exported JSON)
├── python-scripts/         # Python processing scripts
├── assets/                 # Relevant images or reference files
├── requirements.txt        # Python dependencies (if applicable)
└── README.md               # Project documentation

## 🛠 **How to Run the Project**

Running Node-RED

* Pull the official Node-RED Docker image:
```bash
docker pull nodered/node-red

* Start Node-RED:
```bash
docker run -it -p 1880:1880 --name mynodered nodered/node-red

* Open Node-RED in your browser: http://localhost:1880.
* Import the flow from node-red-flows/flow.json.

### Running Python Scripts

* Clone this repository:
```bash
git clone https://github.com/your-username/36zero-vision-automation-assignment.git

* Navigate to the project directory:
```bash
cd python-scripts

* Install dependencies:
```bash
pip install -r requirements.txt

* Run the script:

```bash
python your-script-name.py

## 📚 Features
* Data Parsing: Handling JSON and XML data formats
* System Integration: REST API and IPC/OPC UA communication
* Exception Handling: Robust flow control and error handling
* Low-Code Automation: Utilizing Node-RED for efficient automation

## ⚠️ Error Handling
* Node-RED catch nodes for structured exception handling
* Python try/except blocks for resilient data processing
