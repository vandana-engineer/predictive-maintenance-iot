def preprocess_sensor_data(data):
    features = [
        data["temperature"],
        data["vibration"],
        data["pressure"]
    ]
    return features
