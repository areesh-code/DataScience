import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
july_births = [12, 15, 11, 9, 1, 9, 21]

df_july = pd.DataFrame({
    "Day": days,
    "Births": july_births
})

print("July Data:")
print(df_july)

plt.figure()
plt.plot(df_july["Day"], df_july["Births"],
         marker='o', linestyle='-', linewidth=2, color='blue', label='July')

plt.title("Birth Rate - July")
plt.xlabel("Days")
plt.ylabel("Number of Births")
plt.legend()
plt.grid()
plt.show()

august_births = [17, 5, 2, 11, 1, 8, 29]

df_august = pd.DataFrame({
    "Day": days,
    "Births": august_births
})

print("\nAugust Data:")
print(df_august)

plt.figure()
plt.plot(df_august["Day"], df_august["Births"],
         marker='s', linestyle='--', linewidth=2, color='red', label='August')

plt.title("Birth Rate - August")
plt.xlabel("Days")
plt.ylabel("Number of Births")
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(days, july_births,
         marker='o', linestyle='-', linewidth=2, color='blue', label='July')

plt.plot(days, august_births,
         marker='s', linestyle='--', linewidth=2, color='red', label='August')

plt.title("Comparison of Birth Rates (July vs August)")
plt.xlabel("Days")
plt.ylabel("Number of Births")
plt.legend()
plt.grid()
plt.show()

x = np.arange(1, 11)
y = 6*(x**2) + x + 1

plt.figure()
plt.plot(x, y,
         marker='o', linestyle='-', linewidth=2, color='green',
         label='y = 6x^2 + x + 1')

plt.title("Plot of y = 6x^2 + x + 1")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
plt.grid()
plt.show()