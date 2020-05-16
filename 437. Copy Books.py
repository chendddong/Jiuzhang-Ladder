'''
Given n books and the i-th book has pages[i] pages. There are k persons to
copy these books.

These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Return the shortest time that the slowest copier spends.
The sum of book pages is less than or equal to 2147483647

Example
Example 1:

Input: pages = [3, 2, 4], k = 2
Output: 5
Explanation: 
    First person spends 5 minutes to copy book 1 and book 2.
    Second person spends 4 minutes to copy book 3.
Example 2:

Input: pages = [3, 2, 4], k = 3
Output: 4
Explanation: Each person copies one of the books.

'''
# TAG:[Binary Search, Search the answer]

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages:
            return 0

        # Narrow down the start and end
        start, end = max(pages), sum(pages)

        while start + 1 < end:
            mid = (start + end) // 2
            # Every one has mid minutes for copying the book, can we finish?
            if self.can_finish_copy(mid, pages, k):
                end = mid
            else:
                start = mid

        if self.can_finish_copy(start, pages, k):
            return start
        return end

    def can_finish_copy(self, time, pages, k):
        count = 1 # how many people are copying
        time_cost = 0 # the time that cost by the current guy
        # Go over all the books from first to last, count how many people
        for page in pages:
            # Need one more people for the job
            if time_cost + page > time:
                count += 1
                time_cost = 0
            time_cost += page

        return count <= k



# Takeaways:
# Take proper 'Guess' of the answer you wanna search for