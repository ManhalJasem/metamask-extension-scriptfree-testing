from model import ModelType

# Basic
BINARY_LOCATION = "/usr/bin/google-chrome"
CHROMEDRIVER_LOCATION = "/usr/local/bin/chromedriver"
MODEL_LOCATION = "data"
TESTCASE_DIR = "test_cases_metamask_experiment"
TESTCASE_FILE = "metamaskui"
APP_SPECIFIC_CHROME_OPTIONS = ["--user-data-dir=chrome-profiles/mm-chrome-profile", 
                               "--load-extension=../../../dist/chrome"]
ALL_TESTCASE = True # Run all test case
TESTCASES = ["show_qr_code"] # test case set to run if ALL_TESTCASE==false
OUTPUT_DIRECTORY = "test_script/metamask_exp"
WRITE_LOCATOR = False

# Common
MODEL = ModelType.FASTTEXT_300_SMALL
HEADLESS = False  # Chrome headless
SLEEP_TIME = 1  # wait between operations
SCREENSHOT_FOLDER = "test_script/metamask_exp/screenshots"
TRANSITION_SLEEP_TIME = 1  # wait after page transition
SHOW_OPERATION = True
IDF_WEIGHT = 1.5  # The closer to 1, the bigger
TAG_CLICK = {"button", "img", "a"}  # click target tags
TAG_ASSERT_ELEMENT = {"span","textarea", "input", "button", "img", "a"} 

# Transition-level search
RESTART_DRIVER = True
SEARCH_WIDTH = 5
BEAM_WIDTH = 5
PAGE_MATCHING_SEARCH = 10  # explore top n
TEXT_WEIGHT = 3  # against attr_words

EXCEPT_ATTRS = {
    "autocorrect",
    "spellcheck",
    "tabindex",
    "style",
    "pattern",
    "aria-hidden",
    "maxlength",
    "minlength",
    "max",
    "min",
    "height",
    "width",
    "size",
    "step",
}

STOP_WORDS = {
    "for",
    "the",
    "do",
    "did",
    "does",
    "this",
    "to",
    "of",
    "with",
    "and",
    "or",
    "have",
    "has",
    "as",
    "is",
}

HEURISTIC_STOP_WORDS = {
    "button",
    "btn",
    "link",
    "form",
    "svg",
    "www",
    "https",
    "http",
    "com",
    "js",
    "css",
    "true",
    "false",
    "checked",
}
