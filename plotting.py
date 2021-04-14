"""Plot functions """

import pandas as pd
import matplotlib.pyplot as plt


def plot_crash_detections(
    start_date,
    end_date,
    threshold,
    distances,
    time_index_derivs,
    price_resampled_derivs,
    metric_name
):

    # calculate rolling mean, min, max of homological derivatives
    rolled_mean_h = pd.Series(distances).rolling(20, min_periods=1).mean()
    rolled_min_h = (
        pd.Series(distances)
        .rolling(len(distances), min_periods=1)
        .min()
    )
    rolled_max_h = (
        pd.Series(distances)
        .rolling(len(distances), min_periods=1)
        .max()
    )

    # normalise the time series values to lies within [0, 1]
    probability_of_crash_h = (rolled_mean_h - rolled_min_h) / (
        rolled_max_h - rolled_min_h
    )

    # define time intervals to plots
    is_date_in_interval = (time_index_derivs > pd.Timestamp(start_date)) & (
        time_index_derivs < pd.Timestamp(end_date)
    )
    probability_of_crash_h_region = probability_of_crash_h[is_date_in_interval]
    time_index_region = time_index_derivs[is_date_in_interval]
    resampled_close_price_region = price_resampled_derivs.loc[is_date_in_interval]

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 2, 1)
    plt.plot(time_index_region, probability_of_crash_h_region, color="#1f77b4")
    plt.axhline(y=threshold, linewidth=2, color='#ff7f0e', linestyle='--', label='Threshold')
    plt.title(f"Crash Probability Based on {metric_name}")
    plt.legend(loc="best", prop={"size": 10},)

    plt.subplot(1, 2, 2)
    plt.plot(
        resampled_close_price_region[probability_of_crash_h_region.values > threshold],
        '#ff7f0e', marker='.', linestyle='None', markersize=4
    )
    plt.plot(
        resampled_close_price_region[probability_of_crash_h_region.values <= threshold],
        color="#1f77b4", marker='.', linestyle='None', markersize=4
    )

    plt.title("Close Price")
    plt.legend(
        [
            "Crash probability > {0}%".format(int(threshold * 100)),
            "Crash probability ≤ {0}%".format(int(threshold * 100)),
        ],
        loc="best",
        prop={"size": 10},
    )
    plt.savefig(f'./images/crash_{metric_name}.png')
    plt.show()
    
    
def plot_crash_comparisons(
    start_date,
    end_date,
    threshold,
    distances_1,
    distances_2,
    time_index_derivs,
    price_resampled_derivs,
):

    # calculate rolling mean, min, max of homological derivatives
    rolled_mean_1 = pd.Series(distances_1).rolling(20, min_periods=1).mean()
    rolled_min_1 = (
        pd.Series(distances_1)
        .rolling(len(distances_1), min_periods=1)
        .min()
    )
    rolled_max_1 = (
        pd.Series(distances_1)
        .rolling(len(distances_1), min_periods=1)
        .max()
    )

    # normalise the time series values to lies within [0, 1]
    probability_of_crash_1 = (rolled_mean_1 - rolled_min_1) / (
        rolled_max_1 - rolled_min_1
    )
    
    # calculate rolling mean, min, max of homological derivatives
    rolled_mean_2 = pd.Series(distances_2).rolling(20, min_periods=1).mean()
    rolled_min_2 = (
        pd.Series(distances_2)
        .rolling(len(distances_2), min_periods=1)
        .min()
    )
    rolled_max_2 = (
        pd.Series(distances_2)
        .rolling(len(distances_2), min_periods=1)
        .max()
    )

    # normalise the time series values to lies within [0, 1]
    probability_of_crash_2 = (rolled_mean_2 - rolled_min_2) / (
        rolled_max_2 - rolled_min_2
    )

    # define time intervals to plots
    is_date_in_interval = (time_index_derivs > pd.Timestamp(start_date)) & (
        time_index_derivs < pd.Timestamp(end_date)
    )
    probability_of_crash_1_region = probability_of_crash_1[is_date_in_interval]
    probability_of_crash_2_region = probability_of_crash_2[is_date_in_interval]

    time_index_region = time_index_derivs[is_date_in_interval]
    resampled_close_price_region = price_resampled_derivs.loc[is_date_in_interval]

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 2, 1)
    plt.plot(
        resampled_close_price_region[probability_of_crash_1_region.values > threshold],
        '#ff7f0e', marker='.', linestyle='None', markersize=4
    )
    plt.plot(
        resampled_close_price_region[probability_of_crash_1_region.values <= threshold],
        "#1f77b4", marker='.', linestyle='None', markersize=4
    )

    plt.title("Baseline Detector")
    plt.ylabel('Close Price', fontsize=12)
    plt.legend(
        [
            "Crash probability > {0}%".format(int(threshold * 100)),
            "Crash probability ≤ {0}%".format(int(threshold * 100)),
        ],
        loc="best",
        prop={"size": 10},
    )

    plt.subplot(1, 2, 2)
    plt.plot(
        resampled_close_price_region[probability_of_crash_2_region.values > threshold],
        '#ff7f0e', marker='.', linestyle='None', markersize=4
    )
    plt.plot(
        resampled_close_price_region[probability_of_crash_2_region.values <= threshold],
        "#1f77b4", marker='.', linestyle='None', markersize=4
    )

    plt.title('Topological Detector')
    plt.legend(
        [
            "Crash probability > {0}%".format(int(threshold * 100)),
            "Crash probability ≤ {0}%".format(int(threshold * 100)),
        ],
        loc="best",
        prop={"size": 10},
    )

    plt.savefig('./images/crash_comparison.png')
    plt.show()
