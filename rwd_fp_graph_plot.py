import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

#--------CSVファイル--------------
csv_filenames = [
    "",
    "",
    "",
    "",
    "",
    "",
    ]
folder_path = '/Users/'


for csv_filename in csv_filenames:
    file_path = os.path.join(folder_path, csv_filename)

    if not os.path.exists(file_path):
        print(f"No such a File in Directory!!!")
        continue

    df = pd.read_csv(file_path)

    time_from_start = (df['timestamp']- df['timestamp'].iloc[0])/60000
    df['Time(min)'] = time_from_start - 30

    fig, ax = plt.subplots(figsize=(15,7))
    ax.plot(df['Time(min)'], df['DeltaF/F-1'], label="dF/F", color="green")

    graph_title = csv_filename.replace(".csv", "")
    ax.set_title(f"{graph_title}", fontsize=28)

    ax.set_xlabel("Time(minutes)", fontsize=26)
    ax.set_ylabel("dF/F", fontsize=26)
    ax.set_xlim(-30, 60)
    ax.set_ylim(top=6)
    ax.set_xticks(range(-30, 61, 15))
    ax.set_yticks(range(-2, 13, 2))
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
    ax.plot(df['Time(min)'], df['Zscore-1'], color="red")

    graph_title = csv_filename.replace(".csv", "")
    ax.set_title(f"{graph_title}", fontsize=28)

    ax.set_xlabel("Time (minutes)", fontsize=26)
    ax.set_ylabel("Z-score", fontsize=26)
    ax.set_xlim(-30, 60)
    
    ax.set_ylim(-4, 10)
    ax.set_yticks(range(-4, 11, 2))
    
    ax.set_xticks(range(-30, 61, 15))
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