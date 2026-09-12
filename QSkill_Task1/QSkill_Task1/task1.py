import pandas as pd
import matplotlib.pyplot as plt



# 1. LOAD CSV FILE


data = pd.read_csv("vehicle_rental_data.csv")

print("===== VEHICLE RENTAL DATASET =====")
print(data)



# 2. BASIC DATA ANALYSIS


print("\n===== BASIC INFORMATION =====")
print(data.info())

print("\n===== STATISTICAL SUMMARY =====")
print(data.describe())



# 3. AVERAGE ANALYSIS


print("\n===== AVERAGE VALUES =====")

print("Average Rental Days:",
      round(data["Rental_Days"].mean(), 2))

print("Average Daily Rate:",
      round(data["Daily_Rate"].mean(), 2))

print("Average Total Rent:",
      round(data["Total_Rent"].mean(), 2))

print("Average Customer Rating:",
      round(data["Customer_Rating"].mean(), 2))



# 4. VEHICLE TYPE ANALYSIS


print("\n===== VEHICLE TYPE ANALYSIS =====")

vehicle_count = data["Vehicle_Type"].value_counts()

print(vehicle_count)

print("\nMost Rented Vehicle Type:",
      vehicle_count.idxmax())



# 5. CITY ANALYSIS


print("\n===== CITY ANALYSIS =====")

city_count = data["City"].value_counts()

print(city_count)

print("\nCity With Most Rentals:",
      city_count.idxmax())



# 6. BAR CHART


plt.figure(figsize=(10, 6))

vehicle_count.plot(kind="bar")

plt.title("Number of Rentals by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Number of Rentals")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# 7. SCATTER PLOT


plt.figure(figsize=(8, 6))

plt.scatter(
    data["Distance_Travelled"],
    data["Total_Rent"]
)

plt.title("Distance Travelled vs Total Rent")
plt.xlabel("Distance Travelled (km)")
plt.ylabel("Total Rent")

plt.tight_layout()
plt.show()



# 8. CORRELATION HEATMAP


correlation = data[
    [
        "Rental_Days",
        "Daily_Rate",
        "Total_Rent",
        "Customer_Rating",
        "Distance_Travelled"
    ]
].corr()

plt.figure(figsize=(9, 7))

plt.imshow(
    correlation,
    cmap="coolwarm",
    interpolation="nearest"
)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)


# Add values inside heatmap
for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(
            j,
            i,
            f"{correlation.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )


plt.title("Vehicle Rental Correlation Heatmap")

plt.tight_layout()
plt.show()



# 9. INSIGHTS AND OBSERVATIONS


print("\n===== INSIGHTS AND OBSERVATIONS =====")

print("1. The dataset contains vehicle rental information "
      "including vehicle type, city, rental days, daily rate, "
      "total rent, customer rating and distance travelled.")

print("2. The most frequently rented vehicle type is:",
      vehicle_count.idxmax())

print("3. The city with the highest number of rentals is:",
      city_count.idxmax())

print("4. The scatter plot helps analyze the relationship "
      "between distance travelled and total rental amount.")

print("5. The heatmap shows the correlation between "
      "rental days, daily rate, total rent, customer rating "
      "and distance travelled.")