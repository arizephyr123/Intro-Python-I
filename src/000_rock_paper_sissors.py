# Create a RPS game

# type q to quit

# Create a REPL
wins = 0
losses = 0
ties = 0

choices = ['r', 'p', 's']

# LOOP
while True:
    print(f"Score: {wins} /{losses} /{ties}")

# READ
cmd = input("-> ")

# EVAL
cpu_cmd = random.choice(choices)
print

else:
    print
