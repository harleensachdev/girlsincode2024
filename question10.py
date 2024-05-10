age_groups = {"children": 200, "adults": 500, "elderly": 100}
available_resources = {"food": 2000, "water": 5000, "medicine": 300}
def allocateresources(age_groups, available_resources):
    allocation_plan = {}
    total_individuals = sum(age_groups.values())
    allocationperperson = {resource: available_resources[resource] / total_individuals for resource in available_resources}
    for age_group, num_individuals in age_groups.items():
        allocation_plan[age_group] = {resource: allocationperperson[resource] * num_individuals for resource in available_resources}
    return allocation_plan
allocation_plan = allocateresources(age_groups, available_resources)
for resource, allocations in allocation_plan.items():
    print(f"Allocation plan for {resource}:")
    for age_group, amount in allocations.items():
        print(f"{age_group}: {amount} units")
