# AI-Web-Crawler
# Advanced Web Crawler

## Overview
The **Advanced Web Crawler** is a feature-rich Python application designed to crawl web pages and categorize links based on webpage headings. The tool implements multiple search algorithms (BFS, DFS, Best-First Search, Iterative Deepening Search) and features a user-friendly GUI built with `tkinter`.

---

## Features
- **Multiple Search Algorithms**:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Best-First Search (Heuristic-based BFS)
  - Iterative Deepening Search (IDS)
- **Categorization**: Groups URLs based on extracted headings (`h2`, `h3`, `h4`, `li`) from the crawled pages.
- **Progress Bar**: Tracks crawling progress in real-time.
- **Stop and Export Options**:
  - Pause crawling mid-way.
  - Export results to a JSON file.
- **Clickable Results**: Displays categorized URLs in the GUI with clickable links.
- **Error Handling**: Gracefully handles network errors and invalid URLs.

---

## Requirements
Ensure the following dependencies are installed:
- Python 3.7 or higher
- Required Python libraries:
  - `beautifulsoup4`
  - `tkinter` (bundled with Python)
  - `urllib`
  - `heapq` (standard library)

Install BeautifulSoup if not already installed:
```bash
pip install beautifulsoup4
```

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/advanced-web-crawler.git
   cd advanced-web-crawler
   ```

2. Run the program:
   ```bash
   python advanced_web_crawler.py
   ```

3. Interact with the GUI:
   - Enter the **starting URL** (e.g., `https://example.com`).
   - Set the **maximum number of pages** to crawl.
   - Choose an **algorithm** from the dropdown menu.
   - Click **Start Crawl** to begin.
   - Stop the crawl using the **Stop Crawl** button.
   - Export results to `categorized_urls.json` by clicking **Export Results**.

---

## File Structure
```
advanced-web-crawler/
│
├── advanced_web_crawler.py  # Main Python script
├── README.md                # Documentation
└── requirements.txt         # (Optional) Dependencies list
```

---

## Limitations
- The tool does not support crawling JavaScript-heavy websites.
- Results are limited to headings (`h2`, `h3`, `h4`, `li`) present on the crawled pages.
- Crawling is limited to HTTP/HTTPS protocols.

---

## License
This project is licensed under the MIT License.

---

## Contact
For questions or support, reach out to:
- **Your Name**: ruthikmandala2005@gmail.com
- GitHub: https://github.com/RuthiKode

---
