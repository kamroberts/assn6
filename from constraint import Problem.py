from constraint import Problem

# Create a new constraint problem
problem = Problem()

# Add variables for each person, indicating whether they're a knight (1) or a knave (0)
names = ["Bozo", "Alice", "Zippy", "Marge", "Zoey"]
problem.addVariables(names, [0, 1])

# Add constraints for each person's statement
problem.addConstraint(lambda b, z: b == (z == 0), ("Bozo", "Zippy"))   # Bozo states that Zippy is a knave
problem.addConstraint(lambda b, z: b == (z == 0), ("Bozo", "Zoey"))   # Bozo states that Zoey is a knave

problem.addConstraint(lambda a, z: a == (a == 1 and z == 0), ("Alice", "Zoey"))   # Alice states that she is a knight and Zoey is a knave

problem.addConstraint(lambda z, m, a: z == ((m == 1) or (a == 1)), ("Zippy", "Marge", "Alice"))   # Zippy states that at least one of the following is true: Marge is a knight or Alice is a knight

problem.addConstraint(lambda m, b: m == (b == 1), ("Marge", "Bozo"))   # Marge states it is false that Bozo is a knave

problem.addConstraint(lambda z, m, b: z == ((m == 1) or (b == 0)), ("Zoey", "Marge", "Bozo"))   # Zoey states that at least one of the following is true: Marge is a knight or Bozo is a knave

# Solve the problem
solutions = problem.getSolutions()

# Print out the solutions
for solution in solutions:
    print("Solution:")
    for name, value in solution.items():
        print(f"{name} is a {'Knight' if value == 1 else 'Knave'}")