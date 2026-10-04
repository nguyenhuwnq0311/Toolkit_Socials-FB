from playwright.sync_api import sync_playwright
from config import BROWSER_PROFILE_DIR, FACEBOOK_URL


class FacebookBrowser:

    def __init__(self):
        self.playwright = None
        self.context = None

    def start(self):
        print("[+] Starting browser...")

        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=str(BROWSER_PROFILE_DIR),
            headless=False,
            viewport={
                "width": 1400,
                "height": 900
            }
        )

        if self.context.pages:
            page = self.context.pages[0]
        else:
            page = self.context.new_page()

        return page

    def ensure_login(self, page):
        print("[+] Opening Facebook...")

        page.goto(
            FACEBOOK_URL,
            wait_until="domcontentloaded"
        )

        print()
        print("====================================")
        print(" FACEBOOK LOGIN CHECK")
        print("====================================")

        # Kiểm tra đơn giản xem trang login có xuất hiện không
        if "login" in page.url.lower():

            print()
            print("Facebook chưa đăng nhập.")
            print("Hãy login thủ công trong cửa sổ browser.")
            print("Nếu có OTP / 2FA thì nhập bình thường.")
            print()

            input(
                "Sau khi vào được Facebook, nhấn ENTER tại Terminal..."
            )

            page.goto(
                FACEBOOK_URL,
                wait_until="domcontentloaded"
            )

        print()
        print("[OK] Facebook browser ready.")
        print()

    def close(self):
        print("[+] Closing browser...")

        if self.context:
            self.context.close()

        if self.playwright:
            self.playwright.stop()