raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
raffle_prizes = []
raffle_prizes += raffle.pop(223842, "No prize")

print(raffle)
raffle_prizes_joined = "".join(raffle_prizes)
print(raffle_prizes)
print(raffle_prizes_joined)

