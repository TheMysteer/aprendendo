import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_random_data(n_days: int) -> pd.DataFrame:
    dates = pd.date_range(start="2023-01-01", periods=n_days, freq="D")

    data = {
        'date': dates,
        'sales': np.random.randint(50, 300, size=n_days),
        'profit': np.random.randint(10, 150, size=n_days),
        'expenses': np.random.randint(20, 200, size=n_days)
    }
    
    df = pd.DataFrame(data)
    return df

def display_basic_info(df: pd.DataFrame):
    print("Visualizando as 5 primeiras linhas do dataset:")
    print(df.head())
    print("\nResumo estatístico:")
    print(df.describe())
    print("\nCorrelação entre vendas, lucro e despesas:")
    correlation = df[['sales', 'profit', 'expenses']].corr()
    print(correlation)

def plot_sales_over_time(df: pd.DataFrame):
    df = df.copy()
    df.set_index('date', inplace=True)
    
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['sales'], marker='o', linestyle='-', color='blue')
    plt.title("Evolução das Vendas ao Longo do Tempo")
    plt.xlabel("Data")
    plt.ylabel("Vendas")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_profit_vs_expenses(df: pd.DataFrame):
    plt.figure(figsize=(8,6))
    plt.scatter(df['expenses'], df['profit'], alpha=0.7, color='green', edgecolor='k')
    plt.title("Lucro vs. Despesas")
    plt.xlabel("Despesas")
    plt.ylabel("Lucro")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def pivot_table_analysis(df: pd.DataFrame):

    df = df.copy()
    df['month'] = df['date'].dt.to_period("M")
    pivot_table = df.pivot_table(values=['sales', 'profit', 'expenses'], 
                                 index='month', aggfunc='mean')
    print("\nTabela dinâmica com médias mensais:")
    print(pivot_table)
    return pivot_table

def main():
    n_days = 365

    df = generate_random_data(n_days)

    display_basic_info(df)
    
    pivot_table_analysis(df)

    plot_sales_over_time(df)
    plot_profit_vs_expenses(df)
    
if __name__ == "__main__":
    main()
