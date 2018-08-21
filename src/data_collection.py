import googlemaps
from itertools import combinations
import pandas as pd

METERS_IN_MILE = 1609.34


def query_gmaps_api_for_one_way_driving_distance_and_duration(venue_names, google_maps_api_key):
    """
    Query Google Maps API for the one-way driving distance and duration
    between all combination pairs of venues from a list of venues.

    Parameters
    ----------
    venue_names : list
        A list of venue names.

    Returns
    -------
    distance_duration_data : dict
        A data dictionary with a list of venue 1 names, a list of venue
        2 names, a list of driving distances in miles, and a list of
        driving durations in seconds.

    Raises
    ------
    Exception : If the distance or duration between venue 1 and venue 2
    not found.

    """

    # Instantiate Google Maps API session
    gmaps = googlemaps.Client(google_maps_api_key)

    # Initialize data dictionary to hold values
    distance_duration_data = {
        'Venue 1': [],
        'Venue 2': [],
        'Distance (mi)': [],
        'Duration (s)': []
    }

    # Collect driving distance and duration data for each venue to venue combination
    for (venue_1, venue_2) in combinations(venue_names, 2):

        try:

            # Query Google Maps API for driving distance and duration
            trip = gmaps.distance_matrix(
                origins=[venue_1],
                destinations=[venue_2],
                mode="driving",
                units="metric")

            # Extract driving distance in meters and convert to miles
            distance_m = trip['rows'][0]['elements'][0]['distance']['value']
            distance_mi = round(distance_m / METERS_IN_MILE)

            # Extract driving duration in seconds
            duration_s = trip['rows'][0]['elements'][0]['duration']['value']

            # Add values to data dictionary
            distance_duration_data['Venue 1'].append(venue_1)
            distance_duration_data['Venue 2'].append(venue_2)
            distance_duration_data['Distance (mi)'].append(distance_mi)
            distance_duration_data['Duration (s)'].append(duration_s)

        except Exception:

            raise Exception("Error finding the distance between {} and {}.".format(venue_1, venue_2))

    return(distance_duration_data)


def convert_seconds_to_hhmm(seconds):
    """
    Convert a value from seconds to hours and minutes in HH:MM format.

    Parameters
    ----------
    seconds : float or int
        The number of seconds.

    Returns
    -------
    hhmm : str
        The number of hours and minutes in HH:MM format.

    """

    # Determine number of full minutes and remainder seconds
    minutes, seconds = divmod(seconds, 60)

    # Determine number of full hours and remainder minutes
    hours, minutes = divmod(minutes, 60)

    # Convert hours and minutes to HH:MM format
    hhmm = "{:d}:{:02d}".format(hours, minutes)

    return(hhmm)


def create_distance_and_duration_df(distance_duration_data):
    """
    Create a distance and duration DataFrame from a distance and
    duration data dictionary.

    Parameters
    ----------
    distance_duration_data : dict
        A data dictionary with a list of venue 1 names, a list of venue
        2 names, a list of driving distances in miles, and a list of
        driving durations in seconds.

    Returns
    -------
    distance_duration_df : pandas.core.frame.DataFrame
        A distance and duration DataFrame including venue 1, venue 2,
        distance (mi), duration (s), and duration (hhmm).

    """

    distance_duration_df = pd.DataFrame(distance_duration_data)

    column_order = [
        'Venue 1',
        'Venue 2',
        'Distance (mi)',
        'Duration (s)']

    distance_duration_df = distance_duration_df[column_order]

    distance_duration_df['Duration (hhmm)'] = distance_duration_df['Duration (s)'].apply(convert_seconds_to_hhmm)

    return(distance_duration_df)
