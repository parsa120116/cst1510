def load_accounts(filepath):
    """Read the accounts file into a dict: id -> {"name": ..., "balance": ...}."""
    accounts = {}
    with open(filepath) as file:
        for line in file:
            parts = line.split()
            if len(parts) != 3:
                continue                       # skip empty or broken lines
            account_id = int(parts[0])
            accounts[account_id] = {"name": parts[1], "balance": float(parts[2])}
    return accounts


try:
    accounts = load_accounts("DATA/accounts1.txt")
except FileNotFoundError:
    print("Sorry, the accounts file was not found. Check that DATA/accounts1.txt exists.")
    accounts = {}

if accounts:
    print(f"{'ID':<6}{'Name':<12}{'Balance':>10}")
    print("-" * 28)
    total = 0
    for account_id, info in accounts.items():
        print(f"{account_id:<6}{info['name']:<12}{info['balance']:>10.2f}")
        total += info["balance"]
    print("-" * 28)
    print(f"{'Total':<18}{total:>10.2f}")

    richest_id = None
    for account_id, info in accounts.items():
        if richest_id is None or info["balance"] > accounts[richest_id]["balance"]:
            richest_id = account_id
    richest = accounts[richest_id]
    print(f"Highest balance: {richest['name']} (account {richest_id}, {richest['balance']:.2f})")
