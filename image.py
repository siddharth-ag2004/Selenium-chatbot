from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def SendText(driver,text_input):
    try:
        textarea = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "prompt"))
        )

        textarea.clear()

        textarea.send_keys(text_input)

        # Wait for the upload button to be present
        upload_button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "generateButton")))

        # Click the upload button
        upload_button.click()

    except Exception as e:
        print(f"An error occurred: {e}")


driver = webdriver.Chrome()
driver.get("https://www.craiyon.com/")
driver.minimize_window()

text_input = "Generate a comic-style image with an old retro vibe featuring a detective who looks exactly like Sherlock Holmes. The detective should have a height of approximately 6 feet, a lean and athletic build with well-defined features. His face should sport a sharp jawline, a slightly pointed nose, and intense, piercing blue eyes. His hair should be dark brown, neatly combed back, and he should have a well-groomed mustache and beard.The detective should be dressed in a classic detective attire, wearing a tailored brown tweed suit with a matching vest. The suit should have a slight wear-and-tear appearance, indicative of a seasoned investigator. He should wear a crisp white shirt with a high collar and a loosely tied, patterned ascot. The detective's footwear should be polished brown leather shoes, and he should carry a vintage magnifying glass in his left hand.The facial expression of the detective should convey a sense of astuteness and curiosity, as befitting a seasoned investigator. Ensure that the generated image consistently adheres to these detailed characteristics, avoiding variations in the detective's appearance."

SendText(driver,text_input)

input("Press Enter to close the script.")
