# 8. Computational Graphs, Derivatives, and Backpropagation

Understanding how neural networks actually compute gradients and learn is crucial for becoming an effective deep learning practitioner. Let's break down these mathematical concepts in an intuitive way.

## What is a Computational Graph?

### Simple Definition

**Computational Graph**: A visual representation of mathematical operations as a network of connected nodes, where each node represents an operation and edges represent data flow.

**Think of it like**: A recipe flowchart where each step depends on previous steps, and you can trace backwards to see what ingredients affected the final result.

### Basic Example

Let's say we want to compute: `z = (x + y) × w`

**As a computational graph**:

```
x ──┐
    ├─→ [+] ──→ [*] ──→ z
y ──┘           ↑
                w
```

**What each node does**:

1. **Addition node**: Takes x and y as inputs, produces (sum of x + y) as output
2. **Multiplication node**: Takes output of Addition node (sum of x + y) and w as inputs, produces final result z as output

### Why Computational Graphs Matter

**Forward Pass**: Follow the graph left to right to compute the result
**Backward Pass**: Follow the graph right to left to compute gradients (how much each input affects the output)

## Derivatives: The Foundation of Learning

### What is a Derivative?

**Simple Definition**: A derivative tells you how much the output changes when you slightly change the input.

**Real-Life Example**:

- **Speed** is the derivative of distance with respect to time
- If you're driving and increase your speed, the derivative tells you how much farther you'll travel

### Derivatives in Neural Networks

**The Big Question**: If we slightly change a weight in our network, how much will the final loss (error) change?

**Why This Matters**:

- If increasing a weight increases error → decrease that weight
- If increasing a weight decreases error → increase that weight
- If changing a weight doesn't affect error → leave it alone

### Chain Rule: The Key to Everything

**The Problem**: In deep networks, weights affect the output through many intermediate steps.

**The Solution**: Chain rule lets us compute how a change propagates through multiple steps.

**Simple Example**:
If `z = f(y)` and `y = g(x)`, then:

```
dz/dx = (dz/dy) × (dy/dx)
```

**In Plain English**: To see how z changes with x, multiply:

1. How z changes with y
2. How y changes with x

## Backpropagation: Learning in Action

### What is Backpropagation?

**Simple Definition**: A method to efficiently calculate gradients by working backwards through the computational graph.

**The Process**:

1. **Forward pass**: Compute predictions and loss
2. **Backward pass**: Compute gradients by applying chain rule backwards
3. **Update**: Adjust weights based on gradients

### Step-by-Step Example

Let's trace through a simple network: `Input → Weight → Output → Loss`

#### Forward Pass

**Computational Graph**:

```
x = 2 ──┐
        ├─→ [× (multiply)] ──→ y = 6 ──→ [(y-target)²] ──→ L = 16
w = 3 ──┘                              ↑
                                   target = 2
```

**Step-by-step calculation**:

1. **Multiplication node**: x × w = 2 × 3 = 6 → y = 6
2. **Loss node**: (y - target)² = (6 - 2)² = 4² = 16 → L = 16

#### Backward Pass (Computing Gradients)

**Step 1**: How does Loss change with Output?

```
dL/dy = 2×(y-target) = 2×(6-2) = 8
```

**Step 2**: How does Output change with Weight?

```
dy/dw = x = 2
```

**Step 3**: Chain rule - How does Loss change with Weight?

```
dL/dw = (dL/dy) × (dy/dw) = 8 × 2 = 16
```

**Step 4**: Update the weight

```
w_new = w_old - learning_rate × gradient
w_new = 3 - 0.1 × 16 = 1.4
```

### Visualizing Backpropagation

**Forward Pass (left to right)**:

```
x = 2 ──┐
        ├─→ [×] ──→ y = 6 ──→ [(·)²] ──→ L = 16
w = 3 ──┘
```

**Backward Pass (right to left with gradients)**:

```
        ┌── dL/dx = 24 ←─┐
        │                │
x = 2 ──┼─→ [×] ──→ y = 6 ──→ [(·)²] ──→ L = 16
        │                      ↑
w = 3 ──┼── dL/dw = 16 ←──── dL/dy = 8
        │
        └── (gradients flow backward)
```

## Key Concepts Explained

### Gradients

**What they are**: Numbers that tell you which direction to adjust weights to reduce error.

**Interpretation**:

- **Positive gradient**: Decrease the weight to reduce loss
- **Negative gradient**: Increase the weight to reduce loss
- **Large gradient**: This weight has big impact on loss
- **Small gradient**: This weight has little impact on loss

### Automatic Differentiation

**The Challenge**: Computing derivatives manually is tedious and error-prone for complex networks.

**The Solution**: Frameworks like PyTorch and TensorFlow automatically:

1. Build computational graphs as you define your model
2. Compute gradients using backpropagation
3. Handle all the chain rule mathematics for you

**Your Job**: Just call `.backward()` and the framework does the rest!

### Common Activation Function Derivatives

Understanding these helps you see why certain activations work better:

**ReLU**: `f(x) = max(0, x)`

- **Derivative**: 1 if x > 0, else 0
- **Why it's good**: Simple, no vanishing gradient problem for positive values

**Sigmoid**: `f(x) = 1/(1 + e^(-x))`

- **Derivative**: `f(x) × (1 - f(x))`
- **Problem**: Gradients vanish for large positive/negative inputs

**Tanh**: `f(x) = tanh(x)`

- **Derivative**: `1 - f(x)²`
- **Better than sigmoid**: Centered around zero

## Practical Implications

### Vanishing Gradients

**Problem**: In deep networks, gradients become very small in early layers.

**Why it happens**: Multiplying many small derivatives together (chain rule) makes the result tiny.

**Solutions**:

- Use ReLU activation (doesn't saturate for positive values)
- Skip connections (ResNet architecture)
- Better weight initialization
- Batch normalization

### Exploding Gradients

**Problem**: Gradients become extremely large, causing unstable training.

**Why it happens**: Multiplying many large derivatives together.

**Solutions**:

- Gradient clipping (limit maximum gradient size)
- Better weight initialization
- Lower learning rates

### Gradient Flow

**Good gradient flow**: Gradients propagate well through all layers
**Poor gradient flow**: Some layers barely learn because gradients are too small

**How to check**: Plot gradient magnitudes across layers during training

## Hands-On Understanding

### Simple PyTorch Example

```python
import torch

# Create tensors that track gradients
x = torch.tensor(2.0, requires_grad=True)
w = torch.tensor(3.0, requires_grad=True)

# Forward pass
y = x * w
loss = (y - 4)**2

# Backward pass (automatic differentiation)
loss.backward()

# Check gradients
print(f"Gradient of loss w.r.t. w: {w.grad}")
print(f"Gradient of loss w.r.t. x: {x.grad}")
```

**Remember**: The mathematical details might seem complex, but modern frameworks handle most of the complexity for you. Focus on understanding the concepts and let the tools handle the calculations!

---

## Navigation

**← Back:** [7. Neural Networks Deep Dive](07_Neural_Networks_Deep_Dive.md)
