# YQuantum_EuroQuantum

# Quantum Factorization Challenge

**Sponsored by**
![Quantum Rings](./images/quantum-rings-logo.png)

## Overview
Welcome to the Quantum Factorization Challenge. Your mission: use the large-scale quantum simulation provided by Quantum Rings to factor the largest semiprime in the hackathon by developing and executing your own implementation of Shor's algorithm.

---

## Why Does This Matter?
Shor’s Algorithm was one of the first quantum algorithms to demonstrate exponential speedup over classical methods. It targets a foundational problem: factoring large semiprimes, which underpins modern public-key cryptography.

RSA encryption relies on the fact that it's easy to multiply two primes, but exponentially hard to factor their product. At key sizes like 2048 bits, factoring on classical computers is essentially impossible. Shor’s Algorithm changes that—given a large enough quantum computer, it can break RSA.

By joining this challenge, you're not just solving a math problem. You're helping explore the future of cybersecurity, data privacy, and quantum computational theory.

---

## Expectations / Requirements

### Build a Universal Shor’s Algorithm
Your implementation must be capable of factoring any valid semiprime, not just a hardcoded example. No brute-force attacks. No classical-only factoring.

### Factor Large Semiprime Integers
Work from a [provided list of semiprime integers](./semiprimes.py)—starting from simple 8-bit values and scaling up to sizes never factored using quantum logic.

### Leverage the Quantum Rings Simulator
Use any framework, but all circuits must run on the Quantum Rings Simulator.

### Quantum Logic Required
No classical shortcuts. Implement full quantum modular exponentiation, phase estimation, and QFT.

### Demonstrate Universality
Show that your circuit works across multiple semiprimes of the [given list](./semiprimes.py).

### Working Source Code
All source code must be provided via an open source [GitHub](https://github.com/home) repository.  If you don't already have an account, you can get one for free.

### Document Your Approach
Also in your GitHub repository, provide a clean explanation of your algorithm, approach, and insights.

See the [Challenge Guidelines](./challenge-guidelines.md) for detailed do’s and don’ts.

---

## Judging Criteria

### In-Person Teams
- Present your approach and results in person.
- Judged based on:
  - Correctness and scale of the solution
  - Novelty/innovation (optimizations, resource efficiency, etc.)
  - Quality of presentation
- All submissions must include:
  - Live presentation
  - Source code
  - Execution evidence
  - Documentation

### Remote Teams
- Submit source code and result via an online form
- Judged based on:
  - Largest semiprime factored
  - Tie-breakers: fastest execution + strongest documentation
- All submissions must include:
  - Source code
  - Execution evidence
  - Documentation

**Note:** Before selecting a winner, the source code, execution evidence, and documentation will be reviewed to ensure all requirements have been met.

## What you'll Win

In addition to the pride of winning the challenge, members of the winning team will receive:

🏆 **A copy of *Fundamentals of Quantum Computing: Theory and Practice*** by Quantum Rings' Co-founder and CTO, **Venkat Kasirajan**. (up to 5 team members)

- If the winning team is based in the U.S., each member will receive a signed copy with a personal note from Venkat. 
- If the winning team is outside the U.S., each member will receive a copy of the textbook shipped directly from the publisher.

[📖 Check out the book here.](https://www.google.com/books/edition/Fundamentals_of_Quantum_Computing/NVw0EAAAQBAJ?hl=en&gbpv=0)

Additionally, all participants will receive:
- Access to the Quantum Rings Simulator with 200 qubits for one year after the hackathon (non-commercial use).
- Support from the Quantum Rings community and staff to assist with simulator-related questions during the event.
- Hands-on experience with cutting-edge quantum computing challenges.

---

## Free Access to Best-in-class Simulation
1. Register for free at [www.QuantumRings.com](https://www.quantumrings.com)
2. Confirm your email
3. Select "Manage Keys" and enter Promocode ```YQUANTUM25``` to unlock 200 qubits of simulation --> This will be available to you for an entire year following the hackathon
4. Copy the key, and use it to start simulating massive circuits locally!

If you need more capacity -- just ask!  We'll be happy to unlock even more qubits of simulation during the hackathon.  Just ask on the [#quantum-rings channel on discord.](https://discord.com/channels/1326009426141777950/1330328378301087804)

---

## Submission Guidelines

Submit the following:

1. **Code**: Provide your quantum implementation using Quantum Rings' simulator via GitHub. 
2. **Results**: Include the integers factored, their prime factors, the number of qubits used, the number of gate operations, and the execution times.
3. **Quantum Rings Email**: Include the email used to register at Quantum Rings-- this will be used to validate the circuit execution.
4. **Documentation**: Explain your algorithm, scalability, and insights into any learnings or novelty in your approach.

When you are ready to submit, you can submit your circuit using this [Google Form](https://forms.gle/NzCSnqppQNQCLRsX6)

Note: In addition to submitting electronically, in-person teams will also be presenting in person.
---

## Resources

### Quantum Rings SDK
- [SDK Documentation](https://portal.quantumrings.com/docs)
- Simulate up to 200 qubits during and after the hackathon
- Free for students and hackathon participants

> **Promo Code:** `YQUANTUM25`  
> Activate before the end of the hackathon to unlock 200 qubits for 1 year

### Help & Community
- [Quantum Rings Discord Channel](https://discord.com/channels/1326009426141777950/1330328378301087804)
  - Quantum Rings employees and community are here to help
  - Get support during and after the hackathon
- [Quantum Rings GPT Assistant](https://chatgpt.com/g/g-67d47e3159f88191b20c3aec22410021-quantum-rings-code-help)

### Challenge Repository
- [Notebook Starter Example](./shor.ipynb) → includes a toy model for factoring 15, with detailed help to understand Shor's algorithm
- [Challenge Guidelines](./challenge-guidelines.md) → clear do’s and don’ts

### Shor’s Algorithm
- [Dr. Shor explains it himself (video)](https://youtu.be/hOlOY7NyMfs)
- [Shor’s Overview](./shors-overview.md) included in the challenge repository

---

Good luck-- let's see what you can achieve!
