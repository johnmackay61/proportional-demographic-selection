import random
import pandas as pd
import numpy as np
from collections import Counter

# Define population proportions based on census-like data
POPULATION_PROPORTIONS = {
    "sex": {"male": 0.49, "female": 0.51},
    "age_group": {"18-30": 0.3, "31-50": 0.4, "51+": 0.3},
    "income": {"low": 0.4, "middle": 0.4, "high": 0.2},
    "family_status": {"single": 0.4, "married": 0.5, "other": 0.1},
}

# Generate synthetic population
def generate_population(size=10000):
    population = []
    for _ in range(size):
        person = {
            "sex": random.choices(list(POPULATION_PROPORTIONS["sex"].keys()), weights=POPULATION_PROPORTIONS["sex"].values())[0],
            "age_group": random.choices(list(POPULATION_PROPORTIONS["age_group"].keys()), weights=POPULATION_PROPORTIONS["age_group"].values())[0],
            "income": random.choices(list(POPULATION_PROPORTIONS["income"].keys()), weights=POPULATION_PROPORTIONS["income"].values())[0],
            "family_status": random.choices(list(POPULATION_PROPORTIONS["family_status"].keys()), weights=POPULATION_PROPORTIONS["family_status"].values())[0],
        }
        population.append(person)
    return pd.DataFrame(population)

# Compute selection probabilities (inverse proportional representation)
def compute_selection_weights(df):
    weight_factors = {}
    for col in POPULATION_PROPORTIONS.keys():
        counts = df[col].value_counts(normalize=True)
        weight_factors[col] = {k: 1/v for k, v in counts.items()}
    
    weights = []
    for _, row in df.iterrows():
        weight = np.mean([weight_factors[col][row[col]] for col in POPULATION_PROPORTIONS.keys()])
        weights.append(weight)
    
    df["weight"] = weights
    return df

# Select legislators based on computed weights
def select_legislators(df, num_seats=100):
    selected = df.sample(n=num_seats, weights=df["weight"], replace=False)
    return selected

# Run simulation
population_df = generate_population()
population_df = compute_selection_weights(population_df)
selected_legislators = select_legislators(population_df)

# Show selection distribution
print(Counter(selected_legislators["sex"]))
print(Counter(selected_legislators["age_group"]))
print(Counter(selected_legislators["income"]))
print(Counter(selected_legislators["family_status"]))
