def even_odd_swap(x):
    if len(x) % 2 != 0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters = x[1::2]
    s = ''

    for i in range(len(even_letters)):
        s = s + odd_letters[i]
        s = s + even_letters[i]

    return s


def swap_middle(x):
    if len(x) % 2 != 0:
        x = x + ' '

    first_half = x[0:int(len(x)/2)]
    second_half = x[int(len(x)/2):]

    s = second_half + first_half
    return s


def reverse(x):
    return x[::-1]


def swap_mid_rev(x):
    s_swap = swap_middle(x)
    return reverse(s_swap)


def reverse_word(x):
    words = x.split(' ')
    s = ''

    for word in words:
        s = s + reverse(word) + ' '

    return s


# BONUS IDEA 1:
# Group characters into chunks
def group_characters(x, size):
    x = x.replace(" ", "")   # remove spaces first
    groups = []

    for i in range(0, len(x), size):
        groups.append(x[i:i+size])

    return ' '.join(groups)


# BONUS IDEA 2:
# Ask user for message and encoding type
print("Encoding Methods:")
print("1. Even Odd Swap")
print("2. Reverse")
print("3. Reverse Each Word")
print("4. Swap Middle")
print("5. Swap Middle + Reverse")

x = input("\nEnter message: ")
choice = input("Choose encoding method (1-5): ")

if choice == '1':
    encoded = even_odd_swap(x)

elif choice == '2':
    encoded = reverse(x)

elif choice == '3':
    encoded = reverse_word(x)

elif choice == '4':
    encoded = swap_middle(x)

elif choice == '5':
    encoded = swap_mid_rev(x)

else:
    print("Invalid choice")
    exit()

# Optional grouping
group_size = int(input("Enter grouping size (example 3 or 4): "))
final_output = group_characters(encoded, group_size)

print("\nEncoded Message:")
print(final_output)