import matplotlib
import matplotlib.pyplot as plt
nvalues = []
time = []

with open(r"C:\Users\SARASWATI YALI\OneDrive\Desktop\laxmi_ADA\time_data.txt", "r") as file:
    for line in file:
        parts = line.split()

        if len(parts) >= 2:
            n = int(parts[0])
            t = float(parts[1])

            nvalues.append(int(n))
            time.append(float(t))

plt.figure(figsize=(10,6))
plt.plot(nvalues, time, marker='o', linestyle='-', color='green')

plt.xlabel('Number of elements')
plt.ylabel('Time taken (ms) ')
plt.title('Time Complexity of Selection Sort')
plt.grid(True)

plt.savefig('selection sort')  # added extension
plt.show()
