import matplotlib.pyplot as plt
import numpy as np

# Define the months of the year
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Define the sales data for each product
product_a_sales = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100]
product_b_sales = [800, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400]
product_c_sales = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]

# Create the plot
plt.figure(figsize=(10, 6))  # Optional: Set the figure size

plt.plot(months, product_a_sales, label='Product A', color='y', linestyle='-')
plt.plot(months, product_b_sales, label='Product B', color='g', linestyle='--')
plt.plot(months, product_c_sales, label='Product C', color='r', linestyle=':')

plt.title('Sales Performance')
plt.xlabel('Month')
plt.ylabel('Sales in Dollars')
plt.legend()  # Show legend with labels for each product

# Display the plot
plt.grid(True)  # Optional: Show grid lines
plt.show()
