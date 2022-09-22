from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pyautogui
import time

email = "您的電子郵件"
password = "您的帳號密碼"

chrome_options = webdriver.ChromeOptions()
prefs = {
    #禁止通知跳出
    "profile.default_content_setting_values.notifications": 2,
    #阻止下載對話框跳出
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    #禁用 PDF 網頁查看器
    "plugins.always_open_pdf_externally": True,
}
chrome_options.add_experimental_option("prefs", prefs)
#使用 ChromeDriverManager 自動開啟 chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options)

#最大化視窗
driver.maximize_window()
#進入 Facebook 登入畫面
driver.get("https://www.facebook.com/")
#填入帳號密碼並送出
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "pass").send_keys(password)
driver.find_element(By.NAME, "login").click()
time.sleep(5)

#進入要爬蟲的 Facebook Group 畫面
driver.get("https://www.facebook.com/groups/946185189309101")
time.sleep(5)
#捲動頁面讓網頁更新
for i in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

#分析網頁原始碼
root = BeautifulSoup(driver.page_source, "html.parser")
#找出包含 PDF 連結的區塊程式碼
fileUrls = root.find_all("a", class_ = "qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 o9erhkwx dzqi5evh hupbnkgi hvb2xoa8 om3e55n1 f14ij5to l3ldwz01 icdlwmnq b6ax4al1")
time.sleep(10)
#快捷鍵 Ctrl+t 新增分頁
pyautogui.hotkey("ctrl", "t", interval = 0.1)
#切換到新分頁
driver.switch_to.window(driver.window_handles[1])
for data in fileUrls:
    #擷取 PDF 下載連結
    url = data.get("href")
    #進入 PDF 下載連結
    driver.get(url)
    time.sleep(5)

#關閉瀏覽器
driver.quit()
