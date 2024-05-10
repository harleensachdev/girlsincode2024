class Item:
  def __init__(self, name, amount, place, zone,person):
      self.name = name
      self.amount = amount
      self.place = place
      self.zone = zone
      self.person = person

def read_inventory(filename):
  items = []
  with open(filename, 'r') as file:
      for line in file:
          parts = line.strip().split(', ')
          if len(parts) == 5:
              name, amount, place, _, person = parts
              item = Item(name, amount, place, person)
              items.append(item)
          else:
              print(f"Error: Invalid data format in line: {line.strip()}")
  return items

def allocate_resources(items):
  resources_by_person = {}
  for item in items:
      person = item.person
      resource = {'Name': item.name, 'Amount': item.amount, 'Place': item.place}
      if person in resources_by_person:
          resources_by_person[person].append(resource)
      else:
          resources_by_person[person] = [resource]
  return resources_by_person

def print_resources(resources_by_person):
  for person, resources in resources_by_person.items():
      print(f"Resources for {person}:")
      for resource in resources:
          print(f"Name: {resource['Name']}, Amount: {resource['Amount']}, Place: {resource['Place']}")
      print()

filename = "inventory.txt"
inventory = read_inventory(filename)
resources_by_person = allocate_resources(inventory)
print_resources(resources_by_person)
