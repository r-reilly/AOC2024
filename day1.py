f = open("input1.txt", "r")
lines = f.readlines()

left_list = list()
right_list = list()
for line in lines:
    parts = line.split()
    left = parts[0]
    left_list.append(left)
    right = parts[1]
    right_list.append(right)

##### part 1 ####
def calc_distances(data1, data2):
    data1.sort()
    data2.sort()
    diff_list = list()
    for d1, d2 in zip(data1, data2):
        diff = abs(int(d1)-int(d2))
        diff_list.append(diff)
    return diff_list

diff_list = calc_distances(left_list, right_list)

def sum_list(data):
    num = sum(data)
    return num

ans = sum_list(diff_list)

# print(ans)

##### part 2 ####

def similarity_score(data1, data2):
    score = 0
    for d1 in data1:
        mode = 0
        for d2 in data2:
            if d1 == d2:
                mode += 1
        score += int(d1)*mode
    return score

# print(similarity_score(left_list, right_list))
