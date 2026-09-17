text = "madam"

left = 0
right = len(text) - 1

while left < right:
    if text[left] != text[right]:
        print("Not a palindrome")
        break

    left += 1
    right -= 1
else:
    print("Palindrome")
