import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import plotly.express as px


def visualize_schedule(schedule, crops, time_periods, plots):
    # Ensure the schedule is numeric and handle NaN values
    schedule_df = pd.DataFrame(schedule, index=plots, columns=time_periods)

    # Check for NaN values and fill them if necessary
    if schedule_df.isnull().values.any():
        print("Warning: NaN values detected in schedule. Filling with 0.")
        schedule_df = schedule_df.fillna(0)  # Or use another strategy like interpolation

    # Convert the DataFrame to a numeric type if not already
    schedule_df = schedule_df.astype(float)

    # Create a heatmap using seaborn
    plt.figure(figsize=(20, 15))
    sns.heatmap(schedule_df, annot=True, fmt=".1f", cmap="viridis", cbar_kws={'label': 'Crop Index'})
    plt.title("Crop Rotation Schedule")
    plt.xlabel("Time Period (Months)")
    plt.ylabel("Plots")
    plt.xticks(ticks=np.arange(len(time_periods)) + 0.5, labels=time_periods, rotation=90)
    plt.yticks(ticks=np.arange(len(plots)) + 0.5, labels=[clean_plot_name(p) for p in plots], rotation=0)
    plt.show()


def clean_plot_name(plot):
    return plot.replace('_', ' ').title()


def create_rotation_visualization(schedule, crops, plots):
    fig = px.imshow(
        schedule,
        labels=dict(x="Time Period (Months)", y="Plots", color="Crop Index"),
        x=[f"Month {i + 1}" for i in range(schedule.shape[1])],
        y=[clean_plot_name(plot) for plot in plots],
        aspect="auto"
    )

    crop_names = [crop.replace('.', ' ').title() for crop in crops]
    fig.update_layout(
        title="Crop Rotation Schedule",
        xaxis_title="Time Period (Months)",
        yaxis_title="Plots",
        coloraxis_colorbar=dict(
            title="Crop Index",
            tickvals=np.arange(len(crops)),
            ticktext=crop_names
        )
    )
    fig.show()
