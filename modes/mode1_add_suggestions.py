import time

from config import (
    MAX_ADD_PER_RUN,
    ACTION_DELAY_SECONDS,
    MAX_SCROLL_ROUNDS,
)


SUGGESTIONS_URL = "https://www.facebook.com/friends/suggestions"


def run(page):

    print()
    print("==========================================")
    print(" MODE 1 - ADD SUGGESTED FRIENDS")
    print("==========================================")
    print()

    print("[+] Opening Facebook Suggestions...")

    page.goto(
        SUGGESTIONS_URL,
        wait_until="domcontentloaded"
    )

    # Chờ Facebook load giao diện
    page.wait_for_timeout(3000)

    print("[OK] Suggestions page opened.")
    print()
    print(f"[+] Maximum requests this run: {MAX_ADD_PER_RUN}")
    print()

    added_count = 0
    scroll_round = 0

    while (
        added_count < MAX_ADD_PER_RUN
        and scroll_round < MAX_SCROLL_ROUNDS
    ):

        print(
            f"[+] Scanning page "
            f"(round {scroll_round + 1}/{MAX_SCROLL_ROUNDS})..."
        )

        # Facebook tiếng Việt:
        # nút "Thêm bạn bè"
        add_buttons = page.get_by_role(
            "button",
            name="Thêm bạn bè",
            exact=True
        )

        button_count = add_buttons.count()

        print(f"[+] Found {button_count} Add Friend button(s).")

        if button_count == 0:

            print("[+] No button found. Scrolling...")

            page.mouse.wheel(0, 1200)
            page.wait_for_timeout(2000)

            scroll_round += 1
            continue

        #
        # QUAN TRỌNG:
        # Mỗi lần chỉ lấy nút đầu tiên.
        #
        # Sau khi click, DOM Facebook thay đổi,
        # nên chúng ta scan lại từ đầu.
        #
        button = add_buttons.first

        try:

            if not button.is_visible():
                print("[SKIP] Button not visible.")

                page.mouse.wheel(0, 700)
                page.wait_for_timeout(1500)

                scroll_round += 1
                continue

            print(
                f"[{added_count + 1}/{MAX_ADD_PER_RUN}] "
                f"Sending friend request..."
            )

            button.click()

            added_count += 1

            print(
                f"[OK] Friend request sent. "
                f"Total = {added_count}"
            )

            # Chờ UI cập nhật trước khi thao tác tiếp
            time.sleep(ACTION_DELAY_SECONDS)

        except Exception as error:

            print()
            print("[WARNING] Could not click this button.")
            print(error)
            print()

            page.mouse.wheel(0, 800)
            page.wait_for_timeout(1500)

            scroll_round += 1

        #
        # Khi các nút hiện tại gần hết,
        # scroll xuống để Facebook load thêm suggestion
        #
        remaining_buttons = page.get_by_role(
            "button",
            name="Thêm bạn bè",
            exact=True
        ).count()

        if remaining_buttons <= 1:

            print("[+] Loading more suggestions...")

            page.mouse.wheel(0, 1400)
            page.wait_for_timeout(2000)

            scroll_round += 1

    print()
    print("==========================================")
    print(" MODE 1 COMPLETED")
    print("==========================================")
    print()
    print(f"Friend requests sent : {added_count}")
    print(f"Configured maximum   : {MAX_ADD_PER_RUN}")
    print()

    if added_count >= MAX_ADD_PER_RUN:
        print("[OK] Maximum for this run reached.")
    else:
        print("[INFO] No more suitable buttons were found.")

    print()

    input("Press ENTER to return to main menu...")