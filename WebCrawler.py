import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser


# ----------------------------- Helper Functions ----------------------------- #
def extract_categories(soup):
    # Extract category headings from the webpage.
    categories = {}
    for tag in soup.find_all(['h2', 'h3', 'li']):
        text = tag.get_text().strip().lower()
        if len(text) >= 3:
            categories[text] = []
    return categories


def simple_bfs_crawl(start_url, max_pages):
    # Simple Breadth-First Search to crawl web pages.
    queue = [start_url]
    visited = set()
    categorized_urls = {}

    while queue and len(visited) < max_pages:
        current_url = queue.pop(0)
        if current_url in visited:
            continue

        try:
            response = urllib.request.urlopen(current_url)
            soup = BeautifulSoup(response, 'html.parser')
            visited.add(current_url)

            categories = extract_categories(soup)
            for tag in soup.find_all("a", href=True):
                link = urljoin(current_url, tag['href']).rstrip('/')
                if link not in visited and link not in queue:
                    queue.append(link)

                for category in categories:
                    if category in tag.get_text().strip().lower():
                        categories[category].append(link)

            for category, urls in categories.items():
                categorized_urls.setdefault(category, []).extend(
                    [url for url in urls if url not in categorized_urls.get(category, [])]
                )

        except Exception:
            pass

    return categorized_urls


# ----------------------------- GUI Logic ----------------------------- #
def update_progress(completed, total, progress_bar):
    # Updates the progress bar.
    progress_bar['value'] = (completed / total) * 100


def display_results(categorized_urls, results_frame, canvas):
    # Displays the categorized URLs.
    for widget in results_frame.winfo_children():
        widget.destroy()

    for category, urls in categorized_urls.items():
        if urls:
            category_label = tk.Label(results_frame, text=f"{category.capitalize()}:", font=("Arial", 12, "bold"), anchor="w")
            category_label.pack(fill=tk.X, padx=5, pady=2)

            for url in urls:
                link = tk.Label(results_frame, text=url, fg="blue", cursor="hand2", anchor="w")
                link.pack(fill=tk.X, padx=10)
                link.bind("<Button-1>", lambda e, u=url: webbrowser.open_new(u))

    canvas.configure(scrollregion=canvas.bbox("all"))


def start_crawl():
    # Starts the crawl.
    progress_bar['value'] = 0
    try:
        url = url_entry.get()
        max_pages = int(pages_entry.get())
        categorized_urls = simple_bfs_crawl(url, max_pages)
        display_results(categorized_urls, results_frame, canvas)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ----------------------------- GUI Components ----------------------------- #
def display_gui():
    global root, progress_bar, url_entry, pages_entry, results_frame, canvas

    root = tk.Tk()
    root.title("Simple Web Crawler")

    # Input Fields
    frame_top = tk.Frame(root)
    frame_top.pack(pady=10)

    tk.Label(frame_top, text="Input URL:").grid(row=0, column=0, padx=5)
    url_entry = ttk.Entry(frame_top, width=50)
    url_entry.grid(row=0, column=1, padx=5)

    tk.Label(frame_top, text="Max Pages:").grid(row=1, column=0, padx=5)
    pages_entry = ttk.Entry(frame_top, width=10)
    pages_entry.grid(row=1, column=1, padx=5)

    # Buttons
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=10)

    start_button = tk.Button(frame_buttons, text="Start Crawl", command=start_crawl)
    start_button.pack(side=tk.LEFT, padx=10)

    # Progress Bar
    progress_bar = ttk.Progressbar(root, length=500, mode="determinate")
    progress_bar.pack(pady=10)

    # Results Canvas
    canvas = tk.Canvas(root, height=400)
    canvas.pack(fill=tk.BOTH, expand=True)

    results_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=results_frame, anchor="nw")

    root.mainloop()


# ----------------------------- Main ----------------------------- #
if __name__ == "__main__":
    display_gui()
