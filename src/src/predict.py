def predict_failure(features):
    temperature, vibration, pressure = features

    if temperature > 85 or vibration > 0.7 or pressure > 40:
        return "Maintenance Required"

    return "Machine Healthy"
