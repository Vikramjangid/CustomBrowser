# CustomBrowser

CustomBrowser is a lightweight and customizable browser built using Python and PyQt5. It allows users to browse the web, navigate with ease, and access restricted websites using dynamic proxy rotation. The browser automatically detects when a site is inaccessible with the current IP and switches to a proxy from a user-defined list.

---

## Features

- **Basic Navigation**: Back, Forward, Refresh, and Address Bar for entering URLs.
- **Proxy Support**: Automatically switches to a proxy if the site is inaccessible without one.
- **Proxy Rotation**: Cycles through proxies from a user-defined `proxies.txt` file.
- **Customizable**: Modify and extend the browser with PyQt5's extensive features.
- **User-Friendly Interface**: Simple layout for easy browsing.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vikramjangid/CustomBrowser.git
   cd CustomBrowser
2. **Install Dependencies**: Ensure you have Python 3.7+ installed, then install the required libraries:
   ```bash
   pip install PyQt5 PyQtWebEngine requests
3. **Run the Browser**:
   ```bash
   python custom_browser.py
   
## Usage
1. Enter a URL: Type the website URL in the address bar and press Enter.
2. Navigation Buttons:
   Back: Go to the previous page.
   Forward: Navigate to the next page.
   Refresh: Reload the current page.
   Update Proxy: Reload the proxy list from proxies.txt and rotate the proxy.
3. Proxy Management: Add your proxies in the proxies.txt file in the format


## File Structure
1. custom_browser.py: Main script for the browser.
2. proxies.txt: Text file containing the list of proxies.

## Dependencies
1. PyQt5
2. PyQtWebEngine
3. requests

## Contributions
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.


Author
Developed by Vikram Jangid. https://github.com/Vikramjangid/

