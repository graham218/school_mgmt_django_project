def accountNumberToPk(account_number):
    for i in range(len(account_number)):
        if account_number[i] != 'B' and account_number[i] != '0':
            return int(account_number[i:])
    return -1









