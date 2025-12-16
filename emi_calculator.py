def calculate_emi(principal, annual_rate, tenure_years):
    """
    Calculate EMI for a loan
    """
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
          ((1 + monthly_rate) ** tenure_months - 1)

    return emi


if __name__ == "__main__":
    print("==== EMI Calculator ====")

    principal = float(input("Enter loan amount (₹): "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    tenure_years = int(input("Enter loan tenure (years): "))

    emi = calculate_emi(principal, annual_rate, tenure_years)

    print(f"\nMonthly EMI: ₹{emi:.2f}")
