#LSTM Model code
import numpy as np
import pandas as pd
from pandas.io import gbq
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt
 
# Replace this with your Google Cloud Project ID
project_id = 'mgmt590-396517'
# Replace this with your BigQuery table
dataset_table = 'mgmt590-396517.finalprojectarchivedata.sorted_consolidated_table'
 
# Fetch the data from BigQuery
query = f"""
SELECT date, Symbol, open, high, low, close, volume
FROM `{dataset_table}`
ORDER BY date
"""
df = gbq.read_gbq(query, project_id=project_id)
 
# Preprocess the data
df['date'] = pd.to_datetime(df['date']).dt.dayofyear.astype('float32')  # Convert to day of year and cast to float
df = pd.get_dummies(df, columns=['Symbol'], dtype='float32')  # Create dummy variables for 'Symbol' as float32
 
#  Feature Scaling
feature_scaler = MinMaxScaler(feature_range=(0, 1))
df[['open', 'high', 'low', 'volume']] = feature_scaler.fit_transform(df[['open', 'high', 'low', 'volume']].astype('float32'))
 
# Scale close price separately
close_scaler = MinMaxScaler(feature_range=(0, 1))
df['close'] = close_scaler.fit_transform(df['close'].values.reshape(-1,1).astype('float32'))
 
# Prepare the dataset for LSTM
def create_dataset(X, y, time_step=1):
    Xs, ys = [], []
    for i in range(len(X) - time_step):
        v = X.iloc[i:(i+time_step)].values
        Xs.append(v)
        ys.append(y[i + time_step])
    return np.array(Xs), np.array(ys)
 
time_step = 100
features = ['date', 'open', 'high', 'low', 'volume', 'Symbol_GOOG', 'Symbol_MSFT']  # Features including dummy variables
X = df[features]
y = df['close'].values  # Target variable
 
# Create the LSTM dataset
X_lstm, y_lstm = create_dataset(X, y, time_step)
X_train, X_test, y_train, y_test = train_test_split(X_lstm, y_lstm, test_size=0.2, random_state=0)
 
# Reshape input to be [samples, time steps, features] and cast to float32
X_train = X_train.reshape(X_train.shape[0], time_step, X_train.shape[2]).astype('float32')
X_test = X_test.reshape(X_test.shape[0], time_step, X_test.shape[2]).astype('float32')
 
# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(time_step, len(features))))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=25))
model.add(Dense(units=1))
 
# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')
 
# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)
 
# Predict and inverse transform the results
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)
# Inverse transform the predictions
train_predict = close_scaler.inverse_transform(train_predict)
test_predict = close_scaler.inverse_transform(test_predict)
 
# Plot the results
plt.figure(figsize=(12,6))
train_index = df.index[time_step:len(train_predict)+time_step]
test_index = df.index[len(train_predict)+(time_step*2):len(train_predict)+(time_step*2)+len(test_predict)]
 
# Inverse transform the original close price
actual_train = close_scaler.inverse_transform(y_train.reshape(-1,1))
actual_test = close_scaler.inverse_transform(y_test.reshape(-1,1))
 
plt.plot(train_index, actual_train, label='Train Data')
plt.plot(test_index, actual_test, label='Actual Close Price')
plt.plot(test_index, test_predict, label='Predictions')
 
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Stock Price Prediction with LSTM')
plt.legend()
plt.show()