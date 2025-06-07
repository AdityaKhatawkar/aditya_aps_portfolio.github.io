import heapq

# Model: Stores active bids and runs the auction
class AuctionModel:
    def __init__(self):
        self.bids = []  # list of (ad_id, bid, quality)
    
    def add_bid(self, ad_id, bid, quality):
        self.bids.append((ad_id, bid, quality))

    def run_auction(self):
        # Compute AdRank = bid * quality for each bid
        adranks = [(bid * quality, ad_id, bid, quality) for ad_id, bid, quality in self.bids]
        # Find top two AdRanks
        top2 = heapq.nlargest(2, adranks, key=lambda x: x[0])
        if not top2:
            return None
        winner = top2[0]
        price = 0
        if len(top2) > 1:
            # Second-price: (second highest AdRank / winner quality) + epsilon
            second_adrank = top2[1][0]
            price = second_adrank / winner[3] + 0.01
        return {'winner': winner[1], 'price': price}

# Controller: Accepts bids and triggers auction resolution
class AuctionController:
    def __init__(self, model):
        self.model = model

    def place_bid(self, ad_id, bid_amount, quality_score):
        self.model.add_bid(ad_id, bid_amount, quality_score)

    def resolve(self):
        return self.model.run_auction()

# View: Displays the auction result
class AuctionView:
    def display_result(self, result):
        if result:
            print(f"Winning Ad: {result['winner']}, Price: ${result['price']:.2f}")
        else:
            print("No bids placed.")

# Example usage
if __name__ == "__main__":
    model = AuctionModel()
    controller = AuctionController(model)
    view = AuctionView()

    # Simulate bid placements
    controller.place_bid("AdA", 5.0, 0.8)
    controller.place_bid("AdB", 6.0, 0.5)
    controller.place_bid("AdC", 4.5, 0.9)

    # Run auction and display result
    result = controller.resolve()
    view.display_result(result)
