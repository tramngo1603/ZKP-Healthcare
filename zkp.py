import sys
import random
from typing import List
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel, QLineEdit

# Pedersen commitment parameters
p = 283
g = 3
h = 7

def commit(value, blinding_factor):
    commitment = (pow(g, value, p) * pow(h, blinding_factor, p)) % p
    return commitment

def generate_response(blinding_factor, challenge):
    return blinding_factor

def verify_response(value, response, challenge, lower_threshold, upper_threshold):
    if lower_threshold <= value <= upper_threshold:
        return True
    else:
        return False

def verify_eligibility(conditions: List[bool]):
    return all(conditions)

age = 35
diastolic_bp = 85
systolic_bp = 130

blinding_factor_age = random.randint(1, 1000)
blinding_factor_dbp = random.randint(1, 1000)
blinding_factor_sbp = random.randint(1, 1000)
commitment_age = commit(age, blinding_factor_age)
commitment_dbp = commit(diastolic_bp, blinding_factor_dbp)
commitment_sbp = commit(systolic_bp, blinding_factor_sbp)
challenge = random.randint(1, 1000)
response_age = generate_response(blinding_factor_age, challenge)
response_dbp = generate_response(blinding_factor_dbp, challenge)
response_sbp = generate_response(blinding_factor_sbp, challenge)

def execute_zkp(text_edit, age_threshold, dbp_lower, dbp_upper, sbp_lower, sbp_upper):
    age_verified = verify_response(age, response_age, challenge, age_threshold, float('inf'))
    dbp_verified = verify_response(diastolic_bp, response_dbp, challenge, dbp_lower, dbp_upper)
    sbp_verified = verify_response(systolic_bp, response_sbp, challenge, sbp_lower, sbp_upper)
    eligibility_verified = verify_eligibility([age_verified, dbp_verified, sbp_verified])
    
    if age_verified:
        age_verified = f"True. Patient is above provided age threshold"
    if dbp_verified:
        dbp_verified = f"True. Patient has BP values within the provided DBP threshold"
    if sbp_verified:
        sbp_verified = f"True. Patient has BP values within the provided SBP threshold"
    
    # Display results
    results = f"Age verification: {age_verified}\n"
    results += f"Diastolic BP verification: {dbp_verified}\n"
    results += f"Systolic BP verification: {sbp_verified}\n"
    results += f"Eligibility verification: {eligibility_verified}"
    text_edit.setText(results)

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('ZKP Demo')

    layout = QVBoxLayout()
    
    # Age threshold input
    age_threshold_label = QLabel('Age Threshold:')
    age_threshold_input = QLineEdit()
    layout.addWidget(age_threshold_label)
    layout.addWidget(age_threshold_input)
    
    # Diastolic BP range inputs
    dbp_lower_label = QLabel('Diastolic BP Lower Bound:')
    dbp_lower_input = QLineEdit()
    layout.addWidget(dbp_lower_label)
    layout.addWidget(dbp_lower_input)
    
    dbp_upper_label = QLabel('Diastolic BP Upper Bound:')
    dbp_upper_input = QLineEdit()
    layout.addWidget(dbp_upper_label)
    layout.addWidget(dbp_upper_input)
    
    # Systolic BP range inputs
    sbp_lower_label = QLabel('Systolic BP Lower Bound:')
    sbp_lower_input = QLineEdit()
    layout.addWidget(sbp_lower_label)
    layout.addWidget(sbp_lower_input)
    
    sbp_upper_label = QLabel('Systolic BP Upper Bound:')
    sbp_upper_input = QLineEdit()
    layout.addWidget(sbp_upper_label)
    layout.addWidget(sbp_upper_input)
    
    button = QPushButton('Run ZKP Verification')
    text_edit = QTextEdit()  # Text area for displaying results
    text_edit.setReadOnly(True)

    def run_zkp():
        age_threshold = int(age_threshold_input.text())
        dbp_lower = int(dbp_lower_input.text())
        dbp_upper = int(dbp_upper_input.text())
        sbp_lower = int(sbp_lower_input.text())
        sbp_upper = int(sbp_upper_input.text())
        execute_zkp(text_edit, age_threshold, dbp_lower, dbp_upper, sbp_lower, sbp_upper)

    button.clicked.connect(run_zkp)  # Connect button to function
    layout.addWidget(button)
    layout.addWidget(text_edit)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()