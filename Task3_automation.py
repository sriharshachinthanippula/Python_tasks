import os
import shutil
import re

def move_jpg_files():
    print("\n📁 OPTION A: Move .jpg Files")
    print("-" * 35)
    source = input("Enter source folder path: ").strip()
    if not os.path.isdir(source):
        print(f"⚠ Folder not found: {source}")
        return
    dest = os.path.join(source, "jpg_files")
    os.makedirs(dest, exist_ok=True)
    moved = 0
    for filename in os.listdir(source):
        if filename.lower().endswith(".jpg"):
            src_path = os.path.join(source, filename)
            dst_path = os.path.join(dest, filename)
            shutil.move(src_path, dst_path)
            print(f"  ✅ Moved: {filename}")
            moved += 1
    if moved == 0:
        print("No .jpg files found in the source folder.")
    else:
        print(f"\n✅ Done! Moved {moved} file(s) to: {dest}")

def extract_emails():
    print("\n📧 OPTION B: Extract Emails from a .txt File")
    print("-" * 45)
    input_file = input("Enter path to input .txt file: ").strip()
    if not os.path.isfile(input_file):
        print(f"⚠ File not found: {input_file}")
        return
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
    email_pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, content)
    unique_emails = sorted(set(emails))
    if not unique_emails:
        print("No email addresses found in the file.")
        return
    print(f"\nFound {len(unique_emails)} unique email(s):")
    for email in unique_emails:
        print(f"  • {email}")
    output_file = input("\nEnter output file path (e.g. emails.txt): ").strip()
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Extracted Emails ({len(unique_emails)} found)\n")
        f.write("=" * 40 + "\n")
        for email in unique_emails:
            f.write(email + "\n")
    print(f"✅ Emails saved to: {output_file}")

def scrape_webpage_title():
    print("\n🌐 OPTION C: Scrape Webpage Title")
    print("-" * 35)
    try:
        import requests
    except ImportError:
        print("⚠ 'requests' module not found.")
        print("Install it by running:  pip install requests")
        return
    url = input("Enter a webpage URL (e.g. https://example.com): ").strip()
    if not url.startswith("http"):
        url = "https://" + url
    print(f"Fetching: {url} ...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"⚠ Failed to fetch the page: {e}")
        return
    match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
    title = match.group(1).strip() if match else "No title found"
    print(f"\n📄 Page Title: {title}")
    output_file = input("Enter output file path (e.g. title.txt): ").strip()
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"URL   : {url}\n")
        f.write(f"Title : {title}\n")
    print(f"✅ Title saved to: {output_file}")

def main():
    print("\n=============================")
    print("    TASK AUTOMATION TOOL")
    print("=============================")
    print("Choose an automation task:\n")
    print("  A) Move all .jpg files to a new folder")
    print("  B) Extract email addresses from a .txt file")
    print("  C) Scrape the title of a webpage and save it")
    print("  Q) Quit")
    choice = input("\nYour choice (A/B/C/Q): ").strip().upper()
    if choice == "A":
        move_jpg_files()
    elif choice == "B":
        extract_emails()
    elif choice == "C":
        scrape_webpage_title()
    elif choice == "Q":
        print("Goodbye! 👋")
    else:
        print("⚠ Invalid choice. Please enter A, B, C, or Q.")
        main()

if __name__ == "__main__":
    main()
