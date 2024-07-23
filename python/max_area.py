def max_area_op(array):
    left =0
    right = len(array)-1
    max_area =0
    while (left< right):
        area = min(array[left], array[right] ) * (right -left)
        max_area = max(area,max_area)
        if array[left] < array[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(max_area_op([7,3,5,6,8,4]))