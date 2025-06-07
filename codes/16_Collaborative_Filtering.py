import math
from typing import List, Tuple

EMPTY = -2.0

class CF:
    def __init__(self, user_to_item: List[List[float]]):
        self.user_to_item = user_to_item
        self.user_size = len(user_to_item) - 1
        self.item_size = len(user_to_item[-1]) - 1 if user_to_item else 0
        self.average = [0.0] * (self.user_size + 1)
        self.item_to_item = []

    def run(self):
        self.build_item_to_item_c()

    def get_average(self):
        for i in range(1, self.user_size + 1):
            cnt = 0
            total = 0.0
            for j in range(1, self.item_size + 1):
                if self.user_to_item[i][j] == EMPTY:
                    continue
                cnt += 1
                total += self.user_to_item[i][j]
            self.average[i] = total / cnt if cnt > 0 else 0.0

    def build_item_to_item_c(self):
        self.item_to_item = [[0.0] * (self.item_size + 1) for _ in range(self.item_size + 1)]
        for i in range(1, self.item_size + 1):
            for j in range(1, self.item_size + 1):
                top = 0.0
                bleft = 0.0
                bright = 0.0
                cnt = 0
                for k in range(1, self.user_size + 1):
                    rating_i = self.user_to_item[k][i]
                    rating_j = self.user_to_item[k][j]
                    if rating_i == EMPTY or rating_j == EMPTY:
                        continue
                    cnt += 1
                    top += rating_i * rating_j
                    bleft += rating_i * rating_i
                    bright += rating_j * rating_j
                if cnt < 1 or bleft == 0 or bright == 0:
                    self.item_to_item[i][j] = 0.0
                else:
                    self.item_to_item[i][j] = top / (math.sqrt(bleft) * math.sqrt(bright))

    def build_item_to_item_p(self):
        self.get_average()
        self.item_to_item = [[0.0] * (self.item_size + 1) for _ in range(self.item_size + 1)]
        for i in range(1, self.item_size + 1):
            for j in range(1, self.item_size + 1):
                top = 0.0
                bleft = 0.0
                bright = 0.0
                cnt = 0
                for k in range(1, self.user_size + 1):
                    rating_i = self.user_to_item[k][i]
                    rating_j = self.user_to_item[k][j]
                    if rating_i == EMPTY or rating_j == EMPTY:
                        continue
                    cnt += 1
                    diff_i = rating_i - self.average[k]
                    diff_j = rating_j - self.average[k]
                    top += diff_i * diff_j
                    bleft += diff_i * diff_i
                    bright += diff_j * diff_j
                if cnt < 1 or bleft == 0 or bright == 0:
                    self.item_to_item[i][j] = 0.0
                else:
                    self.item_to_item[i][j] = top / (math.sqrt(bleft) * math.sqrt(bright))

    def predict(self, user: int, item: int) -> float:
        if item > self.item_size:
            return 3.0  # Default rating if item not trained
        
        top = 0.0
        bottom = 0.0
        for i in range(1, self.item_size + 1):
            rating = self.user_to_item[user][i]
            if rating == EMPTY:
                continue
            sim = self.item_to_item[item][i]
            bottom += abs(sim)
            top += sim * rating
        
        if bottom == 0.0:
            return 3.0
        
        rating = top / bottom
        return rating + 0.5  # Adjusted rating as in C++


class InputReader:
    def __init__(self, filename: str):
        self.filename = filename
        self.input: List[Tuple[int, int, int]] = []
        self.user_to_item: List[List[float]] = []
        self.parse()

    def parse(self):
        max_user = 0
        max_item = 0
        lines = []
        with open(self.filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 4:
                    continue
                user, item, rating, timestamp = map(int, parts)
                self.input.append((user, item, rating))
                max_user = max(max_user, user)
                max_item = max(max_item, item)

        # Initialize user_to_item with EMPTY
        self.user_to_item = [[EMPTY] * (max_item + 1) for _ in range(max_user + 1)]
        for user, item, rating in self.input:
            self.user_to_item[user][item] = float(rating)

    def get_input(self) -> List[Tuple[int, int, int]]:
        return self.input

    def get_user_to_item(self) -> List[List[float]]:
        return self.user_to_item


class OutputPrinter:
    def __init__(self, filename: str):
        self.filename = filename
        self.fout = open(filename, 'w')

    def add_line(self, user: int, item: int, rating: float):
        self.fout.write(f"{user}\t{item}\t{rating}\n")

    def close(self):
        self.fout.close()


def main(base_filename: str, test_filename: str):
    base_input_reader = InputReader(base_filename)
    user_to_item = base_input_reader.get_user_to_item()

    cf = CF(user_to_item)
    cf.run()

    test_input_reader = InputReader(test_filename)
    test = test_input_reader.get_input()

    output_filename = test_filename[:2] + ".base_prediction.txt"
    output_printer = OutputPrinter(output_filename)

    rmse = 0.0
    for user, item, rating in test:
        pred = cf.predict(user, item)
        rmse += (pred - rating) ** 2
        output_printer.add_line(user, item, pred)

    output_printer.close()

    rmse /= len(test)
    rmse = math.sqrt(rmse)
    print(f"RMSE: {rmse:.6f}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Please follow this format: python recommender.py [base file name] [test file name]")
        sys.exit(1)

    base_file = sys.argv[1]
    test_file = sys.argv[2]
    main(base_file, test_file)
