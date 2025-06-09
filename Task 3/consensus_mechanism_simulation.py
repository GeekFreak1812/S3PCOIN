import random
from collections import Counter

def simulate_pow_consensus(miners):
    print("\n--- Simulating Proof-of-Work (PoW) ---")
    if not miners: return print("No miners available.")
    
    selected = max(miners, key=lambda m: m['power'])
    print(f"Selected Validator (PoW): {selected['name']} (Power: {selected['power']})")
    print("Logic: Chooses validator with highest simulated computational power.")
    return selected

def simulate_pos_consensus(stakers):
    print("\n--- Simulating Proof-of-Stake (PoS) ---")
    if not stakers: return print("No stakers available.")
    
    selected = max(stakers, key=lambda s: s['stake'])
    print(f"Selected Validator (PoS): {selected['name']} (Stake: {selected['stake']} S3P)")
    print("Logic: Chooses validator with highest cryptocurrency stake.")
    return selected

def simulate_dpos_consensus(delegates, voters):
    print("\n--- Simulating Delegated Proof-of-Stake (DPoS) ---")
    if not delegates or not voters: return print("Delegates or voters missing.")

    # Tally votes
    vote_counts = Counter(v['voted_for'] for v in voters)
    
    print("Delegate Vote Tally:", dict(vote_counts))

    if not vote_counts: return print("No votes tallied.")

    max_votes = max(vote_counts.values())
    top_delegates = [name for name, votes in vote_counts.items() if votes == max_votes]
    
    selected_name = random.choice(top_delegates)
    selected = next(d for d in delegates if d['name'] == selected_name) # Find the full delegate object

    print(f"Selected Validator (DPoS): {selected['name']} (Total Votes: {max_votes})")
    print("Logic: Token holders vote for delegates; delegate(s) with most votes are selected.")
    return selected

# --- Mock Objects ---
num_validators = 3 # Can change this to easily adjust number of mock validators

miners = [{"name": f"Miner {chr(65+i)}", "power": random.randint(100, 1000)} for i in range(num_validators)]
stakers = [{"name": f"Staker {chr(88+i)}", "stake": random.randint(1000, 10000)} for i in range(num_validators)]
delegates = [{"name": f"Delegate {['Alpha', 'Beta', 'Gamma'][i]}"} for i in range(num_validators)]

voters = [
    {"name": f"Voter {i+1}", "voted_for": random.choice([d['name'] for d in delegates]), "vote_weight": 1} # Simplified vote_weight to 1 for brevity
    for i in range(num_validators * 2) # More voters than delegates
]

# --- Simulate Consensus Mechanisms ---
selected_pow_validator = simulate_pow_consensus(miners)
selected_pos_validator = simulate_pos_consensus(stakers)
selected_dpos_validator = simulate_dpos_consensus(delegates, voters)

print("\n--- Consensus Summary ---")
print(f"PoW: {selected_pow_validator['name'] if selected_pow_validator else 'N/A'}")
print(f"PoS: {selected_pos_validator['name'] if selected_pos_validator else 'N/A'}")
print(f"DPoS: {selected_dpos_validator['name'] if selected_dpos_validator else 'N/A'}")