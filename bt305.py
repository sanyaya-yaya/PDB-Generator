import random
import os

def random_angle(l, r):
    """Function to generate a random angle within a given range"""
    return random.uniform(l, r)

def main():
    random.seed() # Seed for random number generation based on current time
    t = int(input("Enter the number of RIB files you want to create: "))
    res = int(input("Enter the number of residues: "))

    for fileNum in range(t):
        n = random.randint(0, res)
        base = "output"
        file_name = f"{base}{fileNum}.rib"
        with open(os.path.join("ribfiles", file_name), "w") as outputFile:
            # Printing default lines in output.rib file
            outputFile.write("# Sample command file. This builds the peptide as a helix\n\n")
            outputFile.write("# Except for the glycine which has a phi of 90.0 and psi of 0.0\n\n")
            outputFile.write("TITLE RIBOSOME EXAMPLE 2\n\n")
            outputFile.write("default helix\n\n")

            # List of Amino Acids
            amino_acids = ["ala", "leu", "glu", "gln", "lys", "met", "arg", "asn", "asp", "cys", "gly", "his", "ile", "phe", "pro", "ser", "thr", "trp", "tyr", "val"]

            for _ in range(n):
                aa = random.choice(amino_acids)
                strand = random.randint(0, 1)
                if strand: # Generate phi and psi for Alpha Helix
                    phi = random_angle(-65.0, -55.0)
                    psi = random_angle(-55.0, -45.0)
                else:    # Generate phi and psi for Beta Strand
                    phi = random_angle(-145.0, -135.0)
                    psi = random_angle(125.0, 135.0)
                # Printing each residue line in output.rib file
                outputFile.write(f"res {aa} phi {phi:.4f} psi {psi:.4f}\n\n")

    print("Code executed")

if __name__ == "__main__":
    main()