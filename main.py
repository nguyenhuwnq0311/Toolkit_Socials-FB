from core.browser import FacebookBrowser
from modes.mode1_add_suggestions import run as mode1


def show_menu():
    print()
    print("==========================================")
    print("        FACEBOOK FRIEND MANAGER")
    print("==========================================")
    print()
    print("[1] Add Suggested Friends")
    print("[2] Bulk Unfriend")
    print("[3] Cancel Requests Older Than 24h")
    print("[4] Find Fresh Users")
    print("[0] Exit")
    print()
    print("==========================================")


def main():
    print()
    print("Starting Facebook Friend Manager...")
    print()

    browser = FacebookBrowser()

    try:
        page = browser.start()

        browser.ensure_login(page)

        while True:
            show_menu()

            choice = input("Select mode: ").strip()

            if choice == "1":
                mode1(page)

            elif choice == "2":
                print()
                print("Mode 2 selected - not implemented yet.")

            elif choice == "3":
                print()
                print("Mode 3 selected - not implemented yet.")

            elif choice == "4":
                print()
                print("Mode 4 selected - not implemented yet.")

            elif choice == "0":
                print()
                print("Exiting...")
                break

            else:
                print()
                print("Invalid option.")

    except KeyboardInterrupt:
        print()
        print("Stopped by user.")

    except Exception as error:
        print()
        print("ERROR:")
        print(error)

    finally:
        browser.close()


if __name__ == "__main__":
    main()