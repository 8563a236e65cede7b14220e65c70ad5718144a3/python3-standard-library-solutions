"""
Listing 2.80

Recursive data structures are represented with a reference to the
original source of the data given in the format
    <Recrusion on typename with id=number>
"""
import pprint


def main():
    local_data = ["a", "b", 1, 2]
    local_data.append(local_data)

    print(f"id(local_data) => {id(local_data)}")
    pprint.pprint(local_data)


if __name__ == "__main__":
    main()
