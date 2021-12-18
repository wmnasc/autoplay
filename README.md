**Requirements:**

> * [Java 8 (x64)](https://www.java.com/pt-BR/download/ie_manual.jsp?locale=pt_BR)
> * [Sikuli 2.0.5](https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5-win.jar)
> * [Python](https://www.python.org/downloads/) *Mark the box as Python 3.10 to PATH*
> * After install Python, run **install.bat** to solve depedencies

**Editing**
> * 1) Change the file **pass.txt** including MetaMask password base64 encoded. ex: *terminal# echo 'password' |base64*
> * 2) Change **start-sikuli.bat** setting the path to sikuli.jar
> * 3) Create a shortcut from shortcut/start.bat (this .bat must calls YOUR_PATH/captcha_clean/start.py)
> * 4) Change the shortcut icon to **12252.ico** (added in /shortcut)
> * 5) Fix shortcut at start bar

**Using**
> * Open **start-sikuli.bat** (after editing to right sikuli.jar path)
> * From Sikuli click on file > Open, find the bombcrypto.sikuli/bombcrypto.py
> * Run
> * Make sure Google Chrome is open with Bomber Crypto "PlayGame" page loaded.
