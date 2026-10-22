# Kayleb "Xeon" Gonzalez
# CSC 3690 01 Chapter 2 Homework 2.7

import random

BITS = 5

def decode(h):
    return int(h, 2)

def fitness(h):
    x = decode(h)
    return x ** 2

def random_hypothesis():
    return ''.join(random.choice("01") for _ in range(BITS))

def select(H, fits):
    total = sum(fits)

    if total == 0:
        return random.choice(H)

    r = random.uniform(0, total)
    running = 0

    for h, f in zip(H, fits):
        running += f
        if running >= r:
            return h

    return H[-1]

def crossover(p1, p2, c=None):
    if c is None:
        c = random.randint(1, len(p1) - 1)

    child1 = p1[:c] + p2[c:]
    child2 = p2[:c] + p1[c:]

    return child1, child2

def mutate(h):
    i = random.randrange(len(h))

    flipped = "1" if h[i] == "0" else "0"

    return h[:i] + flipped + h[i + 1:]

def GA(fitness, theta, n, r_co, r_mu, max_gens=1000):
    H = [random_hypothesis() for _ in range(n)]

    fits = [fitness(h) for h in H]

    gen = 0

    while max(fits) < theta and gen < max_gens:
        H_next = []

        n_keep = round((1 - r_co) * n)

        for _ in range(n_keep):
            H_next.append(select(H, fits))

        n_pairs = round(r_co * n / 2)

        for _ in range(n_pairs):
            parent1 = select(H, fits)
            parent2 = select(H, fits)

            child1, child2 = crossover(parent1, parent2)

            H_next.append(child1)
            H_next.append(child2)

        n_mut = round(r_mu * n)

        for i in random.sample(range(n_mut), n_mut):
            H_next[i] = mutate(H_next[i])

        H = H_next

        fits = [fitness(h) for h in H]

        gen += 1

        print(f"Gen {gen:3d}: best={max(H, key=fitness)}" f"fitness={max(fits)}")

    return max(H, key=fitness), gen

best, generations = GA(
    fitness=fitness,
    theta=900,
    n=10,
    r_co=0.6,
    r_mu=0.1,
    max_gens=1000
)

if __name__ == "__main__":

    best, generations = GA(fitness, theta=961, n=10, r_co=0.6, r_mu=0.1)

    print(f"\nDone after {generations} generations.")
    print(f"Best: {best} -> x = {decode(best)}, fitness = {fitness(best)}")