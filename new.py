from calcs import toa_proposal as toa
import matplotlib.pyplot as plt


def main():

    # Example usage of the functions in the toa_proposal module
    invo = 500  # Example invocation number
    # toa.print_purple_breakdown(invo)

    purple_item = "fang"  # Example item to visualise
    toa.visualise_purple_chance(purple_item)

    # Example usage of the fit_drop_model function
    # purple_item = "fang"  # Example item to visualise
    # toa.fit_drop_model(purple_item)


if __name__ == "__main__":
    main()
