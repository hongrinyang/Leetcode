class Solution:
    def sampleStats(self, count):
        # Initialize variables
        minimum = -1
        maximum = -1
        sum_elements = 0
        total_count = 0
        mode = 0
        max_count = 0

        for i in range(256):
            if count[i] > 0:
                if minimum == -1:
                    minimum = i
                maximum = i
                sum_elements += i * count[i]
                total_count += count[i]
                if count[i] > max_count:
                    max_count = count[i]
                    mode = i

        mean = sum_elements / total_count

        # Finding median
        mid1, mid2 = None, None
        cumulative_count = 0
        half_total_count = total_count / 2
        for i in range(256):
            cumulative_count += count[i]
            if mid1 is None and cumulative_count >= half_total_count:
                mid1 = i
            if mid2 is None and cumulative_count > half_total_count:
                mid2 = i
                break

        if total_count % 2 == 0:
            median = (mid1 + mid2) / 2
        else:
            median = mid2

        return [float(minimum), float(maximum), mean, median, float(mode)]