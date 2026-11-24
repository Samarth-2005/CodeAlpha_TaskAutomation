import os
import re
import shutil
import urllib.request


def move_jpg_files():
    """Option 1: Move all .jpg files from a source folder to a destination folder."""
    print("\n--- Option 1: Move All .jpg Files ---")
    source_folder = input(
        "Enter source folder path (or press Enter to create & use a demo 'sample_images' folder): "
    ).strip()

    if not source_folder:
        source_folder = "sample_images"
        os.makedirs(source_folder, exist_ok=True)
        existing_jpgs = [
            f for f in os.listdir(source_folder) if f.lower().endswith(".jpg")
        ]
        if not existing_jpgs:
            for demo_name in ["photo1.jpg", "banner2.jpg", "profile3.jpg"]:
                demo_path = os.path.join(source_folder, demo_name)
                with open(demo_path, "w", encoding="utf-8") as f:
                    f.write("Sample JPG placeholder content\n")
            print(f"Created demo folder '{source_folder}' with 3 sample .jpg files.")

    if not os.path.isdir(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return

    dest_folder = input(
        "Enter destination folder path (or press Enter for 'moved_jpg_files'): "
    ).strip()
    if not dest_folder:
        dest_folder = "moved_jpg_files"

    os.makedirs(dest_folder, exist_ok=True)

    moved_count = 0
    for filename in sorted(os.listdir(source_folder)):
        if filename.lower().endswith(".jpg"):
            src_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(src_path, dest_path)
            moved_count += 1
            print(f"  Moved: {filename} -> {dest_folder}/")

    if moved_count == 0:
        print(f"No .jpg files found in '{source_folder}'.")
    else:
        print(f"Successfully moved {moved_count} .jpg file(s) to '{dest_folder}'.")


def extract_email_addresses():
    """Option 2: Extract all email addresses from a .txt file and save them to another file."""
    print("\n--- Option 2: Extract Email Addresses from a .txt File ---")
    input_file = input(
        "Enter input .txt file path (or press Enter to use 'sample_contacts.txt'): "
    ).strip()

    if not input_file:
        input_file = "sample_contacts.txt"
        if not os.path.isfile(input_file):
            sample_text = (
                "CodeAlpha Internship Directory\n"
                "Please reach out to services@codealpha.tech or services.codealpha@gmail.com for support.\n"
                "Project Mentor: mentor.python@codealpha.tech\n"
                "HR Team: hr_department@company.org | Student Coordinator: alex.dev99@university.edu\n"
            )
            with open(input_file, "w", encoding="utf-8") as f:
                f.write(sample_text)
            print(f"Created demo file '{input_file}' with sample contact text.")

    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' was not found.")
        return

    output_file = input(
        "Enter output file path (or press Enter for 'extracted_emails.txt'): "
    ).strip()
    if not output_file:
        output_file = "extracted_emails.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Regular expression pattern to match standard email addresses
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    found_emails = sorted(set(re.findall(email_pattern, content)))

    if not found_emails:
        print(f"No email addresses found in '{input_file}'.")
        return

    with open(output_file, "w", encoding="utf-8") as f:
        for email in found_emails:
            f.write(email + "\n")

    print(f"Found {len(found_emails)} unique email address(es):")
    for email in found_emails:
        print(f"  - {email}")
    print(f"Saved extracted emails to '{output_file}'.")


def scrape_webpage_title():
    """Option 3: Scrape the <title> of a webpage and save it to a .txt file."""
    print("\n--- Option 3: Scrape Webpage Title ---")
    url = input(
        "Enter webpage URL (or press Enter for 'https://www.python.org'): "
    ).strip()
    if not url:
        url = "https://www.python.org"
    elif not url.startswith(("http://", "https://")):
        url = "https://" + url

    output_file = input(
        "Enter output file path (or press Enter for 'webpage_title.txt'): "
    ).strip()
    if not output_file:
        output_file = "webpage_title.txt"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            html_content = response.read().decode("utf-8", errors="ignore")

        match = re.search(
            r"<title[^>]*>(.*?)</title>", html_content, re.IGNORECASE | re.DOTALL
        )
        if match:
            title = " ".join(match.group(1).strip().split())
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"URL: {url}\n")
                f.write(f"Title: {title}\n")
            print(f"Scraped Webpage Title: {title}")
            print(f"Saved result to '{output_file}'.")
        else:
            print("Could not find a <title> tag on that webpage.")
    except Exception as exc:
        print(f"Could not fetch webpage ({exc}).")


def main():
    while True:
        print("\n==================================================")
        print("      Task Automation with Python Scripts         ")
        print("==================================================")
        print("1. Move all .jpg files from a folder to a new folder")
        print("2. Extract all email addresses from a .txt file")
        print("3. Scrape the title of a webpage and save it")
        print("4. Exit")
        print("--------------------------------------------------")

        choice = input("Choose an automation task (1-4): ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_email_addresses()
        elif choice == "3":
            scrape_webpage_title()
        elif choice == "4":
            print("Exiting Task Automation suite. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()