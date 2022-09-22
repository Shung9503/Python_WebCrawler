# __Python 爬蟲 Facebook Group Download PDF__
## 使用到的 Module：
+ selenium 爬蟲動態網頁
+ webdriver_manager 自動下載最新版本的 ChromeDriver
+ pyautogui 快捷鍵新增分頁
+ beautifulsoup4 解析網頁內容
+ time 加入暫停時間讓程式運算
## 需額外安裝 Module 的語法：
```py
pip install selenium
pip install webdriver_manager
pip install pyautogui
pip3 install beautifulsoup4
```
## 注意事項：
可能因為會因為網速太慢的關係，FB社團可能還未加載完成就被爬蟲程式往下拉頁面，會導致蒐集到的網頁原始碼不齊全，所以如果加載不出來的話，需要使用者滑鼠自行上下滾動一下，方能正常運作。
