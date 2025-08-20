def show_menu():
    print("\nTo-do List dasturi")
    print("1. Vazifa qo'shish")
    print("2. Vazifalarni ko'rsatish")
    print("3. Chiqish")

def add_task(tasks):
    task = input("Yangi vazifani kiriting: ")
    tasks.append(task)
    print("Vazifa qo'shildi!")

def show_tasks(tasks):
    if not tasks:
        print("Vazifalar yo'q.")
    else:
        print("\nVazifalar ro'yxati:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Tanlang (1-3): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            print("Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

if __name__ == "__main__":
    main()
