def main():
    print("this is program to convert dollar into rupees")
    print()


    dollars = int(input("Enter your dollar : "))

    rupees = convert_to_rupees(dollars)

    print("this is " , rupees, "rupees.")

convert_to_rupees =  lambda rupees : rupees * 82.91

main()