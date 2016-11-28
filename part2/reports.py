import math

from export import *

# Report functions
def get_most_played(file_name):
    exp = Exporter("reports.txt", "Title of the most played game:")
    top = 0
    records = []
    for line in open(file_name, "r"):
        record = line.strip().split("\t")
        records.append(record)
        if float(record[1]) > float(top):
            top = float(record[1])
    for record in records:
        if float(record[1]) == float(top):
            exp.report_return(record[0])
            return record[0]


def sum_sold(file_name):
    exp = Exporter("reports.txt", "Copies have been sold total:")
    top = 0
    for line in open(file_name, "r"):
        record = line.strip().split("\t")
        top += float(record[1])
    exp.report_return(top)
    return top


def get_selling_avg(file_name):
    exp = Exporter("reports.txt", "Average selling:")
    sellings = []
    for line in open(file_name, "r"):
        record = line.strip().split("\t")
        sellings.append(float(record[1]))
    exp.report_return(sum(sellings)/len(sellings))
    return sum(sellings) / len(sellings)


def count_longest_title(file_name):
    exp = Exporter("reports.txt", "Characters in longest title:")
    longest = 0
    for line in open(file_name, "r"):
        record = line.strip().split("\t")
        if len(record[0]) > longest:
            longest = len(record[0])
    exp.report_return(longest)
    return longest


def get_date_avg(file_name):
    exp = Exporter("reports.txt", "Average of release dates:")
    dates = []
    for line in open(file_name, "r"):
        record = line.strip().split("\t")
        dates.append(float(record[2]))
    exp.report_return(math.ceil(sum(dates)/len(dates)))
    return math.ceil(sum(dates) / len(dates))


def get_game(file_name, name):
    exp = Exporter("reports.txt", "Properties of selected game(" + str(name) + ")")
    for line in open(file_name, "r"):
        record = line.strip().split("\t")
        if record[0] == name:
            exp.report_return(record)
            return record



def count_grouped_by_genre(file_name):
    exp = Exporter("reports.txt", "Games grouped by genre:")
    genres = {}
    for line in open(file_name, "r"):
        record = line.strip().split("\t")
        try:
            genres[record[3]] += 1
        except KeyError:
            genres[record[3]] = 1
    exp.report_return(genres)
    return genres


def get_date_ordered(file_name):
    file_ = open(file_name, "r")
    titles = []
    titles_sorted = []
    titles_ordered = []
    records = []
    for line in file_:
        record = line.strip().split("\t")
        titles.append(record[0])
    for j in range(len(titles)):
        for i in range(len(titles)):
            if titles[i] == min(titles):
                titles_sorted.append(titles[i])
                del titles[i]
                break
    #for title in titles_sorted:
    #    if file_[:].strip().split("\t")[]:
    #        pass




print(get_most_played("game_stat.txt"))
print(sum_sold("game_stat.txt"))
print(get_selling_avg("game_stat.txt"))
print(count_longest_title("game_stat.txt"))
print(get_date_avg("game_stat.txt"))
print(get_game("game_stat.txt", "Minecraft"))
print(count_grouped_by_genre("game_stat.txt"))
#print(get_date_ordered("game_stat.txt"))
