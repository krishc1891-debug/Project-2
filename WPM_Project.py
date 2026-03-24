import time

def calculate_wpm(characters_typed, elapsed_seconds):
    
    if elapsed_seconds <= 0 or characters_typed <= 0:
        return 0.0
    
    words_typed = characters_typed / 5.0
    minutes = elapsed_seconds / 60.0
    wpm = words_typed / minutes
    
    return wpm


def calculate_accuracy(expected_text, typed_text):
    
    if len(expected_text) == 0:
        return 0.0
    
    correct_matches = 0
    
    for i in range(len(expected_text)):
         if i < len(expected_text) and typed_text[i] == expected_text[i]:
             correct_matches += 1
        
    
    accuracy = correct_matches / len(expected_text) * 100
    
    return accuracy


def get_test_text(level):
    
    
    if level == "Easy":
        return "The quick brown fox jumps over the lazy dog"
    elif level == "Medium":
        return "He went to the library to study for his final exams, which are next week"
    elif level == "Hard":
        return "The human body is an amazing machine that performs countless functions every day"
    else:
        return "He went to the library to study for his final exams, which are next week"

def run_single_test(level):
    
    
    expected_text = get_test_text(level)
    
    print("Your text here:")
    print(expected_text)
    
    input("Press ENTER when you are ready to start typing")
    print(" ")
    
    start_time = time.time()
    
    typed_text = input()
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    wpm = calculate_wpm(len(typed_text), elapsed)
    
    accuracy = calculate_accuracy(expected_text, typed_text)
    
    print(" ")
    print(" ")
    print("Time taken (seconds):", elapsed)
    print("Words per minute:", wpm)
    print("Accuracy (%):", accuracy)
    
    d = {"level":level, "elapsed": elapsed, "wpm":wpm, "accuracy": accuracy} 
    
    return d


def choose_level():
    print(" ")
    print("Options: 1) Easy  2) Medium  3) Hard")
    user_input = input()
    
    if user_input == "1":
        return "Easy"
    elif user_input == "3":
        return "Hard"
    else:
        return "Medium"

def show_history(history):
    if not history:
        print("No tests were taken in this session.")
        return

    print("\nSession summary:")
    print("-----------------")

    for i, result in enumerate(history, start=1):
        level = result["level"]
        elapsed = result["elapsed"]
        wpm = result["wpm"]
        accuracy = result["accuracy"]

        print(f"Test #{i}:")
        print(f"  Level   : {level}")
        print(f"  Time    : {elapsed:.2f} seconds")
        print(f"  WPM     : {wpm:.1f}")
        print(f"  Accuracy: {accuracy:.1f}%")
        print()


def main():
    
    print("Welcome to the Typing Speed Test!")
    print("You will see a sentence based on the difficulty you choose.")
    print("Type it as quickly and accurately as you can, then press ENTER")
    
    history = []
    
    while True:
        level = choose_level()
        result = run_single_test(level)
        history.append(result)
        again = input("Do another test? (y/n)")
        
        if again.lower() != "y":
            break
        
    show_history(history)
    print("Goodbye")
    
if __name__ == "__main__":
    main()






