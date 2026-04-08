class FileHandler:
    @staticmethod
    def get_lines(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return {line.strip() for line in f if line.strip()}
        except FileNotFoundError:
            return set()