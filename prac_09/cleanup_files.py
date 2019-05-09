import os


def main():
    """Cleanup inconsistent song lyrics file names."""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename).replace(".TXT", ".txt").replace(" ", "_")
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    new_name = filename[0]

    for i, letter in enumerate(filename[1:], 1):
        if letter.isupper():
            try:
                if filename[i-1].islower() or filename[i+1].islower() and filename[i - 1] != '(':
                    new_name += '_'
            except IndexError:
                pass
        new_name += letter
    return new_name

main()
