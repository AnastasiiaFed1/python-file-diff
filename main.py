from logic import FileHandler

def main():
    handler = FileHandler()
    
    # Використовуємо імена файлів, які хочемо порівняти
    lines1 = handler.get_lines("file1.txt")
    lines2 = handler.get_lines("file2.txt")
    
    same, diff = handler.compare_sets(lines1, lines2)
    
    # Записуємо результати
    with open("same.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(sorted(same)))
    
    with open("diff.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(sorted(diff)))

if __name__ == "__main__":
    main()