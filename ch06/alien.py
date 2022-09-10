#! /bin/python3

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    aliens.append({'color': 'green', 'points': 5, 'speed': 'slow'})

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how manay aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

