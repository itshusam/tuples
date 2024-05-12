def format(itineraries):
    result = ""
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        result += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return result

# Test the function
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted = format(itineraries)
print(formatted)