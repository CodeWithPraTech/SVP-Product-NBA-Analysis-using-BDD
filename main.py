import user_input
from nba_functions import product_nba
from nba_to_bdd import convert_nbas_to_bdds
from bdd_product import bdd_product
import time
from dd.autoref import BDD  # Import the BDD manager
import sys


def compare_products(nbas):
    # Product of NBAs
    start_time_nba = time.time()
    product_nba_automaton = product_nba(nbas)
    end_time_nba = time.time()

    # Measure memory usage
    mem_usage_nba = sys.getsizeof(product_nba_automaton.transitions)

    # Create a single BDD manager
    bdd_manager = BDD()  # This ensures all BDDs share the same context

    # Product of BDDs
    bdds = convert_nbas_to_bdds(nbas, bdd_manager)

    start_time_bdd = time.time()
    product_bdd = bdd_product(bdds)
    end_time_bdd = time.time()

    # Measure memory usage
    mem_usage_bdd = sys.getsizeof(product_bdd.to_expr())

    # Display length
    print("k = ", len(nbas))

    # Display results
    print("\nProduct NBA:")
    # print(product_nba_automaton)
    print(f"Time taken for NBA product: {end_time_nba - start_time_nba:.20f} seconds")
    print(f"Memory usage for NBA product: {mem_usage_nba} B")

    print("\nProduct BDD:")
    print(product_bdd.to_expr())
    print(f"Time taken for BDD product: {end_time_bdd - start_time_bdd:.20f} seconds")
    print(f"Memory usage for BDD product: {mem_usage_bdd} B")

    return end_time_nba - start_time_nba, mem_usage_nba, end_time_bdd - start_time_bdd, mem_usage_bdd


def compare_products_values(nbas):
    # Product of NBAs
    start_time_nba = time.time()
    product_nba_automaton = product_nba(nbas)
    end_time_nba = time.time()

    # Measure memory usage
    mem_usage_nba = sys.getsizeof(product_nba_automaton.transitions)

    # Create a single BDD manager
    bdd_manager = BDD()  # This ensures all BDDs share the same context

    # Product of BDDs
    bdds = convert_nbas_to_bdds(nbas, bdd_manager)

    start_time_bdd = time.time()
    product_bdd = bdd_product(bdds)
    end_time_bdd = time.time()

    # Measure memory usage
    mem_usage_bdd = sys.getsizeof(product_bdd.to_expr())

    # # Display length
    # print("k = ", len(nbas))

    # # Display results
    # print("\nProduct NBA:")
    # # print(product_nba_automaton)
    # print(f"Time taken for NBA product: {end_time_nba - start_time_nba:.20f} seconds")
    # print(f"Memory usage for NBA product: {mem_usage_nba} B")

    # print("\nProduct BDD:")
    # print(product_bdd.to_expr())
    # print(f"Time taken for BDD product: {end_time_bdd - start_time_bdd:.20f} seconds")
    # print(f"Memory usage for BDD product: {mem_usage_bdd} B")

    return end_time_nba - start_time_nba, mem_usage_nba, end_time_bdd - start_time_bdd, mem_usage_bdd

def main():
    nbas = user_input.main()  # Get NBAs from user input
    a,b,c,d = compare_products(nbas)     # Compare NBA and BDD products
    # Python code to generate LaTeX code

# Python code to generate LaTeX code

    k_values = range(1, 6)
    n_values = range(1, 6)
    s_values = range(1, 6)

    latex_code = r"""
    \documentclass{article}
    \usepackage{graphicx}
    \begin{document}
    \title{Performance Comparison}
    \author{Pratik and Sandeep}
    \date{\today}
    \maketitle
    """
    for k in k_values:
        latex_code += r"""
    \begin{table}[ht]
    \centering
    \begin{tabular}{|c|c|c|c|c|c|}
    \hline
    n & s & NT & NS & BT & BS \\
    \hline
    """
        for i in n_values:
            for j in s_values:
                # Assuming `compare_products_values` returns (nba_time, nba_space, bdd_time, bdd_space)
                # Replace with actual function call and data collection logic
                nbas = [user_input.generate_random_nba(i, j) for _ in range(k)]
                nba_time, nba_space, bdd_time, bdd_space = compare_products_values(nbas)
                latex_code += " %d & %d & %.6f & %d & %.6f & %d \\\\ \n" % (i, j, nba_time, nba_space, bdd_time, bdd_space)
        
        latex_code += r"""
    \hline
    \end{tabular}
    \caption{Performance comparison for k = %d}
    \end{table}
    """ % k

    latex_code += r"""
    \end{document}
    """

    # Print or write the LaTeX code to a file
    print(latex_code)

    with open('document.tex', 'w') as file:
        file.write(latex_code)


if __name__ == "__main__":
    main()
