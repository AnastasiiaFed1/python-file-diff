class FileHandler:
    @staticmethod
    def get_lines(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return {line.strip() for line in f if line.strip()}
        except FileNotFoundError:
            return set()
    
    @staticmethod
    def compare_sets(set1, set2):
        same = set1.intersection(set2)
        diff = set1.symmetric_difference(set2)
        return same, diff