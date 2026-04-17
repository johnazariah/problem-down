# Preface

Most quantum computing books start with a qubit. Then two qubits. Then gates. Then circuits. Somewhere around chapter eight, if you're still reading, you might encounter a real problem.

This book does the opposite.

We start with problems. Real ones, with dollar figures attached. UPS saving \$50 million a year by shaving one mile off delivery routes. Banks pricing derivatives with Monte Carlo simulations that take hours. Pharmaceutical companies spending \$2 billion and twelve years to bring a single drug to market. Climate scientists searching for catalysts that could pull carbon from the atmosphere.

For each problem, we ask: what makes it hard? Not "hard" in the vague sense, but structurally hard. What is the specific computational bottleneck that defeats classical computers? And then: does quantum mechanics offer anything at precisely that bottleneck?

Sometimes the answer is yes. Sometimes the answer is "maybe, if hardware improves by two orders of magnitude." Sometimes the answer is "we honestly don't know yet." We give you all three, clearly labelled.

## How this book is structured

The book is organised into eight **units**, each built around one industry problem. Every unit has two parts:

- The **application chapter** tells the story. It opens with the industry context, identifies the computational bottleneck, shows how a quantum algorithm addresses it, walks through a toy example, and closes with an honest assessment of where things stand today. You need no prior quantum knowledge to read these chapters.

- The **deep-dive chapter** teaches the algorithm at the circuit level. It introduces quantum concepts (qubits, gates, interference, entanglement) organically, as the algorithm needs them. These chapters are more technical, but they build everything from scratch.

## Two ways to read this book

**The fast path.** Read only the application chapters (Units 1 through 8). You'll understand what quantum computers could do for logistics, cryptography, drug discovery, machine learning, finance, supply chains, materials science, and climate. You'll know which applications are close to practical and which are speculative. You'll be able to hold your own in any conversation about quantum computing's real-world impact.

**The full path.** Read the application chapters *and* the deep-dives. By the end, you'll understand QAOA, Shor's algorithm, VQE, quantum kernels, amplitude estimation, QUBO, QPE with Trotterisation, and quantum embedding methods. Not as abstract constructions, but as tools built to solve specific problems.

Either path works. The deep-dives never assume you've read other deep-dives out of order; each one states its prerequisites explicitly.

After the eight units, a standalone chapter on **quantum error correction** explains why today's hardware can't yet run most of these algorithms at scale — and what it will take to get there. The book closes with a short **conclusion** that ties the eight units together around a single idea.

## The notebooks

Every unit has a companion Jupyter notebook that runs a version of the algorithm on a real quantum backend. Some are faithful implementations; others are simplified demonstrations that illustrate the pipeline at toy scale. You can run them, modify them, and break them. That's the point.

## What we don't promise

We don't promise that quantum computers will revolutionise your industry next year. Some of the applications in this book require fault-tolerant quantum computers that don't exist yet. Every chapter includes a **Reality Check** section that states, plainly, what works today on noisy hardware, what needs error correction, and what remains an open question.

We use "could" and "in principle" where others use "will" and "soon." We cite specific resource estimates. We acknowledge when classical algorithms have closed the gap. This is not a hype document.

## Who this book is for

You're curious about quantum computing, but you want to know *what it's for* before learning *how it works*. Maybe you're a software engineer evaluating whether to invest time in quantum. Maybe you're a domain expert in finance or pharma who's heard the promises and wants specifics. Maybe you're a student who finds qubits abstract and wants motivation before formalism.

If you're looking for a comprehensive quantum computing textbook, read Nielsen and Chuang. If you want to build quantum circuits from scratch, see our companion project, the Quokka Cookbook. This book is for people who want to start with the "why."

Let's start with a delivery truck.
