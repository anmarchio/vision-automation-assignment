"""
JSON Parsing and REST API communication
"""
import sys
from json_parsing_rest_api import count_conficence
from ipc_integration import monitor_objects
from opcua_communication import extract_and_send_faults_via_opc_ua

def run_workflow():
    # Task 1: parse json and sent REST API calls
    count_conficence("1.json")
    count_conficence("2.json")

    # Task 2: IPC communication
    monitor_objects("3.json")

    # Task 3: OPC UA communication
    extract_and_send_faults_via_opc_ua("4.xml")

def main() -> int:
    try:
        run_workflow()
    except:
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())