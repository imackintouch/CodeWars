def number_nines(s,n):
    count = 0
    for i in range(s, n+1):
        if '9' in str(i):
            count += 1
    return count

def main():
    s,n = 0,0
    while s>=0 and n>= 0:
        data = input("Please input a numerical range(-1 to quit): ")
        s, n = int(data.split(',')[0]), int(data.split(',')[1])
        print(f"Number of numbers between {s} and {n} with 9's is:{number_nines(s,n)}")

if __name__ == '__main__':
    main()