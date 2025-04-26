#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def simulate_transfer(
    votes={
        "A": 40150,
        "B": 20260,
        "C": 15470,
        "D": 10480,
        "E": 50590,
        "F": 10480,
    },
    base_name=Path(__file__).stem,
    nseats = 16,
):

    # Base vote counts for five parties: A, B, C, D, E
    # The values for A and B will change due to vote transfer
    base_votes = votes

    # Number of steps in the simulation (from all votes with A to all with B)
    steps = base_votes['A'] + base_votes['B']

    # Store seat distributions for each step
    seat_distributions = { k: [] for k in base_votes }
    seat_distributions["A+B"] = []

    def dhondt_allocation(votes_dict, total_seats):
        """Perform D'Hondt seat allocation."""
        parties = list(votes_dict.keys())
        quotients = []

        for party in parties:
            for i in range(1, total_seats + 1):
                quotients.append((votes_dict[party] / i, party))

        # Sort all quotients and take the top N
        top_quotients = sorted(quotients, reverse=True)[:total_seats]

        seat_counts = {party: 0 for party in parties}
        for _, party in top_quotients:
            seat_counts[party] += 1

        return seat_counts

    # Simulation: from full vote transfer A -> B to B -> A
    for t in np.linspace(0, 1, steps):
        votes = base_votes.copy()
        total_AB = base_votes["A"] + base_votes["B"]

        # Transfer fraction t from A to B
        votes["A"] = total_AB * (1 - t)
        votes["B"] = total_AB * t

        seats = dhondt_allocation(votes, nseats)

        for party in seat_distributions:
            if party == "A+B":
                seat_distributions["A+B"].append(seats["A"] + seats["B"])
            else:
                seat_distributions[party].append(seats[party])

    # Plotting the results
    x = np.linspace(0, 1, steps)
    parties = list(base_votes.keys())[:3]

    # Stackplot for seat distribution
    fig, ax = plt.subplots(figsize=(8, 4.5))
    labels_es = {
        "A": "Partido A",
        "B": "Partido B",
        "C": "Partido C",
        "D": "Partido D",
        "E": "Partido E",
        "F": "Partido F",
    }
    colors = {
        "A": "#1f77b4",
        "B": "#ff7f0e",
        "C": "#2ca02c",
        "D": "#d62728",
        "E": "#9467bd",
        "F": "#6794bd",
    }

    # Draw stacked areas
    y = np.vstack([ seat_distributions[p] for p in parties])
    ax.stackplot(x, y,
        labels=[labels_es[k] for k in parties],
        colors=[colors[k] for k in parties],
        step='post',
    )

    # Draw A+B line
    ax.plot(x,
        seat_distributions["A+B"],
        color="black",
        linestyle="--",
        linewidth=2,
        label="Total A + B",
        drawstyle='steps-post',
    )

    # Labels and legend
    ax.set_xlabel("Proporción de voto transferido de A a B")
    ax.set_ylabel("Número de escaños")
    ax.set_title("Simulación del reparto de escaños (método D'Hondt)")
    ax.legend(loc="upper right")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, nseats)

    plt.tight_layout()
    plt.savefig(base_name + ".svg")
    plt.savefig(base_name + ".pdf")
    plt.savefig(base_name + ".png", dpi=300)
    plt.show()


simulate_transfer(
    votes={
        "A": 40150,
        "B": 20260,
        "C": 15770,
        "D": 10480,
        "E": 50590,
        "F": 10480,
    },
    base_name = "transfer-ab-updown",
)
simulate_transfer(
    votes={
        "A": 40150,
        "B": 20260,
        "C": 15070, # this changes
        "D": 10480,
        "E": 50590,
        "F": 10480,
    },
    base_name = "transfer-ab-plane",
)
