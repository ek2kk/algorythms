# Пример жадного алгоритма
# Необходимо набрать достаточно станций, чтобы покрыть все необходимые штаты
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}  # Штаты, которые надо пократь
stations = {"kone": {"id", "nv", "ut"},  # Станции и штаты, покрываемые ими
            "ktwo": {"wa", "id", "mt"},
            "kthree": {"or", "nv", "са"},
            "kfour": {"nv", "ut"},
            "kfive": {"ca", "az"}}
final_stations = set()  # Используем сет для того, чтобы не хранились дубликаты

while states_needed:  # на каждой итерации подбираем станцию, которая покроет наибольшее количество непокрытых штатов
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print(final_stations)
