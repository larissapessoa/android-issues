import time
import datetime


def get_date_list(days):
    today = datetime.datetime.today()
    # list of dates from now until 'days' days from now.
    date_list = [today - datetime.timedelta(days=x) for x in range(days)]
    date_list = [str(x.year) + '-' + str(x.month) + '-' + str(x.day) for x in date_list]
    for i in range(len(date_list)):
        if date_list[i][-2] == "-":
            # If the date is single-digits i.e. 2019-10-1 -> 2019-10-01
            date_list[i] = date_list[i][:-1] + "0" + date_list[i][-1]
        if date_list[i][-5] == "-":
            date_list[i] = date_list[i][:-4] + "0" + date_list[i][-4] + date_list[i][-3:]
    return date_list


def main():
    # setup, owner name, access_token and headers
    infile = open("token.txt", 'r')
    access_token = infile.read()
    headers = {'Authorization': "Token " + access_token}
    date_list = get_date_list(1440)


if __name__ == "__main__":
    main()
