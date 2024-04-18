import matplotlib.pyplot as plt

# Data
data = {'0': 5789471,
        '1': 21295863,
        '2': 5549375,
        '3': 4064601,
        '4': 554184,
        '5': 563898,
        '6': 477485,
        '7': 2198267}
# Create bar chart
plt.figure(figsize=(10,6))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.xlabel('Gate Number')
plt.ylabel('Count')
plt.title('Gate Count(n=30000-2)')
plt.ylim(0, 150000000)
# Save plot as a PDF file
plt.savefig('gate_count_-2.png', bbox_inches='tight')
plt.show()
