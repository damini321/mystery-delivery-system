import json
import math
import os


def calculate_distance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find_nearest_agent(warehouse_location, agents):

    nearest_agent = None
    minimum_distance = float("inf")

    for agent_id, agent_location in agents.items():

        distance = calculate_distance(
            warehouse_location,
            agent_location
        )

        if distance < minimum_distance:

            minimum_distance = distance
            nearest_agent = agent_id

    return nearest_agent


def simulate_delivery(data):

    warehouses_data = data["warehouses"]
    agents_data = data["agents"]
    packages = data["packages"]

    # ------------------------------------------
    # Convert warehouses to dictionary
    # ------------------------------------------
    if isinstance(warehouses_data, list):

        warehouses = {}

        for warehouse in warehouses_data:

            warehouses[warehouse["id"]] = warehouse["location"]

    else:

        warehouses = warehouses_data

    # ------------------------------------------
    # Convert agents to dictionary
    # ------------------------------------------
    if isinstance(agents_data, list):

        agents = {}

        for agent in agents_data:

            agents[agent["id"]] = agent["location"]

    else:

        agents = agents_data

    # ------------------------------------------
    # Initialize report
    # ------------------------------------------
    report = {}

    for agent_id in agents.keys():

        report[agent_id] = {
            "packages_delivered": 0,
            "total_distance": 0.0,
            "efficiency": 0.0
        }

    # ------------------------------------------
    # Process packages
    # ------------------------------------------
    for package in packages:

        # Support both keys
        if "warehouse" in package:
            warehouse_id = package["warehouse"]
        else:
            warehouse_id = package["warehouse_id"]

        destination = package["destination"]

        warehouse_location = warehouses[warehouse_id]

        nearest_agent = find_nearest_agent(
            warehouse_location,
            agents
        )

        agent_location = agents[nearest_agent]

        distance_to_warehouse = calculate_distance(
            agent_location,
            warehouse_location
        )

        distance_to_destination = calculate_distance(
            warehouse_location,
            destination
        )

        total_distance = (
            distance_to_warehouse +
            distance_to_destination
        )

        report[nearest_agent]["packages_delivered"] += 1

        report[nearest_agent]["total_distance"] += total_distance

        agents[nearest_agent] = destination

    # ------------------------------------------
    # Calculate efficiency
    # ------------------------------------------
    best_agent = None
    best_efficiency = float("inf")

    for agent_id, details in report.items():

        delivered = details["packages_delivered"]

        if delivered > 0:

            efficiency = (
                details["total_distance"] / delivered
            )

            details["total_distance"] = round(
                details["total_distance"], 2
            )

            details["efficiency"] = round(
                efficiency, 2
            )

            if efficiency < best_efficiency:

                best_efficiency = efficiency
                best_agent = agent_id

    report["best_agent"] = best_agent

    return report

def save_report(report):

    with open("report.json", "w") as file:

        json.dump(report, file, indent=4)


def main():

    filename = input(
        "Enter JSON filename: "
    )

    if filename == "base_case.json":

        filepath = filename

    else:

        filepath = os.path.join(
            "Python Assignment(Delivery System Test Cases)",
            filename
        )

    if not os.path.exists(filepath):

        print("File not found!")
        return

    try:

        with open(filepath, "r") as file:

            data = json.load(file)

        report = simulate_delivery(data)

        print("\nFINAL REPORT\n")

        print(json.dumps(report, indent=4))

        save_report(report)

        print("\nReport saved as report.json")

    except Exception as e:

        print("Error:", str(e))


if __name__ == "__main__":

    main()