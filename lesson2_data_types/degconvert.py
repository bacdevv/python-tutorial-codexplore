def cToF():
    while True:
        cTemp = input("Enter your temperature: ")
        if cTemp:
            cTemp = float(cTemp)
            fTemp = round(cTemp * (9/5) + 32, 1)
            print(f"{round(cTemp)}C to {fTemp}F")
            break
        else:
            print("Empty, type again")
            continue
def main():
    cToF()

if __name__ == '__main__':
    main()