class Solution:
    def convertTemperature(self, celsius: float) -> [float, float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [round(kelvin, 5), round(fahrenheit, 5)]

# Example usage
solution = Solution()
print(solution.convertTemperature(36.50))  # Output: [309.65000, 97.70000]
print(solution.convertTemperature(122.11))  # Output: [395.26000, 251.79800]
