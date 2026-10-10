from groq import generate_response
def reinforcement_learning_activity():
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")
    prompt = input("Please enter a prompt for the AI model(e.g. 'Describe the lion')").strip()
    if not prompt:
        print("Please enter a prompt to run the activity")
        return
    initial_response = generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"\nInitial AI Response: {initial_response}")
    try:
        rating = int(input("Rate the response from 1(bad) to 5(good): ").strip())
        if rating < 1 or rating > 5:
            print("Invalid rating.Using 3")
            rating = 3
    except ValueError:
        print("Invalid rating. Using 3.")
        rating = 3
    feedback = input("Provide feedback for imrovement: ").strip()
    improved_response = f"{initial_response} (Improved with your feedback: {feedback})"
    print("\nReflection:")
    print("1.How did the model's response improve with feedback?")
    print("2.How does reinforcement learning help AI to improve its perfomance over time?")
def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY")
    category = input("Enter a specific category (e.g. science,history,math): ").strip()
    item = input(f"Enter a specific {category} topic (e.g. photosynthesis for science)").strip()
    if not category or not item:
        print("Pleassse fill in both fields to run the activity")
        return
    teacher_prompt = f"You are a teacher.Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}.Explain {item} in a dsetailed,tecnical manner"
    teacher_response = generate_response(expert_prompt,temperature=0.3,max_tokens=1024)
    expert_response = generate_response(expert_prompt,temperature=0.3,max_tokens=1024)
    print(f"\n Tecaher's perspective {teacher_response}")
    print(f"\n Expert's perspective")
    print("\nReflection")
    print("1.How did the AI's response differ b/w the teacher's and expert's perspectives?")
    print("2.How can role-based tailor responses for different contexts?")
    def run_activity():
        print("\n AI Learning Activity")
        print("Choosen an activity:")
        print("1)Reinforcement learning")
        print("2)Rol;e-based prompts")
        choice = input("> ").strip()]
        if choice == "1":
            reinforcement_learning_activity()
        elif choice == "2":
            role_based_prompt_activity()
        else:
            print("Invalid choice please choose 1 or 2")
if __name__ == "__main__":
    run_activity()