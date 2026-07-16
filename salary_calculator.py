def calculate_salary(basic_salary: float) -> dict:
    """
    Calculate employee salary components.

    HRA = 20% of basic salary
    DA = 10% of basic salary
    PF = 12% of basic salary
    """

    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    pf = basic_salary * 0.12

    gross_salary = basic_salary + hra + da
    net_salary = gross_salary - pf

    return {
        "basic_salary": basic_salary,
        "hra": hra,
        "da": da,
        "pf": pf,
        "gross_salary": gross_salary,
        "net_salary": net_salary
    }


def main() -> None:
    print("=" * 40)
    print("       EMPLOYEE SALARY CALCULATOR")
    print("=" * 40)

    try:
        basic_salary = float(input("Enter employee basic salary: "))

        if basic_salary <= 0:
            print("Basic salary must be greater than zero.")
            return

        salary = calculate_salary(basic_salary)

        print("\nSalary Details")
        print("-" * 40)
        print(f"Basic Salary : ₹{salary['basic_salary']:.2f}")
        print(f"HRA (20%)    : ₹{salary['hra']:.2f}")
        print(f"DA (10%)     : ₹{salary['da']:.2f}")
        print(f"PF (12%)     : ₹{salary['pf']:.2f}")
        print("-" * 40)
        print(f"Gross Salary : ₹{salary['gross_salary']:.2f}")
        print(f"Net Salary   : ₹{salary['net_salary']:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric salary.")


if __name__ == "__main__":
    main()