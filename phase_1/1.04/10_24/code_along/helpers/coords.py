def calc_avg_coords(coords):
    """A function to calculate average cooridinates

    coords are a list of tuple floats that represent cooridinatess
    """
    # unpack list of coords & zip into two tuples into a list
    unzipped = list(zip(*coords))

    # sum up latitude
    avg_lat = sum(unzipped[0])
    # sum up longitude
    avg_lon = sum(unzipped[1])

    # calculate averages
    return avg_lat/len(coords), avg_lon/len(coords)


if __name__ == "__main__":
    coordinates = [
        (40.8499, -73.8769),
        (40.9125, -73.8478),
        (40.8165, -73.9025),
        (40.8790, -73.9060),
        (40.8450, -73.8320)
    ]

    print(calc_avg_coords(coordinates))

    print("Does this work?")
    print(calc_avg_coords(coordinates) == (40.86058, -73.87304))
