#!/usr/bin/env python3
# Скрипт для вывода приветствия в GitHub Actions

def main():
    print("Hello GitHub Actions")  # Основное сообщение
    print(f"Python version: {__import__('sys').version}")  # Доп. информация о версии Python

if __name__ == "__main__":
    main()
