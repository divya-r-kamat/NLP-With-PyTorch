# Sequence to Sequence Learning with Neural Networks

The goal is to build a machine learning model to go from once sequence to another, using PyTorch and TorchText. 
This will be done on English to German translations, but the models can be applied to any problem that involves going from one sequence to another, such as summarization, i.e. going from a sequence to a shorter sequence in the same language.


## Model architecture
    Seq2Seq(
      (encoder): Encoder(
        (embedding): Embedding(5893, 256)
        (rnn): LSTM(256, 512, num_layers=3, dropout=0.5)
        (dropout): Dropout(p=0.5, inplace=False)
      )
      (decoder): Decoder(
        (embedding): Embedding(7855, 256)
        (rnn): LSTM(256, 512, num_layers=3, dropout=0.5)
        (fc_out): Linear(in_features=512, out_features=7855, bias=True)
        (dropout): Dropout(p=0.5, inplace=False)
      )
    )

## Training log

      Epoch: 01 | Time: 1m 14s
        Train Loss: 5.230 | Train PPL: 186.841
         Val. Loss: 5.129 |  Val. PPL: 168.800
      Epoch: 02 | Time: 1m 14s
        Train Loss: 4.684 | Train PPL: 108.254
         Val. Loss: 4.812 |  Val. PPL: 122.956
      Epoch: 03 | Time: 1m 14s
        Train Loss: 4.334 | Train PPL:  76.272
         Val. Loss: 4.656 |  Val. PPL: 105.188
      Epoch: 04 | Time: 1m 14s
        Train Loss: 4.088 | Train PPL:  59.623
         Val. Loss: 4.511 |  Val. PPL:  91.003
      Epoch: 05 | Time: 1m 14s
        Train Loss: 3.913 | Train PPL:  50.060
         Val. Loss: 4.452 |  Val. PPL:  85.785
      Epoch: 06 | Time: 1m 15s
        Train Loss: 3.780 | Train PPL:  43.828
         Val. Loss: 4.339 |  Val. PPL:  76.629
      Epoch: 07 | Time: 1m 14s
        Train Loss: 3.661 | Train PPL:  38.881
         Val. Loss: 4.222 |  Val. PPL:  68.140
      Epoch: 08 | Time: 1m 14s
        Train Loss: 3.522 | Train PPL:  33.848
         Val. Loss: 4.148 |  Val. PPL:  63.321
      Epoch: 09 | Time: 1m 14s
        Train Loss: 3.408 | Train PPL:  30.210
         Val. Loss: 4.040 |  Val. PPL:  56.809
      Epoch: 10 | Time: 1m 14s
        Train Loss: 3.297 | Train PPL:  27.028
         Val. Loss: 3.973 |  Val. PPL:  53.164
