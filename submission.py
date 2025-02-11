import MonteCarlo
import ZeroR
import perceptron
import os

print("testing Monte Carlo")
MonteCarlo.monte_carlo_approach(10)

print("testing ZeroR")
fname = "tennis.csv"
with open(fname) as f :
    data = f.readlines()
    print(ZeroR.zeroR(data))
print("You can test the command line arguments from the command line using tennis.csv.")


print("Testing wc.py")
print("You can run wc.py from the command line, like so:")
print()
print("  python3 wc.py --strip sample.txt")
print("  python3 wc.py --strip --convert sample.txt")
print("  python3 wc.py --strip --pfile=works.pkl sample.txt")
print()

# Runing the actual tests using os.system()
print("Running: python wc.py --strip sample.txt")
os.system("python3 wc.py --strip sample.txt")

print("\n Running: python wc.py --strip --convert sample.txt")
os.system("python3 wc.py --strip --convert sample.txt")

print("\n Running: python wc.py --strip --pfile=works.pkl sample.txt")
os.system("python3 wc.py --strip --pfile=works.pkl sample.txt")

print("\n Test script finished.")


print("testing perceptron")
perceptron.perceptron_training()

print("")