# Vision Automation Engineer Assignment  

This repository contains the solution to the **36zero Vision Automation Engineer take-home assignment**, which focuses on data processing, system integration, and automation using **Node-RED** and **Python**.

---

## 🚀 **Assignment Overview**
The assignment is split into 3 dedicated tasks. The key objectives can be summed up as follows:  
- Task 1: Parsing and processing data from json files and send POST and GET requests to an API endpoint
- Task 2: Communicating with an OPC UA server and sending data to a REST API endpoint
- Task 3: Communicating with an IPC and sending DIO signals via a standardized interface (TCP/IP)
- Ensure Exception handling and logging for maintainability  

---

## 📁 **Project Structure**
```plaintext
├── /                   # raw assignment source data and configuration files
├── endpoints/          # Python helper scripts
├── node-red/           # Node-RED flow files (exported JSON)
├── requirements.txt    # Python dependencies (if applicable)
└── README.md           # Project documentation
```

## 🛠 **Setting up the Project**

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

## 📡 **Running the Assignment**

### Set Environemt Variables

* open `management\settings`
* Insert variables by clicking `add`:
  * Insert the path of the root directory on your machine, e.g. as: 
  * `ROOT_PATH`: `<YOUR-DIRECTORY>\vision-automation-assignment`
  * `WEBHOOK`: `localhost:8000`

### Task 1: JSON parsing and REST API Communication

* *Run Python Environment:* 
```bash
python main.py
``` 
* select `1` to run the uvicorn server on `localhost:8000`
* In node-red, select `management/import`
  * import the json file: `node-red/ipc-communication.json`
  * select `deploy` to run the IPC communication flow
* Execution will then run locally and output should appear in the debug window
  * Check for terminal output
  * Should show `1` upon execution

### Task 2: IPC Integration
* Import the json file: `node-red/rest-api-communication.json` 
* Click deploy to run the flow

### Task 3: OPC UA Communication
* Import the json file: `node-red/opc-ua-communication.json` 
* Check if the opc ua node is active (see instructions to install nodes above)
* Click deploy to run the flow
* Message will be written to: `opc.tcp://opcuademo.sterfive.com:26543/UA/SampleServer` 

### Run unittests
```bash
python -m unittest discover tests
```

## ⚠️ Error Handling
* Node-RED catch nodes for structured exception handling
* Python try/except blocks for resilient data processing

## 📝 **Recommended Improvements**
* Unit testing for python scripts and potentially for node-red
* Containerization for the environment when the specific destination platform is given (raspi, edge PC, linux server)
* Integration with hosted CI/CD pipeline