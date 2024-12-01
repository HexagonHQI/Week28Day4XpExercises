#EXercise 1:
import random

def get_words_from_file(filename):
    """Read words from a file and return them as a list."""
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

def get_random_sentence(length, words):
    """Generate a random sentence of a specified length."""
    random_words = random.choices(words, k=length)
    sentence = ' '.join(random_words).lower() + '.'
    return sentence

def main():
    print("Welcome to the Random Sentence Generator!")
    print("You can generate a random sentence with a specified number of words (between 2 and 20).")
    
    try:
        length = int(input("How long do you want the sentence to be? (2-20): "))
        if length < 2 or length > 20:
            raise ValueError("Length must be between 2 and 20.")
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    words = get_words_from_file('word_list.txt')  
    sentence = get_random_sentence(length, words)
    print("Generated Sentence:", sentence)

if __name__ == "__main__":
    main()
#Exercise 2:

import json


sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)
data["company"]["employee"]["birth_date"] = "1990-01-01" 
with open('employee_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Updated JSON saved to employee_data.json")