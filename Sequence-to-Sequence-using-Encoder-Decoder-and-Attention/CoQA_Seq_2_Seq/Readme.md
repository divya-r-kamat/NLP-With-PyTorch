# CoQA - A Conversational Question Answering Challenge

CoQA is a large-scale dataset for building Conversational Question Answering systems. The goal of the CoQA challenge is to measure the ability of machines to understand a text passage and answer a series of interconnected questions that appear in a conversation. CoQA is pronounced as coca

CoQA contains 127,000+ questions with answers collected from 8000+ conversations. Each conversation is collected by pairing two crowdworkers to chat about a passage in the form of questions and answers. The unique features of CoQA include 1) the questions are conversational; 2) the answers can be free-form text; 3) each answer also comes with an evidence subsequence highlighted in the passage; and 4) the passages are collected from seven diverse domains. CoQA has a lot of challenging phenomena not present in existing reading comprehension datasets, e.g., coreference and pragmatic reasoning.

## License
CoQA contains passages from seven domains. We make five of these public under the following licenses:
- Literature and Wikipedia passages are shared under CC BY-SA 4.0 license.
- Children's stories are collected from MCTest which comes with MSR-LA license.
- Middle/High school exam passages are collected from RACE which comes with its own license.
- News passages are collected from the DeepMind CNN dataset which comes with Apache license.


# [Model1](CoQA_Dataset_Learning_Phrase_Representation_RNN_Encoder_Decoder.ipynb)

Model Architecture

    Seq2Seq(
      (encoder): Encoder(
        (embedding): Embedding(2197, 256)
        (rnn): GRU(256, 512)
        (dropout): Dropout(p=0.5, inplace=False)
      )
      (decoder): Decoder(
        (embedding): Embedding(1504, 256)
        (rnn): GRU(768, 512)
        (fc_out): Linear(in_features=1280, out_features=1504, bias=True)
        (dropout): Dropout(p=0.5, inplace=False)
      )
    )

Training Log

      Epoch: 01 | Time: 6m 54s
        Train Loss: 6.398 | Train PPL: 600.719
         Val. Loss: 6.090 |  Val. PPL: 441.201
      Epoch: 02 | Time: 6m 57s
        Train Loss: 5.788 | Train PPL: 326.394
         Val. Loss: 5.667 |  Val. PPL: 289.266
      Epoch: 03 | Time: 6m 57s
        Train Loss: 5.283 | Train PPL: 196.863
         Val. Loss: 5.551 |  Val. PPL: 257.382
      Epoch: 04 | Time: 7m 0s
        Train Loss: 4.755 | Train PPL: 116.183
         Val. Loss: 5.443 |  Val. PPL: 231.222
      Epoch: 05 | Time: 7m 1s
        Train Loss: 4.168 | Train PPL:  64.585
         Val. Loss: 5.494 |  Val. PPL: 243.221
      Epoch: 06 | Time: 7m 2s
        Train Loss: 3.569 | Train PPL:  35.464
         Val. Loss: 5.630 |  Val. PPL: 278.695
      Epoch: 07 | Time: 6m 59s
        Train Loss: 3.052 | Train PPL:  21.153
         Val. Loss: 5.768 |  Val. PPL: 319.973
      Epoch: 08 | Time: 7m 0s
        Train Loss: 2.656 | Train PPL:  14.239
         Val. Loss: 5.875 |  Val. PPL: 356.088
      Epoch: 09 | Time: 6m 59s
        Train Loss: 2.362 | Train PPL:  10.615
         Val. Loss: 5.989 |  Val. PPL: 398.850
      Epoch: 10 | Time: 7m 2s
        Train Loss: 2.139 | Train PPL:   8.489
         Val. Loss: 6.135 |  Val. PPL: 461.923

Test Loss

     | Test Loss: 5.729 | Test PPL: 307.551 |
       
    
# [Model2](CoQA_Dataset_Sequence_to_Sequence_using_Attention.ipynb)

Model Architecture

    Seq2Seq(
      (encoder): Encoder(
        (embedding): Embedding(2197, 256)
        (rnn): GRU(256, 512, bidirectional=True)
        (fc): Linear(in_features=1024, out_features=512, bias=True)
        (dropout): Dropout(p=0.5, inplace=False)
      )
      (decoder): Decoder(
        (attention): Attention(
          (attn): Linear(in_features=1536, out_features=512, bias=True)
          (v): Linear(in_features=512, out_features=1, bias=False)
        )
        (embedding): Embedding(1504, 256)
        (rnn): GRU(1280, 512)
        (fc_out): Linear(in_features=1792, out_features=1504, bias=True)
        (dropout): Dropout(p=0.5, inplace=False)
      )
    )

Training Log

    Epoch: 01 | Time: 10m 6s
      Train Loss: 6.186 | Train PPL: 486.004
       Val. Loss: 5.626 |  Val. PPL: 277.518
    Epoch: 02 | Time: 10m 6s
      Train Loss: 5.367 | Train PPL: 214.246
       Val. Loss: 5.341 |  Val. PPL: 208.736
    Epoch: 03 | Time: 10m 9s
      Train Loss: 4.675 | Train PPL: 107.207
       Val. Loss: 5.264 |  Val. PPL: 193.284
    Epoch: 04 | Time: 10m 10s
      Train Loss: 3.839 | Train PPL:  46.499
       Val. Loss: 5.287 |  Val. PPL: 197.722
    Epoch: 05 | Time: 10m 15s
      Train Loss: 3.097 | Train PPL:  22.135
       Val. Loss: 5.421 |  Val. PPL: 226.052
    Epoch: 06 | Time: 10m 15s
      Train Loss: 2.562 | Train PPL:  12.957
       Val. Loss: 5.607 |  Val. PPL: 272.382
    Epoch: 07 | Time: 10m 12s
      Train Loss: 2.215 | Train PPL:   9.165
       Val. Loss: 5.761 |  Val. PPL: 317.798
    Epoch: 08 | Time: 10m 12s
      Train Loss: 1.958 | Train PPL:   7.085
       Val. Loss: 5.919 |  Val. PPL: 371.877
    Epoch: 09 | Time: 10m 10s
      Train Loss: 1.767 | Train PPL:   5.855
       Val. Loss: 6.068 |  Val. PPL: 431.622
    Epoch: 10 | Time: 10m 15s
      Train Loss: 1.611 | Train PPL:   5.008
       Val. Loss: 6.198 |  Val. PPL: 491.986
       
Test Loss
   
    | Test Loss: 5.687 | Test PPL: 294.983 |

