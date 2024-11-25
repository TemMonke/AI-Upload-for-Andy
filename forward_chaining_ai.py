import pandas as pd
import time
start_time = time.time()
# Load the dataset from the CSV file
df = pd.read_csv('customer_data.csv')

# Define the forward chaining rule-based system
def apply_rules(customer):
    # Start with known facts
    facts = {}

    # Rule 1: If Monthly Income > 3000, Time Spent on Website > 10 minutes, and Discount Available = Yes, then Purchase = Yes
    if customer['Income'] > 3000 and customer['Time Spent on Website'] > 10 and customer['Discount Available'] == 'Yes':
        facts['Purchase'] = 'Yes'
    
    # Rule 2: If Age < 30 and Previous Purchases > 0, then Purchase = Yes
    if customer['Age'] < 30 and customer['Previous Purchases'] > 0:
        facts['Purchase'] = 'Yes'

    # Rule 3: If Product Category = Electronics and Gender = Male and Device Used = Mobile, then Purchase = Yes
    if customer['Product Category'] == 'Electronics' and customer['Gender'] == 'Male' and customer['Device Used'] == 'Mobile':
        facts['Purchase'] = 'Yes'

    # Rule 4: If Gender = Male and Income < 2000, then Purchase = No
    if customer['Gender'] == 'Male' and customer['Income'] < 2000:
        facts['Purchase'] = 'No'
    
    # Rule 5: If Discount Available = No, then Purchase = No
    if customer['Discount Available'] == 'No':
        facts['Purchase'] = 'No'

    # If no rule applies, default to "No purchase"
    if 'Purchase' not in facts:
        facts['Purchase'] = 'No'

    return facts['Purchase']

# Apply forward chaining to each row in the dataset
df['Predicted Purchase'] = df.apply(apply_rules, axis=1)

# Display the dataset with predictions
print(df[['Age', 'Income', 'Gender', 'Previous Purchases', 'Time Spent on Website', 
          'Discount Available', 'Product Category', 'Time of Visit', 'Device Used', 'Purchase', 'Predicted Purchase']].head())

#Save the predictions into a seperate file for comparison
df.to_csv('customer_predictions.csv', index=False)
print("Predictions saved to 'customer_predictions.csv'.")
print("--- %s seconds ---" % (time.time() - start_time))
