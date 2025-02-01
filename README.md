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
```

## 🛠 **How to Run the Project**

1. Clone this repository:
```bash
git clone https://github.com/anmarchio/vision-automation-assignment.git
```

2. Navigate to the project directory:
```bash
cd vision-automation-assignment
```

### Running Node-RED

* Pull the official Node-RED Docker image:
```bash
docker pull nodered/node-red
```

* Start Node-RED:
```bash
docker run -it -p 1880:1880 --name mynodered nodered/node-red
```

* Open Node-RED in your browser: http://localhost:1880.
* Import the flow from node-red-flows/flow.json.

#### Additional Nodes

* In the node-red dashboard, go to `Management > Palette verwalten`
* Choose Installation: `@opcua/for-node-red`
* Click `Installieren`
* Check if `@opcua/ua-client` shows up under `Installierte Nodes`

#### Open Node-Red Flows

* Click `management/import`
* Choose the files from `node-red/`
  * `node-red/ipc-communication.json` for the IPC communication flow
  * `node-red/opc-ua-communication.json` for the OPC UA communication flow
  * `node-red/rest-api-communication.json` for the REST API communication flow
* To execute one node, select the related tab and click `deploy`
* Execution will then run locally and show output in the debug window

### Running Python Scripts

For reasons of completeness, the same functionality can also be executed as python scripts.
For the purpose, proceed as follows:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python main.py
```

## 📚 Features
* Data Parsing: Handling JSON and XML data formats
* System Integration: REST API and IPC/OPC UA communication
* Exception Handling: Robust flow control and error handling
* Low-Code Automation: Utilizing Node-RED for efficient automation

## ⚠️ Error Handling
* Node-RED catch nodes for structured exception handling
* Python try/except blocks for resilient data processing
