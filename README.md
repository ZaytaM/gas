gas_pred.py was the first implementation of the prediction algorithim, using a simple feedfoward deep network
gas_rnn.py was the first implementation to use a RNN model
gas_rnn_deltaP.py was an attempt to predict the pressure differences between each timestep
gas_rnn_sqrP.py was the first attempt to predict pressure^2 for each timestep (P^2/P_initial was used due to model limitations)  
gas_rnn_stateful.py uses an alternative RNN structure, meant to use the ordering of the sequence to help make better predictions
gas_rnn_alter.py used data/gas_quinto_caso_alterado.txt during the predictions in order to minimize errors due to small time deltas present on the original dataset (data/gas_quinto_caso.txt)
gas_rnn_extend.py was the first to use gas_im, gas_sd and gas_si datasets for both training and prediction (this is to say all previous code was fed the first datasets received in april)
gas_rnn_extend_stateful.py uses the stateful model with the new datasets
gas_rnn_encoder.py and gas_rnn_encoder_1.py uses encoder decoder models

Tests where run with gas_rnn_alter and gas_rnn_extend, prediction plots and results where saved in plots/#.png and plots/#.txt
result.py reads the data from plots/#.txt and graphs the metrics associated to prediction and training (do notice only metrics for the #1000+ tests where saved)

0-25: 3 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, patience=30, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado
50-75: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, patience=30, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado
100-125: 10 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, patience=30, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado


1000-1025: 5 past datapoints, 0.0075 L2 regularizer, layer size = 16, layers = GRU + Linear, patience=30, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado
1050-1075: 5 past datapoints, 0.0025 L2 regularizer, layer size = 16, layers = GRU + Linear, patience=30, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado

1200-1225: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 200 epochs, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado
1225-1250: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 100 epochs, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado
1250-1275: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 500 epochs, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado
1275-1300: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 1000 epochs, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado

1400-1425: 0.01 gaussian noise, 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 1000 epochs, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado
1425-1450: sin(x * pi) * 5 noise, 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 1000 epochs, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado

1500-1510: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_terciero_caso_variavel and predicting gas_quinto_caso_alterado
1510-1520: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h + L points)
1520-1530: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h)
1530-1540: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_si_1 and predicting gas_sd_1 (144h)
1540-1550: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_si_1 and predicting gas_sd_1 (144h + L points)

2000-2030: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, [100,50,200] epochs, training with gas_primeiro_caso_variavel and predicting gas_quinto_caso_alterado
2000-2060: 5 past datapoints, 0.005 L2 regularizer, layer size = 16, layers = GRU + Linear, [100,50,200] epochs, training with gas_segundo_caso_variavel and predicting gas_quinto_caso_alterado

2100-2125: 5 past datapoints, tr=tr2=0, layer size=8, layers= Tanh x2 + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h)
2125-2150: 5 past datapoints, tr=tr2=0.1, layer size=8, layers= Tanh x2 + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h)
2150-2175: 5 past datapoints, tr=tr2=0.5, layer size=8, layers= Tanh x2 + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h)
2175-2200: 5 past datapoints, tr=tr2=0 , layer size=8, layers= Tanh x2 + Linear, 1000 epochs, 75/25 train/val split unrandomized, training with gas_im_1 and predicting gas_im_1 (144h)
2200-2225: 5 past datapoints, tr=tr2=0.5, layer size=8, layers= Tanh x2 + Linear, 100 patience, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h)


2300-2325: 2 past datapoints, tr=tr2=0.5 , layer size=16, layers= GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h)
2325-2350: 3 past datapoints, tr=tr2=0.5 , layer size=16, layers= GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h)
2350-2375: 5 past datapoints, tr=tr2=0.5 , layer size=16, layers= GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h)


2400-2410: 2 past datapoints, 0.005 L2 regularizer, tr=tr2=0.0 , layer size=16, layers= GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (96h)
2410-2420: 2 past datapoints, 0.005 L2 regularizer, tr=tr2=0.1 , layer size=16, layers= GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (96h)

2420-2430: 2 past datapoints, tr=tr2=0.0 , layer size=16, layers= GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (96h)
2430-2440: 2 past datapoints, tr=tr2=0.1 , layer size=16, layers= GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (96h)

2440-2450: 2 past datapoints, tr=tr2=0.0 , layer size=16, layers= GRU + Linear, 1000 epochs, 50/50 train/val split, training with gas_im_1 and predicting gas_im_1 (96h)
2450-2460: 2 past datapoints, tr=tr2=0.1 , layer size=16, layers= GRU + Linear, 1000 epochs, 50/50 train/val split, training with gas_im_1 and predicting gas_im_1 (96h)

2460-2470: 2 past datapoints, tr=tr2=0.0 , layer size=16, layers= GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (~100h)
2470-2480: 2 past datapoints, tr=tr2=0.1 , layer size=16, layers= GRU + Linear, 1000 epochs, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (~100h)

#sqrP=false, gauss noise = 0.01
3000-3010: batch size=64, 3 past datapoints, tr=tr2=0.0, 0.005 L2 regularizer, 3000 epochs, layer size=16, layers= GRU + Linear, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h)
3010-3020: batch size=64, 3 past datapoints, tr=tr2=0.0, 0.005 L2 regularizer, 3000 epochs, layer size=16, layers= GRU + Linear, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (72~120h)
3020-3030: batch size= inf, 3 past datapoints, tr=tr2=0.0, 0.005 L2 regularizer, 500 patience, layer size=16, layers= GRU + Linear, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1 (144h)
3030-3040: batch size=64, 3 past datapoints, tr=tr2=0.0, 0.005 L2 regularizer, 3000 epochs, layer size=16, layers= GRU + Linear, 80/20 train/val split, training with gas_im_1(24~120h) and predicting gas_im_1
3040-3050: batch size=64, 3 past datapoints, tr=tr2=0.0, 0.005 L2 regularizer, 3000 epochs, layer size=16, layers= GRU + Linear, 80/20 train/val split, training with gas_im_1 and predicting gas_im_1(96~120h)