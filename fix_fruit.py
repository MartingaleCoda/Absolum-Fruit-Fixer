import argparse
from pathlib import Path


def main():
    old, new, save_filename, temp_save_filename = _get_args()
    update_fruit(
        old_fruit_count=old,
        new_fruit_count=new,
        filename=save_filename,
    )
    update_fruit(
        old_fruit_count=old,
        new_fruit_count=new,
        filename=temp_save_filename,
    )
    input("\nDone. Press Enter to exit...")


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--old",
        type=int,
        nargs="?",
    )
    parser.add_argument(
        "--new",
        type=int,
        nargs="?",
    )
    parser.add_argument(
        "--save_filename",
        default="Save.bin",
        type=str,
        nargs="?",
    )
    parser.add_argument(
        "--temp_save_filename",
        default="Save.temp.bin",
        type=str,
        nargs="?",
    )

    old = parser.parse_args().old
    if old is None:
        old_input = input("Enter how many fruit you have (e.g. 1): ").strip()
        old = int(old_input)

    new = parser.parse_args().new
    if new is None:
        new_input = input("Enter how many fruit you would like (e.g. 10): ").strip()
        new = int(new_input)

    save_filename = parser.parse_args().save_filename
    temp_save_filename = parser.parse_args().temp_save_filename

    return old, new, save_filename, temp_save_filename


def update_fruit(old_fruit_count, new_fruit_count, filename=""):
    print(f"\nFile: {filename}")

    old_pattern = bytes(
        [
            80,
            101,
            114,
            109,
            97,
            46,
            70,
            105,
            120,
            82,
            97,
            119,
            46,
            77,
            101,
            116,
            97,
            70,
            114,
            117,
            105,
            116,
            18,
            2,
            8,
            old_fruit_count,
            154,
            3,
            37,
        ]
    )
    new_pattern = bytes(
        [
            80,
            101,
            114,
            109,
            97,
            46,
            70,
            105,
            120,
            82,
            97,
            119,
            46,
            77,
            101,
            116,
            97,
            70,
            114,
            117,
            105,
            116,
            18,
            2,
            8,
            new_fruit_count,
            154,
            3,
            37,
        ]
    )

    input_filename = Path("your_save_files") / filename
    if not input_filename.exists():
        print(
            f"\nNo file {input_filename} found \
                (did you forget to copy your save files to the folder?)"
        )
        return

    with open(input_filename, "rb") as f:
        data = bytearray(f.read())

    match_count = data.count(old_pattern)
    if match_count == 0:
        print(f"\nNo save slot(s) found with {old_fruit_count} fruit")
        return

    patched_data = data.replace(old_pattern, new_pattern)

    output_filename = Path("patched_save_files") / filename
    with open(output_filename, "wb") as f:
        f.write(patched_data)

    print(f"  Replaced Old Fruit Count {old_fruit_count}")
    print(f"  With New Fruit Count {new_fruit_count}")
    print(f"  New Save File: {output_filename}")

    print("\n(For Devs)\n")
    print(f"  Old Byte Pattern: {old_pattern} ({list(old_pattern)})")
    print(f"  New Byte Pattern: {new_pattern} ({list(new_pattern)})")
    print()


if __name__ == "__main__":
    main()
