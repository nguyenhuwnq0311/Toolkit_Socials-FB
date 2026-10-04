from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"

BROWSER_PROFILE_DIR = DATA_DIR / "browser_profile"
DATABASE_FILE = DATA_DIR / "facebook.db"

DATA_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)
BROWSER_PROFILE_DIR.mkdir(parents=True, exist_ok=True)

FACEBOOK_URL = "https://www.facebook.com/"


# =========================
# MODE 1 SETTINGS
# =========================

# Test trước với 5 người.
# Sau này có thể chỉnh 10, 20...
MAX_ADD_PER_RUN = 5000

# Thời gian chờ sau mỗi action.
# Dùng để trang Facebook có thời gian cập nhật giao diện.
ACTION_DELAY_SECONDS = 3

# Số lần scroll tối đa để tìm thêm suggestion
MAX_SCROLL_ROUNDS = 10