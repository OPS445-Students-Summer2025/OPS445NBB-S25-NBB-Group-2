import os
import argparse

parser = argparse.ArgumentParser(
    description = "Directory size report tool"
)

#dir path argument
parser.add_argument(
    "--dir",
    required = True,
    help = "Directory path to scan"
)

#largest files argument
parser.add_argument(
    "--top", "-t",
    type = int,
    help = "Show top N largest files"
)

#filetype sort argument
parser.add_argument(
    "--sort", "-s",
    choices = ["size","name","type"],
    help = "sort by <size>|<name>|<type>"
)

#write output file argument
parser.add_argument(
    "--output", "-o",
    help = "path to output file (optional)"
)

args = parser.parse_args()

#Kris
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
            except:
                continue
    all_files.sort(key=lambda x: x[1], reverse=True)
    return all_files[:n]
  
  
# === Andrew's Section: Output Formatting and Saving ===
def human_readable_size(size_bytes):
    for unit in ['B','KB','MB','GB','TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"

def generate_report(path, file_count, dir_count, total_size, top_files=None, type_breakdown=None, sort_method=None, output_path=None):
    report_lines = []

    report_lines.append(f"📁 Directory Report for: {path}")
    report_lines.append(f"📦 Total size: {human_readable_size(total_size)}")
    report_lines.append(f"📄 Files: {file_count}, 📂 Folders: {dir_count}")

    if top_files:
        report_lines.append(f"🔝 Top {len(top_files)} Largest Files:")
        sorted_files = top_files
        if sort_method == 'name':
            sorted_files = sorted(top_files, key=lambda x: x[0].lower())
        elif sort_method == 'type':
            sorted_files = sorted(top_files, key=lambda x: os.path.splitext(x[0])[1].lower())

        for i, (fp, size) in enumerate(sorted_files, 1):
            report_lines.append(f"{i}. {fp} - {human_readable_size(size)}")
        report_lines.append("")

    if type_breakdown:
        report_lines.append("📊 File Type Breakdown:")
        items = type_breakdown.items()
        if sort_method == 'name':
            items = sorted(items, key=lambda x: x[0])
        elif sort_method == 'type':
            items = sorted(items, key=lambda x: x[1], reverse=True)
        for ext, count in items:
            report_lines.append(f"{ext or '[no extension]'}: {count}")
        report_lines.append("")

    final_report = '\n'.join(report_lines)

    print("\n" + final_report)

    if output_path:
        try:
            with open(output_path, 'w') as f:
                f.write(final_report)
            print(f"\n✅ Report saved to: {output_path}")
        except Exception as e:
            print(f"\n❌ Failed to save report: {e}")

# === Main Execution Logic ===
if not os.path.isdir(args.dir):
    print("❌ Invalid directory. Please provide a valid path.")
    exit(1)

file_count, dir_count = count_files_and_dirs(args.dir)
total_size = get_total_size(args.dir)

top_files = get_top_n_files(args.dir, args.top) if args.top else None
type_breakdown = get_file_type_breakdown(args.dir) if args.sort == 'type' or args.sort == 'name' else None

generate_report(
    path=args.dir,
    file_count=file_count,
    dir_count=dir_count,
    total_size=total_size,
    top_files=top_files,
    type_breakdown=type_breakdown,
    sort_method=args.sort,
    output_path=args.output
)
