import pandas as pd
import numpy as np

Load dataset-3.csv
df3 = pd.read_csv('dataset-3.csv')

def calculate_distance_matrix(df)->pd.DataFrame():
     # df has columns: 'id_start', 'id_end', 'distance'
    distance_matrix = df.pivot(index='id_start', columns='id_end', values='distance').fillna(0)
    
    # Make the matrix symmetric
    distance_matrix = distance_matrix + distance_matrix.T
    np.fill_diagonal(distance_matrix.values, 0)
    
    # Calculate cumulative distances along known routes
    for col in distance_matrix.columns:
        for idx in distance_matrix.index:
            if distance_matrix.loc[idx, col] == 0:
                continue
            for intermediate_point in distance_matrix.columns:
                if distance_matrix.loc[idx, intermediate_point] == 0 or distance_matrix.loc[intermediate_point, col] == 0:
                    continue
                if distance_matrix.loc[idx, col] == 0 or distance_matrix.loc[idx, col] > distance_matrix.loc[idx, intermediate_point] + distance_matrix.loc[intermediate_point, col]:
                    distance_matrix.loc[idx, col] = distance_matrix.loc[idx, intermediate_point] + distance_matrix.loc[intermediate_point, col]

    return distance_matrix
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here

    return df


def unroll_distance_matrix(df)->pd.DataFrame():
     unrolled_df = distance_matrix.unstack().reset_index(name='distance')
    unrolled_df = unrolled_df[unrolled_df['id_start'] != unrolled_df['id_end']]
    return unrolled_df
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here

    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    avg_distance = unrolled_df[unrolled_df['id_start'] == reference_value]['distance'].mean()
    lower_threshold = 0.9 * avg_distance
    upper_threshold = 1.1 * avg_distance
    
    selected_ids = unrolled_df[(unrolled_df['distance'] >= lower_threshold) & (unrolled_df['distance'] <= upper_threshold)]['id_start'].unique()
    return sorted(selected_ids)
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here

    return df


def calculate_toll_rate(df)->pd.DataFrame():
    toll_rates = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}
    
    for vehicle_type in toll_rates.keys():
        unrolled_df[vehicle_type] = unrolled_df['distance'] * toll_rates[vehicle_type]
    
    return unrolled_df
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    # Create time ranges
    time_ranges = [ {'start': '00:00:00', 'end': '10:00:00', 'discount_factor': 0.8},{'start': '10:00:00', 'end': '18:00:00', 'discount_factor': 1.2},{'start': '18:00:00', 'end': '23:59:59', 'discount_factor': 0.8}]

    # Apply discount factors based on time ranges
    unrolled_df['start_day'] = pd.to_datetime(unrolled_df['start_day']).dt.day_name()
    unrolled_df['end_day'] = pd.to_datetime(unrolled_df['end_day']).dt.day_name()
    
    for time_range in time_ranges:
        mask = (unrolled_df['start_time'] >= pd.to_datetime(time_range['start']).time()) & (unrolled_df['end_time'] <= pd.to_datetime(time_range['end']).time())
        unrolled_df.loc[mask, ['moto', 'car', 'rv', 'bus', 'truck']] *= time_range['discount_factor']

    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # distance_matrix = calculate_distance_matrix(df3)
unrolled_df = unroll_distance_matrix(distance_matrix)
selected_ids = find_ids_within_ten_percentage_threshold(unrolled_df, reference_value=1)
toll_rate_df = calculate_toll_rate(unrolled_df)
time_based_toll_rates_df = calculate_time_based_toll_rates(unrolled_df)

    return df
