#!/usr/bin/env python3

def human_readable_size(size_bytes):
    # Convert bytes to a human-readable format
    for unit in ['B','KB','MB','GB','TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"

def generate_report(path, file_count, dir_count, total_size, top_files, type_breakdown, sort_method, sorted_extensions, output_path):

    report_lines = []

    report_lines.append(f"📁 Directory Report for: {path}")
    report_lines.append(f"📦 Total size: {human_readable_size(total_size)}")
    report_lines.append(f"📄 Files: {file_count}, 📂 Folders: {dir_count}\n")
    
    if top_files:
        report_lines.append(f"🔝 Top {len(top_files)} Largest Files (Sorted by size):")
        for i, (fp, size) in enumerate(top_files, 1):
            report_lines.append(f"{i}. {fp} - {human_readable_size(size)}")
        report_lines.append("")

    if type_breakdown:
        report_lines.append("📊 File Type Breakdown:")
        for ext, count in sorted(type_breakdown.items(), key=lambda x: x[1], reverse=True):
            report_lines.append(f"{ext or '[no extension]'}: {count}")
        report_lines.append("")
    
    if sort_method and sorted_extensions:
        report_lines.append(f"🗂 Sorted File Types by `{sort_method}`:")
        for ext in sorted_extensions:
            report_lines.append(f"• {ext}")
        report_lines.append("")
    
    final_report = '\n'.join(report_lines)
    
    print("\n" + final_report)
    
    if output_path:
        try:
            with open(output_path, 'w') as f:
                f.write(final_report)
            print(f"✅ Report saved to: {output_path}")
        except Exception as e:
            print(f"❌ Error writing to file: {e}")
    else:
        pass



# ---------------- Main Block ---------------- #
if __name__ == '__main__':
    # Sample data for testing
    sample_path = "/home/student/testdir"
    sample_file_count = 8
    sample_dir_count = 2
    sample_total_size = 3145728  # 3 MB
    sample_top_files = [
        ("/home/student/testdir/file1.txt", 2048000),
        ("/home/student/testdir/file2.jpg", 512000),
        ("/home/student/testdir/big.iso", 1024000)
    ]
    sample_type_breakdown = {
        ".txt": 2,
        ".jpg": 3,
        ".iso": 1
    }

    