"""
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""

from typing import List

# Sort before merging + List to store merged intervals
def merge_intervals(intervals: List[List]) -> List[List]:
    # Sort based on start value of intervals
    intervals.sort(key=lambda interval: interval[0])
    i = 1
    final_intervals = [intervals[0]]

    while i < len(intervals):
        # Merge condition
        if final_intervals[-1][1] >= intervals[i][0]:
            # End value after merge?
            final_intervals[-1][1] = max(final_intervals[-1][1], intervals[i][1])
        else:
            final_intervals.append(intervals[i])
        i += 1

    return final_intervals

# Sort before merging + del operation (Slower)
def merge_intervals_del(intervals: List[List]) -> List[List]:
    # Sort based on start value of intervals
    intervals.sort(key=lambda interval: interval[0])
    i = 0
    while i < len(intervals) - 1:
        # Merge condition
        if intervals[i][1] >= intervals[i + 1][0]:
            # End value after merge?
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            # Delete the next element after merge
            # Can be expensive
            del intervals[i + 1]
        else:
            i += 1

    return intervals


# Swap and merge
# Exceeds time limit for large values of intervals
def merge_intervals_n2(intervals: List[List]) -> List[List]:
    i = 0
    while i < len(intervals) - 1:
        j = i + 1
        merged = False
        while j < len(intervals):
            if intervals[i][0] > intervals[j][0]:
                intervals[i], intervals[j] = intervals[j], intervals[i]
                j = i + 1
                continue
            if intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                del intervals[j]
                merged = True
            else:
                j += 1
        if not merged:
            i += 1
    return intervals
merge_intervals_n2([[1,3],[2,6],[8,10],[15,18]])
