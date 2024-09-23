def main():
    mass = int(input("m: "))
    energy = mass * (300000000 ** 2) # 300000000 approximately the speed of light
    energy = "{:0.0f}".format(energy) # necessary for python to don't show scientific notation
    print(f"E: {energy}")


main()

