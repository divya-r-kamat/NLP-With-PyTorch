# Goal
Understand Pytorch concepts:
- Tensors
- AutoGrad
- Tensors and Numpy
- Sharing Memory for Performance
- Tensor Indexing
- Squeezing and Unsqueezing and other Operations
- Writing a NN from scratch in Pytorch:
  - Working with dataset
  - Building a network
  - Accessing the weights
  - Forward Function
  - Training
  - Loss
  - Gradients
  - Weight Updates
  - Batch Training
  - Epochs
  
  
  # Objective
  Objective of this notebook is to update this [Sentiment analysis code](notebooks/2_Upgraded_Sentiment_Analysis.ipynb) in such a way that:

   - it has 3 LSTM layers
   - for loop is used to do so in the forward function
   - the dropout value used is 0.2
   - trained on the input text that is reversed 
   - achieves 87% or more accuracy
