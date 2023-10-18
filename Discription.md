# Storage-and-Validation-of-Certificate-using-cryptography
We are storing different certificates of a particular student by generating hash codes.
STORAGE AND VALIDATION OF CERTIFICATES USING CRYPTOGRAPHY
We are storing different certificates of a particular student by generating hash codes.

# INTRODUCTION
Cryptography is used to protect digital data. It is a division of computer science that focuses on transforming data into formats that cannot be recognized by unauthorized users.
Various Cryptographic methods are used to provide security to the certificates.
We can able to validate any copy of the certificates we stored and prove it as original one based on generation of hash code for the certificate we want to validate.
A hash is usually a hexadecimal string of several characters. Hashing is an algorithm that calculates a fixed-size bit string value from a file.

# REQUIREMENTS
SOFTWARE REQUIREMENTS                     HARDWARE REQUIREMENTS
Operating System: Windows 10              Processor: Intel Core i3
Programming Language: Python 3.7          Hard Disk: 4 GB
                                          RAM: 512 MB

# IMPLEMENTATION
Step1: 10th, Inter and B.tech certificates of particular student are uploaded.

Step2: Hash code is generated for each certificate stored.
Step3: Upload the Certificate that we want to verify
Step4: Hash code of uploaded certificate is compared with the hash codes of already stored certificates.
Step5:If hash codes matches - Uploaded certificate is validated as Original,
      If hash codes doesn't matches - Upload certificate is validated as fake.

# CONCLUSION & FUTURE SCOPE 
The generated unique ID is used to verify the certificates.
This system can be used by all the universities and colleges, in order to provide security to the certificates and the students' data.
The problem of fake certificates can be identified by validation.
This system can be implemented in applications which need certificate verification.
The proposed system validates the cetificates, it can be extended by adding an additional feature of protecting the stored certificates without giving any chance to edit.
