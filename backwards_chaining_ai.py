#Generated with ChatGPT
#OpenAI. (2024). ChatGPT (November 2024 version) [AI model]. Retrieved from https://chat.openai.com/

import pandas as pd
import time
start_time = time.time()
# Load the dataset from the CSV file
df = pd.read_csv('customer_data.csv')

# Define the backward chaining rule-based system
def backward_chaining(goal, customer):
    # Define rules as functions
    def rule1():
        return customer['Income'] > 3000 and customer['Time Spent on Website'] > 10 and customer['Discount Available'] == 'Yes'
    
    def rule2():
        return customer['Age'] < 30 and customer['Previous Purchases'] > 0
    
    def rule3():
        return customer['Product Category'] == 'Electronics' and customer['Gender'] == 'Male' and customer['Device Used'] == 'Mobile'
    
    def rule4():
        return customer['Gender'] == 'Male' and customer['Income'] < 2000
    
    def rule5():
        return customer['Discount Available'] == 'No'
    
    # Backward chaining process
    if goal == "Purchase = Yes":
        # Check if any rule concludes 'Yes'
        if rule1():
            return True
        if rule2():
            return True
        # If none of the rules support 'Yes', return False
        return False
    
    elif goal == "Purchase = No":
        # Check if any rule concludes 'No'
        if rule3():
            return True
        if rule4():
            return True
        if rule5():
            return True
        # If none of the rules support 'No', return False
        return False
    
    # Default to no conclusion
    return False

# Apply backward chaining to predict purchase for each customer
def predict_purchase(customer):
    # Try to prove "Purchase = Yes"
    if backward_chaining("Purchase = Yes", customer):
        return "Yes"
    # Otherwise, conclude "Purchase = No"
    if backward_chaining("Purchase = No", customer):
        return "No"
    # Default if neither goal is provable
    return "No"

# Apply the backward chaining system to each customer in the dataset
df['Predicted Purchase'] = df.apply(lambda row: predict_purchase(row), axis=1)

# Display the dataset with predictions
print(df[['Age', 'Income', 'Gender', 'Previous Purchases', 'Time Spent on Website',
          'Discount Available', 'Product Category', 'Time of Visit', 'Device Used', 'Purchase', 'Predicted Purchase']].head())

#Save the predictions into a seperate file for comparison
df.to_csv('customer_predictions_backward.csv', index=False)
print("Predictions saved to 'customer_predictions_backward.csv'.")
print("--- %s seconds ---" % (time.time() - start_time))
