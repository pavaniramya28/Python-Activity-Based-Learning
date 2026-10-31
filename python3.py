
"""
Case Study 13: ATM Transaction Sequence Simulation

Description:
Simulates deposits and withdrawals, validates transactions,
enforces withdrawal limits, maintains account balance,
and generates a transaction summary.
"""

# ATM transaction limits
MIN_WITHDRAWAL = 100
MAX_WITHDRAWAL = 10000


def read_integer(prompt):
    """Accept and validate non-negative integer input."""
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Invalid input. Enter a non-negative amount.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def process_transaction(transaction_type, amount, balance):
    """Process a deposit or withdrawal transaction."""

    transaction_type = transaction_type.upper()

    if amount <= 0:
        return balance, "REJECTED", "Amount must be positive."

    if transaction_type == "DEPOSIT":
        balance += amount
        return balance, "SUCCESS", "Deposit completed."

    elif transaction_type == "WITHDRAWAL":

        if amount < MIN_WITHDRAWAL:
            return balance, "REJECTED", "Below minimum withdrawal limit."

        if amount > MAX_WITHDRAWAL:
            return balance, "REJECTED", "Exceeds maximum withdrawal limit."

        if amount > balance:
            return balance, "REJECTED", "Insufficient account balance."

        balance -= amount
        return balance, "SUCCESS", "Withdrawal completed."

    else:
        return balance, "REJECTED", "Invalid transaction type."


def display_summary(initial_balance, balance, history,
                    total_deposits, total_withdrawals,
                    successful, rejected):
    """Display complete ATM transaction summary."""

    print("\n" + "=" * 85)
    print("                    ATM TRANSACTION SUMMARY")
    print("=" * 85)

    print(
        f"{'No.':<6}{'Type':<16}{'Amount':>12}"
        f"{'Status':>14}{'Balance':>15}"
    )

    print("-" * 85)

    for transaction in history:
        print(
            f"{transaction['number']:<6}"
            f"{transaction['type']:<16}"
            f"{transaction['amount']:>12}"
            f"{transaction['status']:>14}"
            f"{transaction['balance']:>15}"
        )
        if transaction["reason"]:
            print(f"      Reason: {transaction['reason']}")

    print("-" * 85)
    print(f"Initial Balance          : Rs. {initial_balance}")
    print(f"Total Deposits           : Rs. {total_deposits}")
    print(f"Total Withdrawals        : Rs. {total_withdrawals}")
    print(f"Successful Transactions  : {successful}")
    print(f"Rejected Transactions    : {rejected}")
    print(f"Final Account Balance    : Rs. {balance}")
    print("=" * 85)


def main():
    """Main function to execute the ATM simulation."""

    print("=" * 55)
    print("             ATM TRANSACTION SYSTEM")
    print("=" * 55)

    initial_balance = read_integer(
        "Enter initial account balance: Rs. "
    )

    balance = initial_balance

    total_deposits = 0
    total_withdrawals = 0
    successful = 0
    rejected = 0

    history = []

    transaction_count = read_integer(
        "Enter number of transactions: "
    )

    for index in range(1, transaction_count + 1):

        print(f"\nTransaction {index}")
        print("1. Deposit")
        print("2. Withdrawal")

        choice = input("Select transaction type: ").strip()

        if choice == "1":
            transaction_type = "DEPOSIT"

        elif choice == "2":
            transaction_type = "WITHDRAWAL"

        else:
            transaction_type = "INVALID"

        amount = read_integer("Enter transaction amount: Rs. ")

        previous_balance = balance

        balance, status, reason = process_transaction(
            transaction_type, amount, balance
        )

        if status == "SUCCESS":
            successful += 1

            if transaction_type == "DEPOSIT":
                total_deposits += amount
            else:
                total_withdrawals += amount

        else:
            rejected += 1

        history.append({
            "number": index,
            "type": transaction_type,
            "amount": amount,
            "status": status,
            "balance": balance,
            "reason": reason
        })

        print(f"Transaction Status : {status}")
        print(f"Message            : {reason}")
        print(f"Available Balance  : Rs. {balance}")

    display_summary(
        initial_balance,
        balance,
        history,
        total_deposits,
        total_withdrawals,
        successful,
        rejected
    )


if __name__ == "__main__":
    main()
