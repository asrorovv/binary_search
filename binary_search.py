def binary_search(exx):
    try:
        exx.sort()
        x = len(exx)
        #Agar toq son uchun
        if x % 2 == 0:
            mid = x // 2
            med = exx[mid]
        else:
            mid1 = x // 2
            mid2 = mid1 - 1
            med = (exx[mid1] + exx[mid2]) / 2
        return med
    except Exception as error:
        print(f"Error!: {error}")

def main():
    try:
        #userdan nechta raqamni o'rta arifmetigini topishni so'raydi va nechini kiritgan bo'lsa shunga input qilib so'raydi
        n = int(input("Raqamni kiriting: "))
        nums = []
        for i in range(n):
            num = float(input(f"{i + 1} - raqamni kiriting: "))
            nums.append(num)
        med = binary_search(nums)
        print(f"Kiritilgan raqamlar o'rta arifmetigi: {med}")
    except Exception as error:
        print(f"Error!: {error}")
if __name__ == '__main__':
    main()