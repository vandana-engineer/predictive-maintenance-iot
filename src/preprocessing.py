def preprocess_sensor_data(data):
    return [
        data["temperature"],
        data["vibration"],
        data["pressure"]
    ]
