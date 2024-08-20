
def Parse_Polar(File_path):
    """
    A script for parsing Polar H10 data exported from Polar Flow web UI.
    :param File_path: Path to Polar csv file
    :return: HR data
    """
    import pandas as pd
    df = pd.read_csv(File_path)
    HR = df['HR (bpm)']

    return HR.to_numpy()

def Parse_Huawei(File_path):
   """
   Script for parsing data from Huawei Health data format. Data recorded to Huawei health and exported to csv via Health sync app.
   :param File_path: Path to Huawei csv file
   :return: HR data
   """

   from fit_tool.fit_file import FitFile
   from fit_tool.profile.messages.record_message import RecordMessage
   import numpy as np
   fit_file = FitFile.from_file(File_path)
   HR = []
   for record in fit_file.records:
       message = record.message
       if isinstance(message, RecordMessage):
           print(message.heart_rate)
           if message.heart_rate != None:
            HR.append(int(message.heart_rate))
   return np.array(HR)





