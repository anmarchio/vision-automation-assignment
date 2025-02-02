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
├── endpoints/          # Python helper scripts
├── node-red/           # Node-RED flow files (exported JSON)
├── requirements.txt    # Python dependencies (if applicable)
└── README.md           # Project documentation
```

## 🛠 **Install Prerequesites**

* Get and install java for your environment: https://www.java.com/en/download/
* Get and Extract JMeter: https://jmeter.apache.org/download_jmeter.cgi

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

* For the windows setup, see: https://nodered.org/docs/getting-started/windows
* Download node red from: https://nodejs.org/en/
* Install node red by running the installer
* Open the command prompt and run:
```bash
node-red
```

* Open Node-RED in your browser: http://localhost:1880.
* Import the flows as described below.

#### Additional Nodes

* In the node-red dashboard, go to `Management > Palette Management`
* Choose Installation: `@opcua/for-node-red`
* Click `Install`
* Check if `@opcua/ua-client` shows up under `Installed Nodes`

#### Open Node-Red Flows

* Select `management/import`
* Choose related files from `node-red/`
  * Task 1: `node-red/ipc-communication.json` for the IPC communication flow
  * Task 2: `node-red/opc-ua-communication.json` for the OPC UA communication flow
  * Task 3: `node-red/rest-api-communication.json` for the REST API communication flow
* To execute one node, select the related tab and click `deploy`
* Execution will then run locally and output should appear in the debug window

### Set Environemt Variables

* open `management\settings`
* Insert variables by clicking `add`:
  * Insert the path of the root directory on your machine, e.g. as: 
  * `ROOT_PATH`: `<YOUR-DIRECTORY>\vision-automation-assignment`
  * `WEBHOOK`: `localhost:8000`

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

4. Run script for the equivalent task:

* *For Task 1:* 
  * start local server: `uvicorn app:app --reload --host 0.0.0.0 --port 8000`
  * select `1` when running `python main.py` 
* *Task 2:* 
  * Run: `python main.py`
  * Select `2` 
* *Task 3:*
  * Will write message to: `opc.tcp://opcuademo.sterfive.com:26543/UA/SampleServer` 

## ⚠️ Error Handling
* Node-RED catch nodes for structured exception handling
* Python try/except blocks for resilient data processing

## 📝 **Recommended Improvements**
* Unit testing for python scripts and potentially for node-red
* Containerization for the environment when the specific destination platform is given (raspi, edge PC, linux server)
* Integration with hosted CI/CD pipeline