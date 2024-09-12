import streamlit as st
import plotly.express as px
import pandas as pd 

st.set_page_config(
    page_title = 'Data Analytics Interface ',
    page_icon = '📊'
)

st.title('Data Analysis Interface')
st.subheader(':gray[Ez to Visualize the data]')

file = st.file_uploader('Attach CSV or excel file',type=['csv','xlsx'])
if(file!=None):
    if(file.name.endswith('csv')):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)

    st.dataframe(data)
    st.info(':green[File is uploaded successfully]',icon = '✅')

    st.subheader(':grey[Understanding Dataset]',divider='gray')
    tab1,tab2,tab3,tab4 = st.tabs(['Summary','Data Types','Columns','Missing Values'])

    with tab1:
        st.write(f'Dataset contains {data.shape[0]} rows and {data.shape[1]} columns ')
        st.subheader(':gray[Statistical Summary of the dataset]')
        st.dataframe(data.describe())

    with tab2:
        st.subheader(':gray[Display Data types of columns]')
        st.dataframe(data.dtypes)
    with tab3:
        st.subheader(':gray[Column Names in Dataset]')
        st.write(list(data.columns))
    with tab4:
        st.subheader(':gray[This dataset contains following missing values]')
        missing_values = data.isnull().sum()
        value_count = data.count()
        per_each_missing= missing_values/value_count *100
        percent_missing = data.isnull().sum().sum()/data.count().sum() * 100
        st.write(f'Total Missing value Percentage {percent_missing:.2f} %')
        newdf = pd.DataFrame({
            'Missing values':missing_values,
            'Value Count' : value_count,
            '% Missing value' : per_each_missing
        })
        #newdf.loc['Missing']= [missing_values,value_count,per_each_missing.round(2)]
        #  newdf['% Missing value'] = newdf['% Missing value'].round(2)

        st.dataframe(newdf)
        if(missing_values.sum() > 0 ):
            with st.expander(':orange[see Methods to handle missing values]'):
                st.write(
                    '''Here's a each technique for handling missing values:

                    1. **Dropping Rows**: Removes rows with missing values, suitable when missing data is minimal.
                    2. **Dropping Columns**: Deletes columns with too many missing values, useful when features are not essential.
                    3. **Mean/Median/Mode Imputation**: Fills missing numerical values with mean/median and categorical values with mode.
                    4. **Forward/Backward Fill**: Fills missing values using the previous or next data point in ordered datasets.
                    5. **Interpolation**: Estimates missing values based on linear or polynomial trends, ideal for continuous data.
                    6. **KNN Imputation**: Predicts missing values using the k-nearest neighbors algorithm based on feature similarity.
                    7. **MICE (Multiple Imputation)**: Uses multiple iterations to predict missing values by modeling relationships between variables.
                    8. **Regression Imputation**: Uses regression models to predict and fill missing values based on other features.
                    9. **Random Imputation**: Replaces missing values by randomly sampling from the existing distribution of the feature.
                    10. **Indicator for Missingness**: Creates a new binary feature to flag missing data and fill original values.
                    11. **Machine Learning Models**: Leverages algorithms like Random Forest or XGBoost to predict and impute missing values.
                    
                    Each method varies in complexity and appropriateness based on the data context.'''
                )

    st.subheader(':grey[Column Values To Count]',divider='gray')
    with st.expander('Value Count'):
        col1,col2 = st.columns(2)
        with col1:
          column  = st.selectbox('Choose Column name',options=list(data.columns))
        with col2:
            toprows = st.number_input('Top rows',min_value=1,step=1)
        
        count = st.button('Count')
        if(count==True):
            result = data[column].value_counts().reset_index().head(toprows)
            st.dataframe(result)
            st.subheader('Visualization',divider='gray')
            fig = px.bar(data_frame=result,x=column,y='count',text='count',template='plotly_white')
            st.plotly_chart(fig)
            fig = px.line(data_frame=result,x=column,y='count',text='count',template='plotly_white')
            st.plotly_chart(fig)
            fig = px.pie(data_frame=result,names=column,values='count')
            st.plotly_chart(fig)
    
    st.subheader(':grey[Groupby : Simplify your data analysis]',divider='gray')
    st.write(':gray[The groupby lets you summarize data by specific categories and groups]')
    with st.expander('Group By your columns'):
        col1,col2,col3 = st.columns(3)
        with col1:
            groupby_cols = st.multiselect('Choose your column to groupby',options = list(data.columns))
        with col2:
            operation_col = st.selectbox('Choose column for operation',options=list(data.columns))
        with col3:
            operation = st.selectbox('Choose operation',options=['sum','max','min','mean','median','count'])
        
        if(groupby_cols):
            result = data.groupby(groupby_cols).agg(
                newcol = (operation_col,operation)
            ).reset_index()

            st.dataframe(result)

            st.subheader(':gray[Data Visualization]',divider='gray')
            graphs = st.selectbox('Choose your graphs',options=['line','bar','scatter','pie','sunburst'])
            if(graphs=='line'):
                x_axis = st.selectbox('Choose X axis',options=list(result.columns))
                y_axis = st.selectbox('Choose Y axis',options=list(result.columns))
                color = st.selectbox('Color Information',options= [None] +list(result.columns))
                fig = px.line(data_frame=result,x=x_axis,y=y_axis,color=color,markers='o')
                st.plotly_chart(fig)
            elif(graphs=='bar'):
                 x_axis = st.selectbox('Choose X axis',options=list(result.columns))
                 y_axis = st.selectbox('Choose Y axis',options=list(result.columns))
                 color = st.selectbox('Color Information',options= [None] +list(result.columns))
                 facet_col = st.selectbox('Column Information',options=[None] +list(result.columns))
                 fig = px.bar(data_frame=result,x=x_axis,y=y_axis,color=color,facet_col=facet_col,barmode='group')
                 st.plotly_chart(fig)
            elif(graphs=='scatter'):
                x_axis = st.selectbox('Choose X axis',options=list(result.columns))
                y_axis = st.selectbox('Choose Y axis',options=list(result.columns))
                color = st.selectbox('Color Information',options= [None] +list(result.columns))
                size = st.selectbox('Size Column',options=[None] + list(result.columns))
                fig = px.scatter(data_frame=result,x=x_axis,y=y_axis,color=color,size=size)
                st.plotly_chart(fig)
            elif(graphs=='pie'):
                values = st.selectbox('Choose Numerical Values',options=list(result.columns))
                names = st.selectbox('Choose labels',options=list(result.columns))
                fig = px.pie(data_frame=result,values=values,names=names)
                st.plotly_chart(fig)
            elif(graphs=='sunburst'):
                path = st.multiselect('Choose your Path',options=list(result.columns))
                fig = px.sunburst(data_frame=result,path=path,values='newcol')
                st.plotly_chart(fig)
