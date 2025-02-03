"""
JSON Parsing and REST API communication
"""
import sys

import uvicorn

from endpoints.tcp_listener import run_tcp_listener


def main() -> int:
    print("Vision Assignment Endpoints")
    print("=" * 30 + "\n")
    print("Select an option:")
    print("(1) Task 1: REST API communication")
    print("(2) Task 2: IPC communication")
    print("(3) Task 3: OPC UA communication\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Running REST API server on 0.0.0.0:8000")
        uvicorn.run("endpoints.api_endpoint:app", host="0.0.0.0", port=8000, reload=True)
    elif choice == "2":
        print("Run TCP Listener on 0.0.0.0:500")
        run_tcp_listener()
    elif choice == "3":
        print("NOTE:")
        print("! No OPC UA implementation available !")
        print("Use the sterfive implementation.")

    return 0


if __name__ == '__main__':
    sys.exit(main())
