---
source_pdf: ../doi_10.1038_s41467-021-22539-9.pdf
pages: 9
captions: 4
extracted_at: 2026-04-17T12:32:47+00:00
extractor: PyMuPDF (fitz)
title: "Power of data in quantum machine learning"
author: "Hsin-Yuan Huang"
---

# doi_10.1038_s41467-021-22539-9 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## Fig. 1

Page: 3
Caption bbox: (43.6, 615.7, 551.7, 740.0)
Crop bbox: (35.6, 21.7, 559.7, 611.7)
Crop asset: ../figure-crops/doi_10.1038_s41467-021-22539-9/page_003_figure_01.png

Caption:

Fig. 1 Illustration of the relation between complexity classes and a ﬂowchart for understanding and prescreening potential quantum advantage. a We
cartoon the separation between problem complexities that are created by the addition of data to a problem. Classical algorithms that can learn from data
deﬁne a complexity class that can solve problems beyond classical computation (BPP), but it is still expected that quantum computation can efﬁciently
solve problems that classical ML algorithms with data cannot. A rigorous deﬁnition and proof for the separation between classical algorithms that can learn
from data and BPP/BQP is given in Supplementary Section 2. b The ﬂowchart we develop for understanding the potential for quantum prediction
advantage. N samples of data from a potentially inﬁnite depth QNN made with encoding and function circuits Uenc and UQNN are provided as input along
with quantum and classical methods with associated kernels. Tests are given as functions of N to emphasize the role of data in the possibility of a
prediction advantage. One can ﬁrst evaluate a geometric quantity gCQ that measures the possibility of an advantageous quantum/classical prediction
separation without yet considering the actual function to learn. We show how one can efﬁciently construct an adversarial function that saturates this limit if
the test is passed, otherwise the classical approach is guaranteed to match performance for any function of the data. To subsequently consider the actual
function provided, a label/function-speciﬁc test may be run using the model complexities sC and sQ. If one speciﬁcally uses the quantum kernel (QK)
method, the red dashed arrows can evaluate if all possible choices of UQNN lead to an easy classical function for the chosen encoding of the data.

## Fig. 2

Page: 5
Caption bbox: (43.6, 317.1, 551.7, 345.9)
Crop bbox: (35.6, 21.7, 559.7, 313.1)
Crop asset: ../figure-crops/doi_10.1038_s41467-021-22539-9/page_005_figure_01.png

Caption:

Fig. 2 Cartoon of the geometry (kernel function) deﬁned by classical and quantum ML models. The letters A, B, ... represent data points {xi} in different
spaces with arrows representing the similarity measure (kernel function) between data. The geometric difference g is a difference between similarity
measures (arrows) in different ML models and d is an effective dimension of the dataset in the quantum Hilbert space.

## Fig. 3

Page: 7
Caption bbox: (43.6, 243.2, 551.7, 324.3)
Crop bbox: (35.6, 21.7, 559.7, 239.2)
Crop asset: ../figure-crops/doi_10.1038_s41467-021-22539-9/page_007_figure_01.png

Caption:

Fig. 3 Relation between dimension d, geometric difference g, and prediction performance. The shaded regions are the standard deviation over 10
independent runs and n is the number of qubits in the quantum encoding and dimension of the input for the classical encoding. a The approximate
dimension d and the geometric difference g with classical ML models for quantum kernel (Q) and projected quantum kernel (PQ) under different
embeddings and system sizes n. b Prediction error (lower is better) of the quantum kernel method (Q), projected quantum kernel method (PQ), and
classical ML models on classical (C) and quantum (Q) datasets with number of data N = 600. As d grows too large, the geometric difference g for
quantum kernel becomes small. We see that small geometric difference g always results in classical ML being competitive or outperforming the quantum
ML model. When g is large, there is a potential for improvement over classical ML. For example, projected quantum kernel improves upon the best classical
ML in Dataset (Q, E3).

## Fig. 4

Page: 7
Caption bbox: (43.6, 514.6, 551.7, 564.4)
Crop bbox: (35.6, 21.7, 559.7, 510.6)
Crop asset: ../figure-crops/doi_10.1038_s41467-021-22539-9/page_007_figure_02.png

Caption:

Fig. 4 Prediction accuracy (higher the better) on engineered datasets. A label function is engineered to match the geometric difference g(C∣∣PQ)
between projected quantum kernel and classical approaches, demonstrating a signiﬁcant gap between quantum and the best classical models up to 30
qubits when g is large. We consider the best performing classical ML models among Gaussian SVM, linear SVM, Adaboost, random forest, neural
networks, and gradient boosting. We only report the accuracy of the quantum kernel method up to system size n = 28 due to the high simulation cost and
the inferior performance.
