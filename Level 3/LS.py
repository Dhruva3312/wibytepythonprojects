import random

def get_plural(name):
    return name + 's'

def generate_inventory(count, specs, master_dict):
    laptops = []
    for _ in range(count):
        laptop = {spec: random.choice(master_dict[spec + 's']) for spec in specs}
        laptops.append(laptop)
    return laptops

def collect_user_preferences(specs):
    print("\n--- Search Preferences ---")
    print("Enter your preferred value, or press Enter/type 'none' for no preference.")
    preferences = {}
    for spec in specs:
        response = input(f"Preferred {spec}: ").strip()
        if response.lower() in ['', 'none']:
            preferences[spec] = None
        else:
            preferences[spec] = response
    return preferences

def filter_laptops(laptops, preferences):
    matching_laptops = []
    for laptop in laptops:
        matches = True
        for spec, pref in preferences.items():
            if pref is not None and laptop[spec].lower() != pref.lower():
                matches = False
                break
        if matches:
            matching_laptops.append(laptop)
    return matching_laptops

def sort_laptops(laptops):
    print("\nSort results by Price?")
    print("1. Low to High")
    print("2. High to Low")
    print("3. No sorting")
    choice = input("Select an option (1-3): ").strip()

    if choice == '1':
        return sorted(laptops, key=lambda x: int(x['Price'].replace('INR ', '')))
    elif choice == '2':
        return sorted(laptops, key=lambda x: int(x['Price'].replace('INR ', '')), reverse=True)
    return laptops

def display_laptops(laptops, specs):
    print(f"\nFound {len(laptops)} laptop(s) matching your criteria:\n")
    if not laptops:
        return

    header = "".join([spec.ljust(14) for spec in specs])
    print(header)
    print("-" * len(header))

    for laptop in laptops:
        row = "".join([str(laptop[spec]).ljust(14) for spec in specs])
        print(row)

def main():
    specs = ['Brand', 'Model', 'CPU', 'Speed', 'RAM', 'Storage', 'Screensize', 'Price']
    plural_specs = list(map(get_plural, specs))
    
    master_dict = dict.fromkeys(plural_specs)
    master_dict['Brands'] = ['Dell', 'Asus', 'Acer', 'Lenovo', 'HP']
    master_dict['Models'] = ['AAA', 'BBB', 'CCC']
    master_dict['CPUs'] = ['Intel i5', 'Intel i7', 'AMD Ryzen']
    master_dict['Speeds'] = ['2 GHz', '3 GHz', '3.15 GHz', '3.8 GHz']
    master_dict['RAMs'] = ['2 GB', '4 GB', '8 GB', '16 GB']
    master_dict['Storages'] = ['128 GB', '256 GB', '512 GB', '1024 GB']
    master_dict['Screensizes'] = ['9 in', '12 in', '14.9 in', '17 in']
    master_dict['Prices'] = ['INR 20000', 'INR 30000', 'INR 40000']

    laptops_inventory = generate_inventory(60, specs, master_dict)

    print("========================================")
    print("    Welcome to WiByte Laptop Store    ")
    print("========================================")
    
    while True:
        preferences = collect_user_preferences(specs)
        filtered_results = filter_laptops(laptops_inventory, preferences)
        
        if filtered_results:
            filtered_results = sort_laptops(filtered_results)
        
        display_laptops(filtered_results, specs)

        refine = input("\nWould you like to refine your search? (yes/no): ").strip().lower()
        if refine not in ['yes', 'y']:
            print("\nThank you for visiting WiByte Laptop Store!")
            break

if __name__ == "__main__":
    main()