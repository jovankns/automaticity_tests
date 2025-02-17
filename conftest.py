import os
import json
import logging
import pytest
import datetime
import threading
import time
import numpy as np
import cv2
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


#  Podešavanje logovanja
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "test_log.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)


#  Pytest opcije za browser i runner (lokalno ili remote)
def pytest_addoption(parser):
    parser.addoption("--runner", action="store", default="local", help="Run tests locally or on Selenium Grid")
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, edge")


@pytest.fixture
def runner(request):
    return request.config.getoption("--runner")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


#  Fixture za WebDriver
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"\n--- Pokretanje {browser} WebDriver-a ---")  # Debug ispis
    logging.info(f"Starting {browser} browser for local execution")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1360,768")
        if os.environ.get("HEADLESS_FLAG", "False") == "True":
            options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    elif browser == "edge":
        options = EdgeOptions()
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    logging.info(f"Initialized {browser} WebDriver")
    yield driver
    driver.quit()
    logging.info("Test completed")


#  Snimanje screenshot-a ako test padne
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            feature_request = item.funcargs["request"]
            driver = feature_request.getfixturevalue("driver")
        except KeyError:
            return

        screenshot_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshot_dir, f"screenshot-{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        logging.error(f"Test failed: Screenshot saved at {screenshot_path}")


#  Klasa za snimanje ekrana (video)
class ScreenRecorder:
    def __init__(self, test_name):
        self.test_name = test_name
        self.recording = False
        self.video_writer = None

    def start_recording(self):
        self.recording = True
        thread = threading.Thread(target=self.record_screen)
        thread.start()

    def record_screen(self):
        screen_size = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        video_filename = f"videos/{self.test_name}_{timestamp}.avi"

        os.makedirs("videos", exist_ok=True)
        self.video_writer = cv2.VideoWriter(video_filename, fourcc, 10.0, screen_size)

        while self.recording:
            frame = pyautogui.screenshot()
            frame = np.array(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.video_writer.write(frame)
            time.sleep(0.1)  # Snima 10 fps

        self.video_writer.release()

    def stop_recording(self):
        self.recording = False


#  Fixture za snimanje videa testova
@pytest.fixture(scope="function", autouse=True)
def record_video(request):
    test_name = request.node.name
    recorder = ScreenRecorder(test_name)
    recorder.start_recording()
    yield
    recorder.stop_recording()


#  Učitavanje konfiguracije iz `config.json`
@pytest.fixture
def config():
    config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")
    with open(config_path) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture
def base_url(config):
    return config["base_url"]

@pytest.fixture
def valid_user(config):
    return config["valid_user"]

@pytest.fixture
def invalid_email(config):
    return config["invalid_email"]

@pytest.fixture
def password(config):
    return config["password"]