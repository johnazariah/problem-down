---
source_pdf: ../arxiv_1803.07128.pdf
pages: 12
captions: 8
extracted_at: 2026-04-17T12:32:32+00:00
extractor: PyMuPDF (fitz)
---

# arxiv_1803.07128 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## FIG. 1.

Page: 2
Caption bbox: (54.0, 149.6, 299.2, 210.9)
Crop bbox: (67.4, 44.4, 286.0, 138.0)
Crop asset: ../figure-crops/arxiv_1803.07128/page_002_figure_01.png

Caption:

FIG. 1. While in the original space of training inputs, data
from the two classes ‘blue squares’ and ‘red circles’ are not
separable by a simple linear model (left), we can map them
to a higher dimensional feature space where a linear model is
indeed suﬃcient to deﬁne a separating hyperplane that acts
as a decision boundary (right).

## FIG. 2.

Page: 3
Caption bbox: (54.0, 117.7, 299.1, 137.1)
Crop bbox: (61.8, 49.8, 291.2, 111.9)
Crop asset: ../figure-crops/arxiv_1803.07128/page_003_figure_01.png

Caption:

FIG. 2. Relationships between the concepts of a feature map,
kernel and reproducing kernel Hilbert space.

## FIG. 3.

Page: 5
Caption bbox: (54.0, 225.1, 299.1, 296.8)
Crop bbox: (92.5, 48.0, 257.5, 218.2)
Crop asset: ../figure-crops/arxiv_1803.07128/page_005_figure_01.png

Caption:

FIG. 3. Illustration of the two approaches to use quantum fea-
ture maps for supervised learning. The implicit approach uses
the quantum device to evaluate the kernel function as part of
a hybrid or quantum-assisted model which can be trained by
classical methods. In the explicit approach, the model is solely
computed by the quantum device, which consists of a varia-
tional circuit trained by hybrid quantum-classical methods.

## FIG. 4.

Page: 5
Caption bbox: (317.0, 132.3, 562.1, 174.2)
Crop bbox: (317.2, 44.1, 545.7, 120.5)
Crop asset: ../figure-crops/arxiv_1803.07128/page_005_figure_02.png

Caption:

FIG. 4. Shape of the squeezing kernel function κsq(x, x′) from
Equation (7) for diﬀerent squeezing strength hyperparameters
c. The input x is ﬁxed at (0, 0) and x′ is varied. The plots
show the interval [−1, 1] on both horizontal axes.

## FIG. 5.

Page: 6
Caption bbox: (54.0, 222.9, 299.1, 346.9)
Crop bbox: (66.9, 54.4, 286.2, 217.1)
Crop asset: ../figure-crops/arxiv_1803.07128/page_006_figure_01.png

Caption:

FIG. 5. Decision boundary of a support vector machine with
the custom kernel from Eq. (7). The shaded areas show the
decision regions for Class 0 (blue) and Class 1 (red), and each
plot shows the rate of correct classiﬁcations on the training
set/test set. The ﬁrst row plots three standard 2-dimensional
datasets: ‘circles’, ‘moons’ and ‘blobs’, each with 150 test and
50 training samples. The second row illustrates that increas-
ing the squeezing hyperparameter c changes the classiﬁcation
performance. Here we use a dataset of 500 training and 100
test samples. Training was performed with python’s scikit-
learn SVC classiﬁer using a custom kernel which implements
the overlap of Eq. (8).

## FIG. 6.

Page: 6
Caption bbox: (317.0, 155.2, 562.1, 279.3)
Crop bbox: (330.1, 54.8, 549.2, 149.5)
Crop asset: ../figure-crops/arxiv_1803.07128/page_006_figure_02.png

Caption:

FIG. 6. Decision boundary of a perceptron classiﬁer in Fock
space after mapping the 2-dimensional data points via the
squeezing feature map with phase encoding from Eq.
(6)
(with c = 1.5). The perceptron only acts on the real sub-
space and without regularisation.
The ‘blobs’ dataset has
now only 70 training and 20 test samples. The perceptron
achieves a training accuracy of 1 after less than 5000 epochs,
which means that the data is linearly separable in Fock space.
Interestingly, in this example the test performance remains
exactly the same. The simulations were performed with the
Strawberry Fields simulator as well as a scikit-learn out-of-
the-box perceptron classiﬁer.

## FIG. 7.

Page: 7
Caption bbox: (317.0, 335.2, 562.2, 469.7)
Crop bbox: (345.5, 92.0, 538.4, 328.6)
Crop asset: ../figure-crops/arxiv_1803.07128/page_007_figure_01.png

Caption:

FIG. 7.
a.)
Representation of the Fock-space-classiﬁer in
the graphical language of quantum neural networks. A vector
(x1, x2)T from the input space X gets mapped into the feature
space F which is the inﬁnite-dimensional 2-mode Fock space
of the quantum system. The model circuit, including photon
detection measurement, implements a linear model in feature
space and reduces the “inﬁnite hidden layer” to two outputs.
b.) The model circuit of the explicit classiﬁer described in the
text uses only 2 modes to instantiate this inﬁnite-dimensional
hidden layer. The variational circuit W(θ) consists of repe-
titions of a gate block. We use the gate block shown in c.)
with the beamsplitter (BS), displacement (D), quadratic (P)
and cubic phase gates (C) described in the text.

## FIG. 8.

Page: 8
Caption bbox: (54.0, 149.0, 299.1, 231.2)
Crop bbox: (55.3, 44.3, 293.2, 142.6)
Crop asset: ../figure-crops/arxiv_1803.07128/page_008_figure_01.png

Caption:

FIG. 8. Fock space classiﬁer presented in Figure 7 and the
text for the ‘moons’ dataset. The shaded areas show the prob-
ability p(y = 1) of predicting class 1. The datasets consist of
150 training and 50 test samples, and has been trained for
5000 steps with stochastic gradient descent of batch-size 5,
an adaptive learning rate and a square-loss cost function with
a gentle l2 regularisation applied to all weights. The loss drops
predominantly in the ﬁrst 200 steps (left).
