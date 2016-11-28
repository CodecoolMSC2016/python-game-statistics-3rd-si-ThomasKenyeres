# Report functions
def count_games(file_name):
    count = 0
    file_ = open(file_name, "r")
    for line in file_:
        count += 1
    file_.close()
    return count


def decide(file_name, year):
    file_ = open(file_name, "r")
    for line in file_:
        record = line.strip().split("\t")
        if int(record[2]) == year:
            return True
    return False


def get_latest(file_name):
    file_ = open(file_name, "r")
    latest_year = 0
    latest_title = ""
    for line in file_:
        record = line.strip().split("\t")
        if int(record[2]) > latest_year:
            latest_year = int(record[2])
            latest_title = str(record[0])
    return latest_title


def count_by_genre(file_name, genre):
    file_ = open(file_name, "r")
    count = 0
    for line in file_:
        record = line.strip().split("\t")
        if record[3] == genre:
            count += 1
    return count


def get_line_number_by_title(file_name, title):
    file_ = open(file_name, "r")
    line_num = 0
    for line in file_:
        line_num += 1
        record = line.strip().split("\t")
        if record[0] == title:
            return line_num
    raise ValueError


def sort_abc(file_name):
    file_ = open(file_name, "r")
    titles = []
    titles_sorted = []
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
    return titles_sorted


def get_genres(file_name):
    file_ = open(file_name, "r")
    genres = []
    genres_sorted = []
    for line in file_:
        record = line.strip().split("\t")
        if not record[3] in genres:
            genres.append(record[3])
    for j in range(len(genres)):
        for i in range(len(genres)):
            if genres[i] == min(genres):
                genres_sorted.append(genres[i])
                del genres[i]
                break
    return genres_sorted


def when_was_top_sold_fps(file_name):
    file_ = open(file_name, "r")
    top = 0
    records = []
    for line in file_:
        record = line.strip().split("\t")
        records.append(record)
        if float(record[1]) > float(top) and (record[3] == "First-person shooter"):
            top = record[1]
    for record in records:
        if record[1] == top:
            return record[2]
