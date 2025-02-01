from python.utils import parse_json

SERIAL_IDS = []


def count_confidence(filename: str, threshold: float = 0.99):
    fi_confidence_values, tr_values, _ = parse_json(filename)
    count = 0
    for v in fi_confidence_values:
        if v > threshold:
            count += 1

    # Send count as REST API POST
    raise NotImplementedError


def send_count():
    try:
        # Make a POST request to an API endpoint with the count
        pass
    except Exception as e:
        print(e)


def get_serial_id():
    # - Extract all tr_values
    # – Use these values as serial IDs in REST API calls
    try:
        pass
    except Exception as e:
        print(e)
