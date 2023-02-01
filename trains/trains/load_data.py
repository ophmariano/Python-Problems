def load_data_from_user_interface():
    print(f'Please input all the routes, Graphs separated by comma (AB5, AC3,...)')
    data_routes = input().upper()
    return ''.join(data_routes.split())
