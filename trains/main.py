from trains.data_transformation import create_route_graph
from trains.load_data import load_data_from_user_interface
from trains.trip_shortest_distance import shortest_trip_distance
from trains.trip_distance_calculator import calculate_trip_distance
from trains.trips_with_distance_limitation import number_of_trips_within_max_distance
from trains.trips_with_station_limitation import number_of_trips_with_max_stops, number_of_trips_with_exactly_stops


def load_data_as_route_graph():
    data = load_data_from_user_interface()
    return create_route_graph(data)


def print_trip_distances(routes):
    trips = ['A-B-C', 'A-D', 'A-D-C', 'A-E-B-C-D', 'A-E-D']
    for trip in trips:
        try:
            print(calculate_trip_distance(trip, routes=routes))
        except Exception as error:
            print(error)
            stop()


def run():
    routes = load_data_as_route_graph()
    print_trip_distances(routes)
    print(number_of_trips_with_max_stops(start_station='C', end_station='C', max_stops=3, routes=routes))
    print(number_of_trips_with_exactly_stops(start_station='A', end_station='C', exactly_stops=4, routes=routes))
    print(shortest_trip_distance(start_station='A', end_station='C', routes=routes))
    print(shortest_trip_distance(start_station='B', end_station='B', routes=routes))
    print(number_of_trips_within_max_distance(start_station='C', end_station='C', max_distance=30, routes=routes))
    stop()


def stop():
    print(f'Thank you for using our railing system!')


if __name__ == '__main__':
    run()
