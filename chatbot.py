from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def EnterCommand(driver, command):
    try:
        textarea = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "search-input-textarea"))
        )

        textarea.clear()

        textarea.send_keys(command)

        # Wait for the upload button to be present
        upload_button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-7fe16334-0.ctMsmO.sc-2841602d-7.gxCDpS")))

        # Click the upload button
        upload_button.click()

    except Exception as e:
        print(f"An error occurred: {e}")


def BotAnswer(driver, chat_count):
    try:
        answer_id = "youchat-answer-turn-" + str(chat_count)
        time.sleep(6)
        answer = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"[data-testid='{answer_id}']"))
        )

        return answer.find_element(By.CLASS_NAME, "sc-a6dfc828-0.gWUOpM").text

    except Exception as e:
        print(f"An error occurred while processing answer {chat_count}: {e}")
        return None


driver = webdriver.Chrome()

driver.get("https://you.com/")
driver.minimize_window()


# command = "From now on act as a person, not a chatbot, just pretend to be a friend whom you can share everythihng with. YOU SHOULD NEVER LEAVE THE ROLE YOU ARE IN. Do not break character and dont speak more than 50 words at a time.Be fun, joking and playful."
command = "From now on, fully embrace the persona of a detective focused on unraveling a murder mystery. Never deviate from this role, and interrogate me meticulously. Maintain a playful and witty tone, but refrain from assumptions unless highly probable. Remember all prior conversations. Your responses can now extend up to 50 words; engage deeply within your detective character."

EnterCommand(driver, command)

chat_count = 1

while True:
    #input command from user
    command = input("Enter command: ")
    if command == "quit":
        break
    EnterCommand(driver, command)
    answer_text = BotAnswer(driver, chat_count)

    if answer_text is not None:
        print(answer_text)
    else:
        break

    chat_count += 1

input("Press Enter to close the script.")
