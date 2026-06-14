# Rule-Based Expert System using Forward Chaining

class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion


# -----------------------------
# Knowledge Base (Rule Base)
# -----------------------------
rules = [
    Rule(["fever", "cough"], "flu"),
    Rule(["cold", "cough"], "common_cold"),
    Rule(["sneezing", "runny_nose"], "allergy"),
    Rule(["headache", "fever"], "viral_fever"),
    Rule(["stomach_pain", "vomiting"], "food_poisoning"),

    # Second-level inference
    Rule(["flu", "body_pain"], "severe_flu"),
    Rule(["common_cold", "body_pain"], "viral_infection"),
    Rule(["viral_fever", "fatigue"], "high_viral_infection"),
    Rule(["allergy"], "take_antihistamine"),
    Rule(["food_poisoning"], "drink_fluids"),

    # Third-level inference
    Rule(["severe_flu"], "consult_doctor"),
    Rule(["viral_infection"], "take_rest"),
    Rule(["high_viral_infection"], "medical_checkup"),
    Rule(["consult_doctor", "high_viral_infection"], "urgent_attention"),
    Rule(["medical_checkup"], "follow_prescription"),

    # Additional chaining
    Rule(["take_rest", "drink_fluids"], "recovery_plan"),
    Rule(["recovery_plan"], "monitor_health"),
    Rule(["urgent_attention"], "hospital_visit")
]


# -----------------------------
# User Input (Facts Base)
# -----------------------------
facts = set()

print("=" * 60)
print("RULE-BASED MEDICAL EXPERT SYSTEM")
print("=" * 60)

print("\nEnter symptoms separated by commas")
print("Example:")
print("fever,cough,body_pain")
print("cold,cough,body_pain")
print("headache,fever,fatigue")

user_input = input("\n>> ")

# Store original user facts
user_facts = set()

for symptom in user_input.split(","):
    symptom = symptom.strip().lower()

    if symptom:
        facts.add(symptom)
        user_facts.add(symptom)


# -----------------------------
# Forward Chaining Inference
# -----------------------------
inference_log = []

changed = True

while changed:
    changed = False

    for rule in rules:

        # Check if all rule conditions are satisfied
        if all(condition in facts for condition in rule.conditions):

            # Add new fact if not already present
            if rule.conclusion not in facts:

                facts.add(rule.conclusion)

                log = (
                    f"Rule Fired: "
                    f"{' AND '.join(rule.conditions)} "
                    f"-> {rule.conclusion}"
                )

                inference_log.append(log)

                changed = True


# -----------------------------
# Output Results
# -----------------------------
print("\n" + "=" * 60)
print("INITIAL FACTS")
print("=" * 60)

for fact in sorted(user_facts):
    print(f"• {fact}")

print("\n" + "=" * 60)
print("INFERENCE STEPS")
print("=" * 60)

if inference_log:
    for step in inference_log:
        print(step)
else:
    print("No rules matched the given symptoms.")

# Derived conclusions
derived_facts = facts - user_facts

print("\n" + "=" * 60)
print("FINAL CONCLUSIONS")
print("=" * 60)

if derived_facts:
    for fact in sorted(derived_facts):
        print(f"• {fact}")
else:
    print("No conclusions could be inferred.")

print("\n" + "=" * 60)
print("ALL KNOWN FACTS")
print("=" * 60)

for fact in sorted(facts):
    print(f"• {fact}")






  