Here's a simple README file that provides instructions on how to use the project and a brief description of each file:

---

# NBA to BDD Product Construction

This project generates Non-deterministic Büchi Automata (NBA), converts them to Binary Decision Diagrams (BDD), and computes their products. It also compares the time and memory usage of the product calculations using NBAs and BDDs.

## Project Structure

The project consists of the following files:

- **`main.py`**: The main driver file that orchestrates the entire process. It prompts the user for input, generates the NBAs, computes their products using both NBA and BDD, and compares the performance of the two approaches.

- **`user_input.py`**: This file handles user input and generates random NBAs based on the parameters provided by the user. It collects the number of automata, the number of states for each automaton, and the size of the alphabet.

- **`nba_functions.py`**: Contains functions for computing the product of NBAs. It takes a list of NBAs and returns their product automaton.

- **`nba_to_bdd.py`**: This file converts the generated NBAs into BDDs. It contains the logic for translating NBA state transitions into BDD representations.

- **`bdd_product.py`**: This file contains the function for computing the product of multiple BDDs. It takes a list of BDDs and returns their product.

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Required Libraries**:
   Make sure you have the necessary libraries installed. You may need to install `dd` for BDD functionality. You can install it using:
   ```bash
   pip install dd
   ```

3. **Run the Program**:
   Execute the main script to start the program:
   ```bash
   python main.py
   ```

4. **Provide Input**:
   When prompted, enter the number of NBAs you want to generate, the number of states for each NBA, and the size of the alphabet.

5. **View Results**:
   After entering the inputs, the program will display the generated NBAs, the product of the NBAs, and the product of the BDDs. It will also show the time taken and memory used for both calculations.

## Example Input

```
Enter the number of NBAs (k): 3
Enter the number of states for each NBA: 5
Enter the size of the alphabet for each NBA: 3
```

## Note

Ensure that you have requirements installed on your machine. This project has been tested with Python 3.12