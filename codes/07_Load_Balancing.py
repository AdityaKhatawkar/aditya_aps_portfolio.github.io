class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_next_server(self):
        next_server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return next_server


def main():
    servers = ["Server1", "Server2", "Server3"]
    lb = LoadBalancer(servers)
    requests = 8
    for i in range(requests):
        next_server = lb.get_next_server()
        print(f"Request {i + 1} directed to: {next_server}")


if __name__ == "__main__":
    main()
