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
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    r = filename[0].replace(" ", "_").replace(".TXT", ".txt")

    for i, letter in enumerate(filename[1:], 1):
        if letter.isupper():
            try:
                if filename[i-1].islower() or filename[i+1].islower():
                    r += '_'
            except IndexError:
                pass
        r += letter.replace(" ", "_").replace(".TXT", ".txt")
    return r
    # Need to fix double underscores
    # return new_name

main()
