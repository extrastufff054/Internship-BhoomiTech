import json

def summarize_json(json_data):
    # Process and summarize the JSON data
    summary = ""
    for key, value in json_data.items():
        summary += f"{key}: {str(value)}\n"
    
    return summary

# Read the JSON file
with open('input.json') as file:
    data = json.load(file)

# Generate the summary
summary = summarize_json(data)

# Save the summary to a text file
with open('summary.txt', 'w') as file:
    file.write(summary)
