from model import build_model

def train():
    model = build_model()

    X = [
        [78, 0.4, 30],
        [92, 0.8, 45],
        [80, 0.3, 28],
        [95, 0.9, 50]
    ]

    y = [0, 1, 0, 1]

    model.fit(X, y)

    return model

if __name__ == "__main__":
    train()
