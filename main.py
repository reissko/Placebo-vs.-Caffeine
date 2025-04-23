import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data for Placebo and Caffeine RPE means and standard deviations
placebo_rpe_means = [9.27, 12.07, 11.67, 18.11, 13.93]
placebo_rpe_sds = [1.03, 1.17, 1.89, 2.39, 1.48]
caffeine_rpe_means = [9.8, 12.87, 11.4, 16.6, 12.07]
caffeine_rpe_sds = [1.15, 1.56, 1.63, 2.61, 1.32]

# Data for Placebo and Caffeine Heart Rate means and standard deviations
placebo_hr_means = [153, 156.2, 155.27, 148.07, 149.6]
placebo_hr_sds = [3.38, 4.59, 5.52, 4.08, 5.73]
caffeine_hr_means = [153.6, 149.27, 148.13, 145.6, 147.33]
caffeine_hr_sds = [2.82, 5.62, 5.56, 5.58, 5.88]

# Data for Placebo and Caffeine Systolic Blood Pressure means and standard deviations
placebo_bp_systolic_means = [141, 130.8, 124.27, 127.87, 128.4]
placebo_bp_systolic_sds = [10.64, 6.96, 5.62, 5.74, 8.48]
caffeine_bp_systolic_means = [134.4, 130.6, 128.6, 139.33, 140.93]
caffeine_bp_systolic_sds = [5.27, 5.75, 3.88, 8.30, 6.77]

# Data for Placebo and Caffeine Diastolic Blood Pressure means and standard deviations
placebo_bp_diastolic_means = [58.4, 57.6, 58.4, 67.07, 60.8]
placebo_bp_diastolic_sds = [4.16, 4.04, 5.19, 6.2, 6.86]
caffeine_bp_diastolic_means = [56.07, 50.4, 52.67, 55.07, 55.2]
caffeine_bp_diastolic_sds = [5.11, 7.62, 5.12, 3.84, 11.05]

# Exercise labels
exercises = ["Squats", "Rows", "Lat Raise", "Curls", "Leg Extensions"]

# Create a figure with four subplots (for RPE, Heart Rate, Systolic BP, and Diastolic BP)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Slightly offsetting the x-axis positions for caffeine data
offset = 0.2  # Adjust this value for different offset
x_pos_placebo = np.arange(len(exercises))
x_pos_caffeine = x_pos_placebo + offset  # Shift caffeine data to the right

# Plotting the RPE data (Placebo and Caffeine)
axes[0, 0].errorbar(x_pos_placebo, placebo_rpe_means, yerr=placebo_rpe_sds, fmt='o', capsize=5, label="Placebo", color='b')
axes[0, 0].errorbar(x_pos_caffeine, caffeine_rpe_means, yerr=caffeine_rpe_sds, fmt='o', capsize=5, label="Caffeine", color='r')

# Add labels and title for RPE plot
axes[0, 0].set_title("RPE Mean and Standard Deviation for Placebo vs Caffeine")
axes[0, 0].set_xlabel("Exercise")
axes[0, 0].set_ylabel("RPE (Rating of Perceived Effort)")
axes[0, 0].set_xticks(x_pos_placebo + offset / 2)  # Position x-ticks in between the two sets
axes[0, 0].set_xticklabels(exercises)
axes[0, 0].legend()

# Plotting the Heart Rate data (Placebo and Caffeine)
axes[0, 1].errorbar(x_pos_placebo, placebo_hr_means, yerr=placebo_hr_sds, fmt='o', capsize=5, label="Placebo", color='b')
axes[0, 1].errorbar(x_pos_caffeine, caffeine_hr_means, yerr=caffeine_hr_sds, fmt='o', capsize=5, label="Caffeine", color='r')

# Add labels and title for Heart Rate plot
axes[0, 1].set_title("Heart Rate Mean and Standard Deviation for Placebo vs Caffeine")
axes[0, 1].set_xlabel("Exercise")
axes[0, 1].set_ylabel("Heart Rate (Bpm)")
axes[0, 1].set_xticks(x_pos_placebo + offset / 2)  # Position x-ticks in between the two sets
axes[0, 1].set_xticklabels(exercises)
axes[0, 1].legend()

# Plotting the Systolic Blood Pressure data (Placebo and Caffeine)
axes[1, 0].errorbar(x_pos_placebo, placebo_bp_systolic_means, yerr=placebo_bp_systolic_sds, fmt='o', capsize=5, label="Placebo", color='b')
axes[1, 0].errorbar(x_pos_caffeine, caffeine_bp_systolic_means, yerr=caffeine_bp_systolic_sds, fmt='o', capsize=5, label="Caffeine", color='r')

# Add labels and title for Systolic Blood Pressure plot
axes[1, 0].set_title("Systolic BP Mean and Standard Deviation for Placebo vs Caffeine")
axes[1, 0].set_xlabel("Exercise")
axes[1, 0].set_ylabel("Systolic BP (mmHg)")
axes[1, 0].set_xticks(x_pos_placebo + offset / 2)  # Position x-ticks in between the two sets
axes[1, 0].set_xticklabels(exercises)
axes[1, 0].legend()

# Plotting the Diastolic Blood Pressure data (Placebo and Caffeine)
axes[1, 1].errorbar(x_pos_placebo, placebo_bp_diastolic_means, yerr=placebo_bp_diastolic_sds, fmt='o', capsize=5, label="Placebo", color='b')
axes[1, 1].errorbar(x_pos_caffeine, caffeine_bp_diastolic_means, yerr=caffeine_bp_diastolic_sds, fmt='o', capsize=5, label="Caffeine", color='r')

# Add labels and title for Diastolic Blood Pressure plot
axes[1, 1].set_title("Diastolic BP Mean and Standard Deviation for Placebo vs Caffeine")
axes[1, 1].set_xlabel("Exercise")
axes[1, 1].set_ylabel("Diastolic BP (mmHg)")
axes[1, 1].set_xticks(x_pos_placebo + offset / 2)  # Position x-ticks in between the two sets
axes[1, 1].set_xticklabels(exercises)
axes[1, 1].legend()

# Display the plots
plt.tight_layout()  # Adjust the layout to avoid overlap
plt.show()
