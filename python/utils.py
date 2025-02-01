
def parse_json(filename: str):
    content = json.load(open(filename, "r"))
    fi_confidence_values = content["results"]["up"]["fi_confidence"]
    SERIAL_IDS = tr_values = content["results"]["up"]["tr_values"]
    numberMinDetectedObjects = content["results"]["up"]["numberMinDetectedObjects"]

    return fi_confidence_values, tr_values, numberMinDetectedObjects