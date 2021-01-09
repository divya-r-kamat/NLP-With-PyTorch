# The Stanford Question Answering Dataset (SQuAD)

Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

SQuAD2.0 combines the 100,000 questions in SQuAD1.1 with over 50,000 unanswerable questions written adversarially by crowdworkers to look similar to answerable ones. To do well on SQuAD2.0, systems must not only answer questions when possible, but also determine when no answer is supported by the paragraph and abstain from answering.


# [Model1](SQuAD_Dataset_Learning_Phrase_Representation_RNN_Encoder_Decoder.ipynb)

Model Architecture

    Seq2Seq(
      (encoder): Encoder(
        (embedding): Embedding(18975, 256)
        (rnn): GRU(256, 512)
        (dropout): Dropout(p=0.5, inplace=False)
      )
      (decoder): Decoder(
        (embedding): Embedding(16465, 256)
        (rnn): GRU(768, 512)
        (fc_out): Linear(in_features=1280, out_features=16465, bias=True)
        (dropout): Dropout(p=0.5, inplace=False)
      )
    )

Training Log

    Epoch: 01 | Time: 3m 29s
      Train Loss: 6.215 | Train PPL: 500.413
       Val. Loss: 5.774 |  Val. PPL: 321.878
    Epoch: 02 | Time: 3m 32s
      Train Loss: 5.764 | Train PPL: 318.576
       Val. Loss: 5.538 |  Val. PPL: 254.253
    Epoch: 03 | Time: 3m 30s
      Train Loss: 5.375 | Train PPL: 215.936
       Val. Loss: 5.387 |  Val. PPL: 218.603
    Epoch: 04 | Time: 3m 30s
      Train Loss: 5.036 | Train PPL: 153.786
       Val. Loss: 5.306 |  Val. PPL: 201.499
    Epoch: 05 | Time: 3m 27s
      Train Loss: 4.661 | Train PPL: 105.735
       Val. Loss: 5.355 |  Val. PPL: 211.761
    Epoch: 06 | Time: 3m 29s
      Train Loss: 4.272 | Train PPL:  71.671
       Val. Loss: 5.474 |  Val. PPL: 238.498
    Epoch: 07 | Time: 3m 30s
      Train Loss: 3.813 | Train PPL:  45.268
       Val. Loss: 5.700 |  Val. PPL: 298.801
    Epoch: 08 | Time: 3m 31s
      Train Loss: 3.307 | Train PPL:  27.314
       Val. Loss: 5.952 |  Val. PPL: 384.513
    Epoch: 09 | Time: 3m 30s
      Train Loss: 2.837 | Train PPL:  17.061
       Val. Loss: 6.188 |  Val. PPL: 486.727
    Epoch: 10 | Time: 3m 29s
      Train Loss: 2.474 | Train PPL:  11.867
       Val. Loss: 6.360 |  Val. PPL: 578.040
       
Test Loss

    | Test Loss: 5.376 | Test PPL: 216.088 |
    
    
# [Model2](SQuAD_Dataset_Sequence_to_Sequence_using_Attention.ipynb)

Model Architecture

	Seq2Seq(
	  (encoder): Encoder(
	    (embedding): Embedding(18975, 256)
	    (rnn): GRU(256, 512, bidirectional=True)
	    (fc): Linear(in_features=1024, out_features=512, bias=True)
	    (dropout): Dropout(p=0.5, inplace=False)
	  )
	  (decoder): Decoder(
	    (attention): Attention(
	      (attn): Linear(in_features=1536, out_features=512, bias=True)
	      (v): Linear(in_features=512, out_features=1, bias=False)
	    )
	    (embedding): Embedding(16465, 256)
	    (rnn): GRU(1280, 512)
	    (fc_out): Linear(in_features=1792, out_features=16465, bias=True)
	    (dropout): Dropout(p=0.5, inplace=False)
	  )
	)

Training Loss

	Epoch: 01 | Time: 5m 16s
		Train Loss: 6.034 | Train PPL: 417.228
		 Val. Loss: 5.432 |  Val. PPL: 228.551
	Epoch: 02 | Time: 5m 20s
		Train Loss: 5.361 | Train PPL: 213.028
		 Val. Loss: 5.271 |  Val. PPL: 194.559
	Epoch: 03 | Time: 5m 20s
		Train Loss: 4.899 | Train PPL: 134.173
		 Val. Loss: 5.229 |  Val. PPL: 186.588
	Epoch: 04 | Time: 5m 22s
		Train Loss: 4.367 | Train PPL:  78.783
		 Val. Loss: 5.316 |  Val. PPL: 203.629
	Epoch: 05 | Time: 5m 18s
		Train Loss: 3.663 | Train PPL:  38.975
		 Val. Loss: 5.600 |  Val. PPL: 270.294
	Epoch: 06 | Time: 5m 21s
		Train Loss: 2.975 | Train PPL:  19.581
		 Val. Loss: 5.905 |  Val. PPL: 366.940
	Epoch: 07 | Time: 5m 20s
		Train Loss: 2.478 | Train PPL:  11.913
		 Val. Loss: 6.214 |  Val. PPL: 499.738
	Epoch: 08 | Time: 5m 21s
		Train Loss: 2.148 | Train PPL:   8.564
		 Val. Loss: 6.416 |  Val. PPL: 611.733
	Epoch: 09 | Time: 5m 20s
		Train Loss: 1.882 | Train PPL:   6.566
		 Val. Loss: 6.644 |  Val. PPL: 767.949
	Epoch: 10 | Time: 5m 19s
		Train Loss: 1.674 | Train PPL:   5.333
		 Val. Loss: 6.792 |  Val. PPL: 890.963
     
Test Loss

	| Test Loss: 5.358 | Test PPL: 212.325 |
