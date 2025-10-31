import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
import os

#CSVファイル
csv_filenames = [
    "",
    "",
    "",
    "",
    "",
    "",
    ]
folder_path = '/Users/'

#∆F/Fグラフの設定
df_f_color = "green"

df_f_xmin = -30 #X軸の最小値
df_f_xmax = 61 #X軸の最大値
df_f_xtick = 15 #X軸の間隔

df_f_ymin = -4 #Y軸の最小値
df_f_ymax = 11 #Y軸の最大値
df_f_ytick = 2 #Y軸の間隔

#Z-scoreグラフの設定
z_score_color = "Blue"

z_score_xmin = -30
z_score_xmax = 61
z_score_xtick = 15

z_score_ymin = -4
z_score_ymax = 11
z_score_ytick = 2



for csv_filename in csv_filenames:
    file_path = os.path.join(folder_path, csv_filename)

    if not os.path.exists(file_path):
        print(f"No such a File in Directory!!!")
        continue

    df = pd.read_csv(file_path)

    time_from_start = (df['timestamp']- df['timestamp'].iloc[0])/60000
    df['Time(min)'] = time_from_start - 30

    fig, ax = plt.subplots(figsize=(15,7))
    ax.plot(df['Time(min)'], df['DeltaF/F-1'], label="dF/F", color=df_f_color)

    graph_title = csv_filename.replace(".csv", "")
    ax.set_title(f"{graph_title}", fontsize=28)

    ax.set_xlabel("Time(minutes)", fontsize=26)
    ax.set_ylabel("dF/F", fontsize=26)
    ax.set_xticks(range(df_f_xmin, df_f_xmax, df_f_xtick))
    ax.set_yticks(range(df_f_ymin, df_f_ymax, df_f_ytick))
    ax.tick_params(axis='both', which='major', labelsize=20)


    ax.axvline(x=0, color='grey', linestyle='--')
    ax.axvline(x=30, color='grey', linestyle='--')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    output_filename = csv_filename.replace(".csv", "_dFF.png")
    output_path = os.path.join(folder_path, output_filename)

    print(f"Now saving the graph: {output_path}")
    fig.savefig(output_path)

    plt.close(fig)
    
    
    
for csv_filename in csv_filenames:
    file_path = os.path.join(folder_path, csv_filename)

    if not os.path.exists(file_path):
        print(f"No such a File in Directory!!!")
        continue

    df = pd.read_csv(file_path)
    time_from_start = (df['timestamp'] - df['timestamp'].iloc[0]) / 60000
    df['Time(min)'] = time_from_start - 30

    fig, ax = plt.subplots(figsize=(15, 7))
    ax.plot(df['Time(min)'], df['Zscore-1'], color=z_score_color)

    graph_title = csv_filename.replace(".csv", "")
    ax.set_title(f"{graph_title}", fontsize=28)

    ax.set_xlabel("Time (minutes)", fontsize=26)
    ax.set_ylabel("Z-score", fontsize=26)
    ax.set_xticks(range(z_score_xmin, z_score_xmax, z_score_xtick))
    ax.set_yticks(range(z_score_ymin, z_score_ymax, z_score_ytick))
    ax.tick_params(axis='both', which='major', labelsize=20)

    ax.axvline(x=0, color='grey', linestyle='--')
    ax.axvline(x=30, color='grey', linestyle='--')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    output_filename = csv_filename.replace(".csv", "_Zscore.png")
    output_path = os.path.join(folder_path, output_filename)

    print(f"Now saving the graph: {output_path}")
    fig.savefig(output_path)

    plt.close(fig)

print("\nAll process is done!")