def infer_disease(has_cough, has_fever):
    """A super simplified Bayesian-like inference for two diseases."""

    # Prior probabilities (our initial beliefs)
    prior_flu = 0.05
    prior_cold = 0.2

    # Likelihoods (probability of symptoms given the disease)
    likelihood_cough_given_flu = 0.8
    likelihood_fever_given_flu = 0.9
    likelihood_cough_given_cold = 0.9
    likelihood_fever_given_cold = 0.3

    # Evidence (the observed symptoms)
    p_cough = likelihood_cough_given_flu * prior_flu + likelihood_cough_given_cold * prior_cold
    p_fever = likelihood_fever_given_flu * prior_flu + likelihood_fever_given_cold * prior_cold

    # Probability of evidence (simplified - assuming independence for now)
    p_evidence = 1.0
    if has_cough:
        p_evidence *= p_cough
    else:
        p_evidence *= (1 - p_cough)
    if has_fever:
        p_evidence *= p_fever
    else:
        p_evidence *= (1 - p_fever)

    # Posterior probabilities (updated beliefs given the evidence)
    # Using a simplified form of Bayes' Rule: P(Disease|Symptoms) proportional to P(Symptoms|Disease) * P(Disease)

    prob_flu_given_symptoms_numerator = prior_flu
    if has_cough:
        prob_flu_given_symptoms_numerator *= likelihood_cough_given_flu
    else:
        prob_flu_given_symptoms_numerator *= (1 - likelihood_cough_given_flu)
    if has_fever:
        prob_flu_given_symptoms_numerator *= likelihood_fever_given_flu
    else:
        prob_flu_given_symptoms_numerator *= (1 - likelihood_fever_given_flu)

    prob_cold_given_symptoms_numerator = prior_cold
    if has_cough:
        prob_cold_given_symptoms_numerator *= likelihood_cough_given_cold
    else:
        prob_cold_given_symptoms_numerator *= (1 - likelihood_cough_given_cold)
    if has_fever:
        prob_cold_given_symptoms_numerator *= likelihood_fever_given_cold
    else:
        prob_cold_given_symptoms_numerator *= (1 - likelihood_fever_given_cold)

    # Normalize to get probabilities
    if prob_flu_given_symptoms_numerator + prob_cold_given_symptoms_numerator == 0:
        prob_flu_given_symptoms = 0
        prob_cold_given_symptoms = 0
    else:
        total_prob = prob_flu_given_symptoms_numerator + prob_cold_given_symptoms_numerator
        prob_flu_given_symptoms = prob_flu_given_symptoms_numerator / total_prob
        prob_cold_given_symptoms = prob_cold_given_symptoms_numerator / total_prob

    return {"Flu": prob_flu_given_symptoms, "Common Cold": prob_cold_given_symptoms}
if __name__ == "__main__":
    symptoms1 = infer_disease(has_cough=True, has_fever=True)
    print(f"Symptoms: Cough=True, Fever=True, Probabilities: {symptoms1}")

    symptoms2 = infer_disease(has_cough=True, has_fever=False)
    print(f"Symptoms: Cough=True, Fever=False, Probabilities: {symptoms2}")

    symptoms3 = infer_disease(has_cough=False, has_fever=True)
    print(f"Symptoms: Cough=False, Fever=True, Probabilities: {symptoms3}")

    symptoms4 = infer_disease(has_cough=False, has_fever=False)
    print(f"Symptoms: Cough=False, Fever=False, Probabilities: {symptoms4}")