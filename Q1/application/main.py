import sys

def run_application():
  import sklearn
  import joblib
  import pandas as pd
  columns = ['CHP1Temp1(Deg C)','CHP1Temp2(Deg C)','CHP2Temp1(Deg C)','CHP2Temp2(Deg C)',
            'CHP1Vib1(mm/s)','CHP1Vib2(mm/s)','CHP2Vib1(mm/s)','CHP2Vib2(mm/s)']
  input_collection = {}
  stop = False
  for i in columns:
    if stop:
      sys.exit("Thank You and Good Bye!")
    while True:
      try:
        val = input(f"{i} :")
        if val == 'exit':
          stop = True
          break
        val_num = float(val)
        input_collection[i] = [val_num]
        break
      except:
        print(f'Please enter number on {i} field')
  try:
    data = pd.DataFrame.from_dict(input_collection)
  except:
    print("Something wrong in data framing")
    sys.exit("Force Exit!")
  try:
    scaler = joblib.load('model/scaler/NS.joblib')
    model = joblib.load('model/RandomForest.joblib')
  except:
    print("Failed to load model and scaler")
    sys.exit("Force Exit!")
  try:
    data_scaled = scaler.transform(data)
    result = model.predict(data_scaled)
  except:
    print('Failed to scale and predict the data')
    sys.exit("Force Exit!")
  try:
    if result[0] == 0:
      print("\nNormal\n")
    else:
      print("\nFaulty\n")
  except:
    print("Failed to convert the prediction result")
    sys.exit("Force Exit!")


print("\nWelcome to ML PROGRAM\n")
choice = input("Do you want to insert data for prediction? y/n -> ")
print("\n")
if choice == "y":
  run_ = True
  while run_:
    run_application()
    user_choice = input("Do you want to insert again? y/n -> ")
    print("\n")
    if user_choice == "n":
      run_ = False
  sys.exit("See you later!")
else:
  sys.exit("Have a good day!")
  
