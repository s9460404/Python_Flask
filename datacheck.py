import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import tkinter as tk
import tkinter.filedialog as filedialog
# import matplotlib.pyplot as plt
import scipy.special._cdflib

root = tk.Tk()
root.title("")
root.geometry("180x160")
# root.withdraw()

df_true = pd.read_excel('True.xlsx')

def select_file():
    file_path = filedialog.askopenfilename()
    
    if file_path:
        try:
            df_pre = pd.read_excel(file_path)
            # print(df[['新會員編號','label']])
            # print("成功")
            # print(file_path)
            result_left = pd.merge(df_true, df_pre, on='會員編號', how='left')
            print("Left Join:\n", result_left)
            conf_matrix = confusion_matrix(result_left['label_x'], result_left['label_y'], labels=['loyal', 'partial churn', 'churn'])
            print(conf_matrix)
            print("成功")
            # 計算準確率
            accuracy = accuracy_score(result_left['label_x'], result_left['label_y'])
            print(f"Accuracy: {accuracy:.2f}")
            # 顯示混淆矩陣並標注標籤名稱
            # disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['loyal', 'p_churn', 'churn'])
            # disp.plot(cmap=plt.cm.Blues) 
            
            label = tk.Label(root, text='準確率:'+str(accuracy), font=("Helvetica", 16))
            label.pack(padx=20, pady=20)
            
            # 使用藍色色調顯示
            # plt.title("Confusion Matrix with Labels")
            # plt.xlabel("Predicted Label")
            # plt.ylabel("True Label")
            # plt.show()
            

            # 將混淆矩陣轉換為 DataFrame 
            # conf_matrix_df = pd.DataFrame(conf_matrix, index=['A', 'B', 'C'], columns=['A', 'B', 'C'])
            # print(conf_matrix_df)
            
        except Exception as e:
            print(f"读取文件失败: {e}")


# select_file()
button = tk.Button(root, text="選擇文件", command=select_file)
button.pack(pady=20)
root.mainloop()
