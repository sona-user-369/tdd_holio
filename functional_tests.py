from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.service import Service
from pathlib import Path
import sys

app_dir = Path("/") / "snap" / "bin" / "firefox"
geckodriver = Path("/") / "snap" / "bin" / "geckodriver"

print(app_dir)

options = Options()
# options.add_argument('-headless')
options.binary = FirefoxBinary(str(app_dir))


service = Service(
        executable_path=str(geckodriver),
        service_args=["--log", "trace"],
        log_output=str(Path(sys.prefix) / "geckodriver.log")
    )

browser = webdriver.Firefox(options=options, service=service)

browser.get("http://localhost:8000")

assert 'Django' in browser.title
