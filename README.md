# Zero-Knowledge Proofs for PHI Data Verification

This repository contains a Python script and a research paper that explore the application of Zero-Knowledge Proofs (ZKPs) for verifying Protected Health Information (PHI) data while preserving patient privacy.

## Contents

- `zkp_demo.py`: A Python script that demonstrates a proof-of-concept implementation of ZKPs for verifying age and blood pressure values against specified thresholds without revealing the actual values.
- `Paper.pdf`: A research paper titled "Enabling Secure and Privacy-Preserving Verification of PHI Data with Zero-Knowledge Proofs" that delves into the technical foundations, practical applications, and future directions of ZKPs in the healthcare domain.

## Prerequisites

To run the Python script, we need the following dependencies installed:

- Python 3.x
- PyQt5

  
## Usage

To run the ZKP demo script, execute the following command:

```
python zkp_demo.py
```

This will launch a graphical user interface (GUI) where you can input the desired thresholds for age and blood pressure verification. Click the "Run ZKP Verification" button to initiate the verification process. The script will display the verification results without revealing the actual values of the prover's age and blood pressure.

## Research Paper

The paper was written as the final project for the Cryptology class during my Master's Degree. It provides an exploration of ZKPs and their potential applications in the healthcare domain. 

It covers the following topics:

1. Introduction and background on ZKPs and PHI data privacy
2. Technical foundations of ZKPs, including cryptographic primitives and concepts
3. Problem formulation for applying ZKPs to PHI data verification
4. Implementation considerations and potential solutions
5. Case studies and real-world applications of ZKPs in healthcare
6. Future directions for research and development

Please refer to the `Paper.pdf` file for the complete paper.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

I would like to acknowledge the contributions of the research community in advancing the field of Zero-Knowledge Proofs and their applications in healthcare data privacy. Without such existing contributions, I wouldn't have been able to extend my knowledge in the field.

## Contact

For any questions or inquiries, please contact me via tramngo1603@gmail.com.
