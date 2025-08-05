import os



def get_total_size(path):

    total_size = 0

    for root, dirs, files in os.walk(path):

        for f in files:

            fp = os.path.join(root, f)

            if os.path.isfile(fp):

                total_size += os.path.getsize(fp)

    return total_size



def get_top_n_files(path, n):

    all_files = []

    for root, dirs, files in os.walk(path):

        for f in files:

            fp = os.path.join(root, f)

            try:

                size = os.path.getsize(fp)

                all_files.append((fp, size))

            except Exception as e:

                continue

    all_files.sort(key=lambda x: x, reverse=True)

    return all_files[:n]



if __name__ == "__main__":

    print("Note: This script currently uses placeholder paths for demonstration.")

    print("      In a real application, you would provide paths via command-line arguments.")

    print("-" * 50)



    test_path = '.'

    num_top_files = 3



    if os.path.isdir(test_path):

        print(f"Calculating total size for: {test_path}")

        total_size = get_total_size(test_path)

        print(f"Total size of files: {total_size} bytes")

        print("-" * 50)



        print(f"Finding top {num_top_files} largest files in: {test_path}")

        top_files = get_top_n_files(test_path, num_top_files)

        if top_files:

            for i, (file_path, size) in enumerate(top_files):

                print(f"{i+1}. {file_path}: {size} bytes")

        else:

            print("No files found or unable to retrieve file sizes.")

    else:

        print(f"Error: Directory '{test_path}' does not exist or is not a directory.")