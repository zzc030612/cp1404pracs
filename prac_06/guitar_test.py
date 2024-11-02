from prac_06.guitar import Guitar

print(Guitar("Gibson L-5 CES", 1924, 92500).get_age()) # - Expected 100. Got 100
print(Guitar("Another Guitar", 2015, 120).get_age()) # - Expected 9. Got 9
print(Guitar("Gibson L-5 CES", 1924, 92500).is_vintage()) # - Expected True. Got True
print(Guitar("Another Guitar", 2015, 120).is_vintage()) # - Expected False. Got False