from datetime import datetime, timedelta

from scripts.analytics import (
    get_total_orders,
    get_total_revenue,
    get_unique_customers,
    get_top_products,
    compare_previous_period
)
from scripts.utils import (
    validate_date_range,
    print_heading
)



def get_previous_period(start_date, end_date):

    start = datetime.strptime(
        start_date,
        "%Y-%m-%d"
    )

    end = datetime.strptime(
        end_date,
        "%Y-%m-%d"
    )

    days = (end - start).days

    previous_end = start - timedelta(days=1)

    previous_start = previous_end - timedelta(days=days)

    return (
        previous_start.strftime("%Y-%m-%d"),
        previous_end.strftime("%Y-%m-%d")
    )


def generate_report():

    print("\nE-Commerce Order Analytics Report\n")

    report_type = input(
        "Enter Report Type (Daily / Weekly / Monthly): "
    )

    start_date = input(
        "Enter Start Date (YYYY-MM-DD): "
    )

    end_date = input(
        "Enter End Date (YYYY-MM-DD): "
    )


    if not validate_date_range(
    start_date,
    end_date
    ):

        print("Invalid date range.")

        return


    previous_start, previous_end = get_previous_period(
        start_date,
        end_date
    )

    total_orders = get_total_orders(
        start_date,
        end_date
    )

    total_revenue = get_total_revenue(
        start_date,
        end_date
    )

    unique_customers = get_unique_customers(
        start_date,
        end_date
    )

    top_products = get_top_products(
        start_date,
        end_date
    )

    comparison = compare_previous_period(
        start_date,
        end_date,
        previous_start,
        previous_end
    )

    print_heading(
        f"{report_type.upper()} REPORT"
    )

    print("\nTotal Orders")
    print(total_orders)

    print("\nTotal Revenue")
    print(total_revenue)

    print("\nUnique Customers")
    print(unique_customers)

    print("\nTop 3 Products")
    print(top_products)

    print("\nPrevious Period Comparison")
    print(comparison)

    print("\nReport generated successfully.")


def main():

    generate_report()


if __name__ == "__main__":

    main()