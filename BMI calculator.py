def calculate_bmi(weight, height):
 
  bmi = weight / (height * height)
  return bmi

def interpret_bmi(bmi):
  
  if bmi < 18.5:
    return "Underweight"
  elif bmi < 25:
    return "Normal weight"
  elif bmi < 30:
    return "Overweight"
  else:
    return "Obese"

def main():
 
  while True:
    try:
      print("Welcome to the BMI Calculator!")
      name = input("Enter your name: ")
      weight = float(input("Enter your weight in kilograms (kg): "))
      height = float(input("Enter your height in meters (m): "))
      if weight <= 0 or height <= 0:
        print("Weight and height must be positive values")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter numbers only")

  bmi = calculate_bmi(weight, height)
  bmi_category = interpret_bmi(bmi)

  print(f"Your BMI is: {bmi:.2f}")
  print(f"BMI Category: {bmi_category}")

  # Recommendation to consult a doctor
  print("**Disclaimer**\n") 
  print("THIS IS A GENERAL BMI CALCULATOR. IT IS RECOMMENDED TO CONSULT A DOCTOR OR HEALTHCARE PROFESSIONAL63 FOR PERSONALIZED GUIDANCE AND INTERPRETATION OF YOUR BMI")

if __name__ == "__main__":
  main()
