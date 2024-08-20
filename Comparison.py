"""
A script for comparing Polar H10 data in comparison to Huawei watch GT4 heart rate data
"""

from fit_tool.fit_file import FitFile
import Parsers
from matplotlib import pyplot as plt

File_path_Polar = "Data/Polar Flow.CSV"
File_path_Huawei = "Data/Huawei Health.csv"
File_path_Huawei = "Data/Huawei.fit"

Polar_data = Parsers.Parse_Polar(File_path_Polar)
Huawei_data = Parsers.Parse_Huawei(File_path_Huawei)

print(Polar_data)
print(Huawei_data)

print(Polar_data.shape)
print(Huawei_data.shape)

Polar_data = Polar_data[:len(Huawei_data)]

plt.figure()
plt.title("Polar H10 vs Huawei Watch GT4 heart rate")
plt.subplot(2,1,1)
plt.suptitle("HR time comparison")
plt.plot(Polar_data, "r")
plt.plot(Huawei_data, "b")
plt.legend(["Polar", "Huawei"])
plt.subplot(2,1,2)
plt.scatter(Polar_data, Huawei_data)
plt.xlabel("Polar HR")
plt.ylabel("Huawei HR")



plt.show()

