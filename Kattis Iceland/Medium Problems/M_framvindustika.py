percent_of_complete, load_bar_size = map(int, input().split())

if 0 < percent_of_complete <= 100:
    hashes = int(load_bar_size * percent_of_complete / 100)
    dashes_amount = load_bar_size - hashes

    dashes = "[" + "#" * hashes + "-" * dashes_amount + "]"
    if len(str(percent_of_complete)) == 1:
        percent = f"  {percent_of_complete}%"
    elif len(str(percent_of_complete)) == 2:
        percent = f" {percent_of_complete}%"
    elif len(str(percent_of_complete)) == 3:
        percent = f"{percent_of_complete}%"

else:
    dashes = "[" + "-" * load_bar_size + "]"
    if len(str(percent_of_complete)) == 1:
        percent = f"  {percent_of_complete}%"
    elif len(str(percent_of_complete)) == 2:
        percent = f" {percent_of_complete}%"
    elif len(str(percent_of_complete)) == 3:
        percent = f"{percent_of_complete}%"
print(f"{dashes} | {percent}")
