# Container With Most Water
"""
Problem Statement

You are given an array of heights.

Each height represents a vertical line.

Find two lines that can store the maximum amount of water."""


height = [1,8,6,2,5,4,8,3,7]

left = 0
right = len(height)-1
max_water = 0
while left < right:
    width = right - left

    h = min(height[left], height[right])

    area = width*h

    max_water = max(max_water, area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(max_water)