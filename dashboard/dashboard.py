import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set_style('darkgrid')

# Setting up DataFrames
def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='D', on='order_date').agg({
        'order_id': 'nunique',
        'total_price': 'sum'
    })
    daily_orders_df = daily_orders_df.reset_index()
    daily_orders_df.rename(columns={
        'order_id': 'order_count',
        'total_price': 'revenue'
    }, inplace=True)
    
    return daily_orders_df

def create_sum_order_items_df(df):
    sum_order_items_df = df.groupby('product_name').quantity_x.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_df

def create_bygender_df(df):
    bygender_df = df.groupby(by='gender').customer_id.nunique().reset_index()
    bygender_df.rename(columns={
        'customer_id': 'customer_count'
    }, inplace=True)
    
    return bygender_df

def create_byage_df(df):
    byage_df = df.groupby(by='age_group').customer_id.nunique().reset_index()
    byage_df.rename(columns={
        'customer_id': 'customer_count'
    }, inplace=True)
    
    return byage_df

def create_bystate_df(df):
    bystate_df = df.groupby(by='state').customer_id.nunique().reset_index()
    bystate_df.rename(columns={
        'customer_id': 'customer_count'
    }, inplace=True)
    
    return bystate_df

def create_rfm_df(df):
    rfm_df = df.groupby(by='customer_id', as_index=False).agg({
        'order_date': 'max',
        'order_id': 'nunique',
        'total_price': 'sum'
    })
    rfm_df.columns = ['customer_id', 'max_order_timestamp', 'frequency', 'monetary']
    
    rfm_df['max_order_timestamp'] = rfm_df['max_order_timestamp'].dt.date
    recent_date = df['order_date'].dt.date.max()
    rfm_df['recency'] = rfm_df['max_order_timestamp'].apply(lambda x: (recent_date - x).days)
    rfm_df.drop('max_order_timestamp', axis=1, inplace=True)
    
    return rfm_df

all_df = pd.read_csv('https://raw.githubusercontent.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/main/dashboard/all_data.csv')

datetime_columns = ['order_date', 'delivery_date']
all_df.sort_values(by='order_date', inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])


# Create Filter Components by Date
min_date = all_df['order_date'].min()
max_date = all_df['order_date'].max()

with st.sidebar:
    st.image('https://github.com/dicodingacademy/assets/raw/main/logo.png')

    start_date, end_date = st.date_input(
        label='Rentang waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[
    (all_df['order_date'] >= str(start_date)) &
    (all_df['order_date'] <= str(end_date))
]

# Calling Helper Function
daily_orders_df = create_daily_orders_df(main_df)
sum_order_items_df = create_sum_order_items_df(main_df)
bygender_df = create_bygender_df(main_df)
byage_df = create_byage_df(main_df)
bystate_df = create_bystate_df(main_df)
rfm_df = create_rfm_df(main_df)

# Complementing the Dashboard with Data Visualization
st.header(':sparkles: Dicoding Collection Dashboard :sparkles:')

st.subheader('Daily Orders')

col1, col2 = st.columns(2)

# Displays the order total
with col1:
    total_orders = daily_orders_df.order_count.sum()
    st.metric('#Total Orders', value=total_orders)

# Displays the revenue total
with col2:
    total_revenue = format_currency(daily_orders_df.revenue.sum(), 'AUD', locale='es_CO')
    st.metric('#Total Revenue', value=total_revenue)

# Displays the number of daily orders
if min_date <= daily_orders_df['order_date'].max() - pd.DateOffset(days=60):
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        daily_orders_df['order_date'],
        daily_orders_df['order_count'],
        marker='o',
        linewidth=2,
        color='#90CAF9'
    )
    ax.tick_params(axis='y', labelsize=18)
    ax.tick_params(axis='x', labelsize=15)

    st.pyplot(fig)
else:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        daily_orders_df['order_date'],
        daily_orders_df['order_count'],
        marker='o',
        linewidth=2,
        color='#90CAF9'
    )
    ax.tick_params(axis='y', labelsize=18)
    ax.tick_params(axis='x', labelsize=15)

    for i in range(len(daily_orders_df)):
        plt.text(
            daily_orders_df['order_date'][i],
            daily_orders_df['order_count'][i] + 0.1,
            daily_orders_df['order_count'][i],
            ha='left',
            va='bottom',
            fontsize=8
        )

    st.pyplot(fig)

# Displays the sales performance of each product
st.subheader('Best & Worst Performing Products')

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(28, 8))

colors = ['#90CAF9', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3']

# First plot
sns.barplot(
    x='quantity_x',
    y='product_name',
    data=sum_order_items_df.head(5),
    palette=colors,
    ax=ax[0]
)
ax[0].set_ylabel(None)
ax[0].set_xlabel('Number of Sales', fontsize=28, labelpad=15)
ax[0].set_title('Best Performing Product', loc='center', fontsize=34, pad=20)
ax[0].tick_params(axis='y', labelsize=30)
ax[0].tick_params(axis='x', labelsize=26)

for i in range(len(sum_order_items_df.head(5))):
    ax[0].text(
        sum_order_items_df['quantity_x'].iloc[i],
        i,
        sum_order_items_df['quantity_x'].iloc[i], 
        va='center',
        fontsize=20
    )

# Second plot
asc_sum_order = sum_order_items_df.sort_values(
    by='quantity_x', ascending=True
).head(5)

sns.barplot(
    x='quantity_x',
    y='product_name',
    data=asc_sum_order,
    palette=colors,
    ax=ax[1]
)
ax[1].set_ylabel(None)
ax[1].set_xlabel('Number of Sales', fontsize=28, labelpad=15)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position('right')
ax[1].yaxis.tick_right()
ax[1].set_title('Worst Performing Product', loc='center', fontsize=34, pad=20)
ax[1].tick_params(axis='y', labelsize=30)
ax[1].tick_params(axis='x', labelsize=26)

for i, value in enumerate(asc_sum_order['quantity_x']):
    ax[1].text(
        value,
        i,
        value,
        va='center',
        ha='right',
        fontsize=20
    )

st.pyplot(fig)

# Displays customer demographics
st.subheader('Customer Demographics')

col1, col2 = st.columns(2)

# By Gender
with col1:
    desc_bygender_df = bygender_df.sort_values(by='customer_count', ascending=False)
    
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        data=desc_bygender_df,
        y='customer_count', 
        x='gender',
        palette=colors,
        ax=ax
    )
    
    ax.set_title('Number of Customer by Gender', loc='center', fontsize=40, pad=20)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=38)
    ax.tick_params(axis='y', labelsize=32)
    
    for i, value in enumerate(desc_bygender_df['customer_count']):
        ax.text(
            i,
            value,
            value,
            ha='center',
            fontsize=26
        )
    st.pyplot(fig)

# By Age
with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    colors_ = ['#D3D3D3', '#90CAF9', '#D3D3D3']
    
    bar = sns.barplot(
        data=byage_df,
        y='customer_count',
        x='age_group',
        order=['Youth', 'Adults', 'Seniors'],
        palette=colors_,
        ax=ax
        )
    
    for p in bar.patches:
        bar.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    xytext=(0, 1),
                    textcoords='offset points',
                    ha='center', va='bottom',
                    fontsize=26)
        
    ax.set_title('Number of Customer by Age', loc='center', fontsize=40, pad=20)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=36)
    ax.tick_params(axis='y', labelsize=32)
    
    st.pyplot(fig)

# By State
colors_ = ['#90CAF9', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3', '#D3D3D3']
desc_bystate_df = bystate_df.sort_values(by='customer_count', ascending=False)

fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    data=desc_bystate_df,
    x='customer_count',
    y='state',
    palette=colors_,
    ax=ax
)
ax.set_title('Number of Customer by States', loc='center', fontsize=30, pad=16)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=24)
ax.tick_params(axis='x', labelsize=20)

for i, value in enumerate(desc_bystate_df['customer_count']):
    ax.text(
        x=value,
        y=i,
        s=value,
        va='center',
        fontsize=18
    )

st.pyplot(fig)

# Displays RFM (Recency, Frequency, & Monetary) Analysis
st.subheader('Best Customer Based on RFM Parameters')

col1, col2, col3 = st.columns(3)

with col1:
    avg_recency = round(rfm_df.recency.mean(), 1)
    st.metric('#Average Recency (days)', value=avg_recency)
 
with col2:
    avg_frequency = round(rfm_df.frequency.mean(), 2)
    st.metric('#Average Frequency', value=avg_frequency)

with col3:
    avg_frequency = format_currency(rfm_df.monetary.mean(), 'AUD', locale='es_CO') 
    st.metric('#Average Monetary', value=avg_frequency)


fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 10))
colors = ['#90CAF9']

# First plot
asc_recency_rfm_df = rfm_df.sort_values(by='recency', ascending=True).head(5)
sns.barplot(
    y='recency',
    x='customer_id',
    data=asc_recency_rfm_df,
    palette=colors,
    order=asc_recency_rfm_df['customer_id'],
    ax=ax[0]
)
ax[0].set_ylabel(None)
ax[0].set_xlabel('customer_id', fontsize=28, labelpad=10)
ax[0].set_title('By Recency (days)', loc='center', fontsize=32, pad=15)
ax[0].tick_params(axis ='x', labelsize=24)
ax[0].tick_params(axis ='y', labelsize=20)

for i, value in enumerate(asc_recency_rfm_df['recency']):
    ax[0].text(
        x=i,
        y=value,
        s=value,
        ha='center',
        fontsize=18
    )

# Second plot
desc_frequency_rfm_df = rfm_df.sort_values(by='frequency', ascending=False).head(5)
sns.barplot(
    y='frequency',
    x='customer_id',
    data=desc_frequency_rfm_df,
    palette=colors,
    order=desc_frequency_rfm_df['customer_id'],
    ax=ax[1]
)
ax[1].set_ylabel(None)
ax[1].set_xlabel('customer_id', fontsize=28, labelpad=10)
ax[1].set_title('By Frequency', loc='center', fontsize=32, pad=15)
ax[1].tick_params(axis='x', labelsize=22)
ax[1].tick_params(axis='y', labelsize=20)

for i, value in enumerate(desc_frequency_rfm_df['frequency']):
    ax[1].text(
        x=i,
        y=value,
        s=value,
        ha='center',
        fontsize=18

    )

# Third plot
desc_monetary_rfm_df = rfm_df.sort_values(by='monetary', ascending=False).head(5)
sns.barplot(
    y='monetary',
    x='customer_id',
    data=desc_monetary_rfm_df,
    palette=colors,
    order=desc_monetary_rfm_df['customer_id'],
    ax=ax[2]
)
ax[2].set_ylabel(None)
ax[2].set_xlabel('customer_id', fontsize=28, labelpad=10)
ax[2].set_title('By Monetary', loc='center', fontsize=32, pad=15)
ax[2].tick_params(axis='x', labelsize=22)
ax[2].tick_params(axis='y', labelsize=20)

for i, value in enumerate(desc_monetary_rfm_df['monetary']):
    ax[2].text(
        x=i,
        y=value,
        s=value,
        ha='center',
        fontsize=18
    )

st.pyplot(fig)


st.caption('Copyright (c) Dicoding 2023 | Author: Nurkholiq Agani Hafid')