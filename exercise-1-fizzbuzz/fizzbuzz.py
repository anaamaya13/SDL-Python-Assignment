import argparse
import sys

def fizzbuzz_game(max_num, rules):
    for i in range(1, max_num + 1, 1):
        output = ""
        for factor, word in rules.items():
            if i % factor == 0:
                output += word
        print(output if output else i)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FizzBuzz Game.")
    
    # Allows the user to define the max number 
    parser.add_argument("-n", "--max", type=int, default=100, help="Maximun number")
    
    #Allows the user to define numbers and replacement words 
    #Example: --rule 3 Fizz --rule 5 Buzz --rule 7 Fang
    parser.add_argument("--rule", action="append", nargs=2, metavar=("Factor", "Replacement Word"),
                        help="Add a factor and its replacement word")

    args = parser.parse_args()
    
   # The basic rules already established-- dict
    user_rules = {3: "Fizz", 5: "Buzz", 7: "Fang", 11: "Bang"} 

    #If the user adds new rules, theay are added to the dictionary
    if args.rule:
        for factor, word in args.rule:
            user_rules[int(factor)] = word
        
fizzbuzz_game(args.max, user_rules)