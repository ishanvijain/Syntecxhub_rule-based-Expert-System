import datetime

class MedicalExpertSystem:
    def __init__(self):
        # The Knowledge Base: A list of rules (Requirements -> Conclusion)
        self.rules = [
            ({"fever", "cough"}, "Respiratory Infection"),
            ({"Respiratory Infection", "runny_nose"}, "Common Cold"),
            ({"Respiratory Infection", "fatigue", "body_ache"}, "Influenza (Flu)"),
            ({"Respiratory Infection", "shortness_of_breath"}, "Potential Pneumonia"),
            ({"itchy_eyes", "sneezing"}, "Allergies"),
            ({"fever", "stiff_neck", "headache"}, "Meningitis (Urgent!)")
        ]
        self.facts = set()
        self.conclusions = []

    def greet(self):
        print("="*40)
        print("   AI MEDICAL DIAGNOSIS EXPERT SYSTEM   ")
        print("="*40)
        print("Please answer 'yes' or 'no' to the symptoms.\n")

    def ask_questions(self):
        symptoms_to_ask = [
            "fever", "cough", "runny_nose", "fatigue", 
            "body_ache", "shortness_of_breath", "itchy_eyes", 
            "sneezing", "stiff_neck", "headache"
        ]
        
        for s in symptoms_to_ask:
            choice = input(f"Do you have {s.replace('_', ' ')}? ").lower()
            if choice in ['yes', 'y']:
                self.facts.add(s)

    def run_inference(self):
     
        print("\n[SYSTEM] Analyzing symptoms...")
        new_inference = True
        
        while new_inference:
            new_inference = False
            for requirements, result in self.rules:
                if result not in self.facts and requirements.issubset(self.facts):
                    print(f"[LOG] Logic Triggered: {requirements} -> {result}")
                    self.facts.add(result)
                    self.conclusions.append(result)
                    new_inference = True

    def save_report(self):
        
        filename = "diagnosis_log.txt"
        with open(filename, "a") as f:
            f.write(f"\n--- Consultation Date: {datetime.datetime.now()} ---\n")
            f.write(f"Symptoms Provided: {', '.join([f for f in self.facts if f[0].islower()])}\n")
            if self.conclusions:
                f.write(f"AI Conclusions: {', '.join(self.conclusions)}\n")
            else:
                f.write("AI Conclusions: No specific condition identified.\n")
            f.write("-" * 40 + "\n")
        print(f"\n[SUCCESS] Report saved to {filename}")

    def display_results(self):
        print("\n" + "="*40)
        print("           FINAL DIAGNOSIS             ")
        print("="*40)
        if not self.conclusions:
            print("The AI could not find a matching condition.")
        else:
            for c in self.conclusions:
                print(f"-> {c}")
        print("="*40)

if __name__ == "__main__":
    engine = MedicalExpertSystem()
    engine.greet()
    engine.ask_questions()
    engine.run_inference()
    engine.display_results()
    engine.save_report()