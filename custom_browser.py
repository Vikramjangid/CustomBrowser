import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtNetwork import QNetworkProxy, QNetworkProxyFactory
import os
import requests


class CustomBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Browser")
        self.setGeometry(100, 100, 1024, 768)

        # Layouts
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Address Bar
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Enter URL...")
        self.address_bar.returnPressed.connect(self.load_url)

        # Buttons
        self.button_layout = QHBoxLayout()
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)
        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(self.go_forward)
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_page)
        self.update_proxy_button = QPushButton("Update Proxy")
        self.update_proxy_button.clicked.connect(self.update_proxies)

        self.button_layout.addWidget(self.back_button)
        self.button_layout.addWidget(self.forward_button)
        self.button_layout.addWidget(self.refresh_button)
        self.button_layout.addWidget(self.update_proxy_button)

        # Web View
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Add widgets to layout
        self.layout.addWidget(self.address_bar)
        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.browser)

        # Proxy Management
        self.proxy_list = []
        self.current_proxy = None
        self.load_proxies()

    def load_proxies(self):
        """Load proxies from a text file."""
        if not os.path.exists("proxies.txt"):
            with open("proxies.txt", "w") as f:
                f.write("")  # Create empty file if not exists
        with open("proxies.txt", "r") as f:
            self.proxy_list = [line.strip() for line in f.readlines() if line.strip()]

    def check_site_access(self, url):
        """Check if the site is accessible without a proxy."""
        try:
            response = requests.get(url, timeout=10)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"requests.RequestException: {url} | {e}")
            return False

    def set_proxy(self):
        """Set a proxy dynamically."""
        if self.proxy_list:
            self.current_proxy = self.proxy_list.pop(0)
            self.proxy_list.append(self.current_proxy)  # Rotate proxy
            proxy_ip, proxy_port = self.current_proxy.split(":")
            proxy = QNetworkProxy()
            proxy.setType(QNetworkProxy.HttpProxy)
            proxy.setHostName(proxy_ip)
            proxy.setPort(int(proxy_port))
            QNetworkProxy.setApplicationProxy(proxy)
        else:
            QNetworkProxy.setApplicationProxy(QNetworkProxy())  # No proxy

    def load_url(self):
        """Load the URL entered in the address bar."""
        url = self.address_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        # Check if site is accessible without proxy
        if self.check_site_access(url):
            QNetworkProxy.setApplicationProxy(QNetworkProxy())  # Reset to no proxy
        else:
            self.set_proxy()  # Use proxy if site is not accessible

        self.browser.setUrl(QUrl(url))

    def go_back(self):
        """Go to the previous page."""
        self.browser.back()

    def go_forward(self):
        """Go to the next page."""
        self.browser.forward()

    def refresh_page(self):
        """Refresh the current page."""
        self.browser.reload()

    def update_proxies(self):
        """Reload the proxy list."""
        self.load_proxies()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = CustomBrowser()
    browser.show()
    sys.exit(app.exec_())
