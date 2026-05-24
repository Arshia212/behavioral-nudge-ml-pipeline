# 1. Data Ingestion & Preprocessing
def ingest_patient_data(raw_input):
    # Parse input (e.g., JSON from app or EHR) to structured format
    patient_profile = parse_profile(raw_input)
    patient_history = parse_medical_history(raw_input)
    # ... include symptoms, med schedule, device data, etc.
    return normalize_data({**patient_profile, **patient_history})

patient = ingest_patient_data(synthetic_patient_input)
# 'patient' now contains cleaned fields like age, AF_diagnosis_duration, medications, 
# adherence_history, symptom_triggers, preferences, etc.

# 2. Behavioral Readiness Assessment (COM-B or similar model)
def assess_behavioral_profile(patient):
    profile = {}
    # Evaluate Capability: e.g., knowledge test score, physical ability, health literacy
    profile['capability'] = evaluate_capability(patient)
    # Evaluate Opportunity: e.g., social support score, routine, environmental cues
    profile['opportunity'] = evaluate_opportunity(patient)
    # Evaluate Motivation: e.g., self-motivation rating, past adherence behavior
    profile['motivation'] = evaluate_motivation(patient)
    return profile

behavior_profile = assess_behavioral_profile(patient)
# Example output: behavior_profile = {'capability': 'low', 'opportunity': 'moderate', 'motivation': 'low'}

# 3. Identify Target Behavior and Barrier
target_behavior = determine_target_behavior(patient) 
# e.g., "medication_adherence" or "daily_exercise" based on care plan or risk assessment

barrier = identify_key_barrier(behavior_profile, target_behavior)
# e.g., returns "low motivation" or "knowledge gap" etc., possibly using rules:
# if capability is low for the required behavior, barrier = "capability";
# elif motivation is low, barrier = "motivation"; etc.

# 4. Nudge Strategy Selection using Behavioral Frameworks
def select_nudge_strategy(target_behavior, barrier):
    # Choose a nudge type or technique based on the barrier and desired behavior.
    if barrier == "capability":
        strategy = "Education"            # Focus on increasing knowledge/skills
    elif barrier == "opportunity":
        strategy = "EnvironmentalPrompt"  # Reminder or environmental restructuring
    elif barrier == "motivation":
        strategy = "MotivationalNudge"    # Leverage incentives, social proof, etc.
    # Incorporate MINDSPACE/EAST principles into the chosen strategy:
    strategy_design = apply_framework_principles(strategy, frameworks=["MINDSPACE","EAST"])
    return strategy_design

nudge_plan = select_nudge_strategy(target_behavior, barrier)
# nudge_plan might include details like 
# {"type": "MotivationalNudge", "principles_applied": ["Social","Attractive","Timely"]}

# 5. Personalized Content Selection
def personalize_nudge_content(nudge_plan, patient):
    nudge_type = nudge_plan["type"]
    # Select or generate content tailored to patient characteristics
    if nudge_type == "Education":
        content = choose_educational_content(topic=target_behavior, level=patient.knowledge_level)
        # E.g., a fact sheet about AF and stroke risk, if knowledge is low
    elif nudge_type == "EnvironmentalPrompt":
        content = create_reminder_message(action=target_behavior, 
                                          tone="neutral", channel=patient.preferred_channel)
        # E.g., "It's 8 AM – time to take your anticoagulant.", ensuring ease of action
    elif nudge_type == "MotivationalNudge":
        content = create_motivational_message(action=target_behavior, patient=patient,
                                              principles=nudge_plan["principles_applied"])
        # E.g., a message that uses social proof or incentives: 
        # "Taking your medication now keeps you on track! 95% of patients in your program did it today."
    return content

nudge_content = personalize_nudge_content(nudge_plan, patient)

# 6. Scheduling the Nudge (Just-In-Time Adaptive logic)
def schedule_nudge_delivery(patient, content, nudge_plan):
    # Determine optimal timing or trigger for this nudge
    if "Timely" in nudge_plan.get("principles_applied", []):
        # Use JITAI principles: check for context triggers
        if content.type == "reminder" and patient.last_dose_missed: 
            return "NOW"   # trigger immediately if a dose was missed
        # or schedule at next optimal context:
        return find_next_best_time(patient.schedule, patient.preferences)
    else:
        # default scheduling for non-time-sensitive content (e.g., education tip next morning)
        return schedule_at_preferred_slot(patient.preferences)
        
delivery_time = schedule_nudge_delivery(patient, nudge_content, nudge_plan)
# e.g., delivery_time =  "2025-10-20 08:00 CST" or an immediate trigger flag

# 7. Nudge Deployment
def send_nudge(patient, content, when):
    channel = patient.preferred_channel  # e.g., in-app chat, SMS, email
    messenger_identity = "AF Coach Bot"
    # Apply Messenger effect: optionally use a humanized or authoritative persona
    if content.requires_doctor_voice:
        messenger_identity = patient.doctor_name  # send message as if from their doctor
    dispatch_message(to=patient.contact_info, content=content.text, sender=messenger_identity, time=when)

send_nudge(patient, nudge_content, delivery_time)

# 8. Feedback Loop – Tracking and Learning
def record_feedback(patient, content):
    response = get_user_response(patient.id, content.id)  # e.g., did they click/acknowledge?
    outcome = evaluate_behavior_outcome(patient, target_behavior)  # e.g., check if they took the med
    log_interaction(patient.id, content.id, timestamp=now(), user_response=response, outcome=outcome)
    # Update patient profile or model based on outcome
    update_behavioral_profile(patient.id, outcome, content, response)

record_feedback(patient, nudge_content)
