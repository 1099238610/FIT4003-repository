import csv
import pandas as pd

def write_csv():
    header_list = ["Project", "Name", "Category", "status", "url", "Participate", "Comment", "Comment date"]

    with open("../result/issue_data.csv", mode="w", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(header_list)
        data = read_source()
        for project in data:
            for issue in project['issue_list']:
                print(issue)


def read_source():
    label = ['project', 'issue_status', 'issue_num', 'item_type']

    reader = csv.DictReader(open("../source/issue_track_data.csv"), label)
    res_list = []
    for row in reader:
        res_list.append(row)
    return res_list


def collect_issue_status():
    res_list = read_source()[1:]
    issue_list = []
    same_issues = []
    for i in range(len(res_list) - 1):
        if res_list[i]['issue_num'] == res_list[i + 1]['issue_num']:
            same_issues.append(res_list[i]['issue_num'])
        else:
            same_issues.append(res_list[i]['issue_num'])
            issue_list.append(same_issues)
            same_issues = []

    return issue_list


if __name__ == '__main__':
    res_list = collect_issue_status()
    print(len(res_list))
    for i in res_list:
        print(i)
