import random

## for each element, the first six items are the input, and the last is the expected output.
training_examples = [
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0],
]

def threshold(val):
    return 1 if val >= 0 else 0

def perceptron_training():
    alpha = 0.1
    bias = -0.1
    weights = [(random.random() / 10) - 0.05 for _ in range(6)]  # Initialize weights randomly

    converged = False
    while not converged:
        converged = True
        for example in training_examples:
            inputs = example[:-1]  # First 6 values are inputs
            expected = example[-1]  # Last value is expected output

            # Compute the actual output
            total = bias + sum(weights[i] * inputs[i] for i in range(len(inputs)))
            actual = threshold(total)

            # Update weights if incorrect
            if actual != expected:
                converged = False
                error = expected - actual
                for i in range(len(weights)):
                    weights[i] += alpha * error * inputs[i]
                bias += alpha * error  # Update bias

    # Print results
    print("Final weights:", weights)
    print("Final bias:", bias)
    for example in training_examples:
        total = bias + sum(weights[i] * example[i] for i in range(len(weights)))
        output = threshold(total)
        print(f"Expected: {example[-1]} Actual: {output}")

perceptron_training()
