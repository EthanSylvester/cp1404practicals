import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    chars = []
    adjust = 0
    for n, char in enumerate(filename):
        chars.append(char)
        if n == 0:
            chars[n] = char.upper()
        if char == " ":
            chars[n + adjust] = "_"
        if filename[n - 1].islower() and char.isupper() and n != 0:
            chars[n + adjust] = "_"
            chars.append(char)
            adjust += 1
        if filename[n - 1] == "_" and char.islower():
            chars[n + adjust] = char.upper()
        if filename[n - 1] == "(" and char.islower():
            chars[n + adjust] = char.upper()
        if filename[n - 3] == "." and (char == "T" or filename[n - 1] == "X" or filename[n - 2] is "T"):
            chars[n + adjust - 2] = "t"
            chars[n + adjust - 1] = "x"
            chars[n + adjust] = "t"
    new_name = "".join(chars)
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            if os.path.isdir(filename):
                continue
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


# main()
demo_walk()
