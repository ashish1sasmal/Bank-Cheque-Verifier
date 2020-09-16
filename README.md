# Bank-Cheque-Verifier

### A very simple bank cheque verifier using custom configuration for cheques of different banks.

#### How to use this ?
1. Select ROI (Region Of Interest) over the cheque fields which you want to check.
    ![alt text](https://github.com/ashish1sasmal/Bank-Cheque-Verifier/blob/master/Cheque_Verifier/Outputs/output1.png)  
2. Confirm ROIs.
3. Align Images using Feature Based alignment. (ORB detecter and RANSAC method)
4. Extract the ROIs from aligned image.
5. Perform OCR to recognize the text inside the ROIs.
6. Apply custom checks defined by client.
7. Done<br>
    ![alt text](https://github.com/ashish1sasmal/Bank-Cheque-Verifier/blob/master/Cheque_Verifier/Outputs/output2.png)  
